"""Chat trực tiếp với Claude qua Telegram (long polling, chạy liên tục).

Biến môi trường:
  ANTHROPIC_API_KEY     khóa API Anthropic (bắt buộc)
  TELEGRAM_BOT_TOKEN    token bot (bắt buộc; dùng chung được với bot cảnh báo vì bot đó chỉ gửi tin)
  ALLOWED_CHAT_IDS      các chat id được phép chat, cách nhau dấu phẩy (mặc định = TELEGRAM_CHAT_ID)
  CLAUDE_MODEL          mặc định claude-opus-5-5
  CLAUDE_EFFORT         low | medium | high | xhigh | max, mặc định medium
  HISTORY_TURNS         số lượt hỏi gần nhất giữ làm ngữ cảnh, mặc định 20
"""
import base64
import os
import threading
import time

import anthropic
import requests

MODEL = os.environ.get("CLAUDE_MODEL", "claude-opus-5-5")
EFFORT = os.environ.get("CLAUDE_EFFORT", "medium")
HISTORY_TURNS = int(os.environ.get("HISTORY_TURNS", "20"))
TG_LIMIT = 4000  # Telegram giới hạn 4096 ký tự mỗi tin

SYSTEM = (
    "Bạn là Claude, đang trò chuyện với người dùng qua Telegram. "
    "Trả lời bằng ngôn ngữ người dùng viết. Telegram hiển thị văn bản thuần, "
    "nên không dùng bảng Markdown hay tiêu đề #; danh sách gạch đầu dòng ngắn thì được."
)

HELP = (
    "Gửi tin nhắn hoặc ảnh (kèm chú thích) để chat với Claude.\n"
    "/new  bắt đầu cuộc trò chuyện mới (xóa ngữ cảnh)\n"
    "/id   xem chat id của bạn"
)


def parse_ids(raw):
    return {int(x) for x in raw.replace(" ", "").split(",") if x}


def trim(history, turns):
    """Giữ `turns` lượt hỏi gần nhất. Chỉ cắt từ đầu, tại tin của người dùng, để không sửa phần giữa lịch sử."""
    starts = [i for i, m in enumerate(history) if m["role"] == "user"]
    if len(starts) > turns:
        del history[: starts[-turns]]


def split_text(text, limit=TG_LIMIT):
    parts = []
    while len(text) > limit:
        cut = text.rfind("\n", 0, limit)
        if cut < limit // 2:
            cut = limit
        parts.append(text[:cut])
        text = text[cut:].lstrip("\n")
    if text:
        parts.append(text)
    return parts


class Telegram:
    def __init__(self, token):
        self.base = f"https://api.telegram.org/bot{token}"
        self.file_base = f"https://api.telegram.org/file/bot{token}"

    def call(self, method, timeout=30, **params):
        r = requests.post(f"{self.base}/{method}", json=params, timeout=timeout)
        data = r.json()
        if not data.get("ok"):
            raise RuntimeError(f"{method}: {r.status_code} {data.get('description')}")
        return data["result"]

    def poll(self, offset):
        r = requests.post(f"{self.base}/getUpdates", timeout=70, json={
            "offset": offset, "timeout": 50, "allowed_updates": ["message"]})
        data = r.json()
        if not data.get("ok"):
            raise RuntimeError(f"getUpdates: {r.status_code} {data.get('description')}")
        return data["result"]

    def send(self, chat_id, text, reply_to=None):
        for i, part in enumerate(split_text(text) or ["(trống)"]):
            params = {"chat_id": chat_id, "text": part, "disable_web_page_preview": True}
            if reply_to and i == 0:
                params["reply_parameters"] = {"message_id": reply_to, "allow_sending_without_reply": True}
            self.call("sendMessage", **params)

    def download(self, file_id):
        path = self.call("getFile", file_id=file_id)["file_path"]
        r = requests.get(f"{self.file_base}/{path}", timeout=60)
        r.raise_for_status()
        return r.content


def keep_typing(tg, chat_id, stop):
    while not stop.is_set():
        try:
            tg.call("sendChatAction", chat_id=chat_id, action="typing", timeout=10)
        except Exception:
            pass
        stop.wait(4)


def user_content(tg, msg):
    """Đổi tin Telegram thành nội dung gửi Claude; None nếu không hỗ trợ."""
    text = msg.get("text") or msg.get("caption") or ""
    blocks = []
    if msg.get("photo"):
        img = tg.download(msg["photo"][-1]["file_id"])  # ảnh lớn nhất
        blocks.append({"type": "image", "source": {
            "type": "base64", "media_type": "image/jpeg", "data": base64.standard_b64encode(img).decode()}})
    if not blocks:
        return text or None
    blocks.append({"type": "text", "text": text or "Mô tả ảnh này."})
    return blocks


def ask_claude(client, history):
    with client.beta.messages.stream(
        model=MODEL,
        max_tokens=64000,
        system=SYSTEM,
        messages=history,
        output_config={"effort": EFFORT},
        cache_control={"type": "ephemeral"},
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",  # bị từ chối do bộ lọc an toàn thì máy chủ tự chạy lại bằng mô hình dự phòng
    ) as stream:
        return stream.get_final_message()


def handle(tg, client, histories, msg):
    chat_id = msg["chat"]["id"]
    text = (msg.get("text") or "").strip()
    cmd = text.split()[0].split("@")[0].lower() if text.startswith("/") else ""

    if cmd in ("/start", "/help"):
        return tg.send(chat_id, HELP)
    if cmd == "/id":
        return tg.send(chat_id, f"Chat id: {chat_id}")
    if cmd == "/new":
        histories.pop(chat_id, None)
        return tg.send(chat_id, "Đã xóa ngữ cảnh, bắt đầu cuộc trò chuyện mới.")

    content = user_content(tg, msg)
    if content is None:
        return tg.send(chat_id, "Hiện bot chỉ đọc được chữ và ảnh.")

    history = histories.setdefault(chat_id, [])
    history.append({"role": "user", "content": content})
    stop = threading.Event()
    threading.Thread(target=keep_typing, args=(tg, chat_id, stop), daemon=True).start()
    try:
        resp = ask_claude(client, history)
    except anthropic.APIStatusError as e:
        history.pop()
        return tg.send(chat_id, f"Lỗi API Claude ({e.status_code}): {e.message}")
    except anthropic.APIConnectionError:
        history.pop()
        return tg.send(chat_id, "Không kết nối được tới API Claude, thử lại sau nhé.")
    finally:
        stop.set()

    if resp.stop_reason == "refusal":
        history.pop()
        return tg.send(chat_id, "Claude từ chối trả lời yêu cầu này.", reply_to=msg["message_id"])

    # Giữ nguyên toàn bộ khối trả về (kể cả thinking) để lượt sau gửi lại đúng như cũ.
    history.append({"role": "assistant", "content": [b.to_dict() for b in resp.content]})
    trim(history, HISTORY_TURNS)
    answer = "\n".join(b.text for b in resp.content if b.type == "text").strip()
    if resp.stop_reason == "max_tokens":
        answer += "\n\n(câu trả lời bị cắt vì quá dài)"
    tg.send(chat_id, answer, reply_to=msg["message_id"])


def main():
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    allowed = parse_ids(os.environ.get("ALLOWED_CHAT_IDS") or os.environ.get("TELEGRAM_CHAT_ID", ""))
    tg = Telegram(token)
    client = anthropic.Anthropic()  # đọc ANTHROPIC_API_KEY
    histories = {}

    tg.call("deleteWebhook")  # getUpdates không chạy được khi bot đang đặt webhook
    me = tg.call("getMe")
    print(f"[chatbot] @{me['username']} đang chạy, model {MODEL}, cho phép {sorted(allowed) or 'không ai'}", flush=True)

    offset = None
    while True:
        try:
            updates = tg.poll(offset)
        except Exception as e:
            print(f"[chatbot] getUpdates lỗi: {e}", flush=True)
            time.sleep(10)  # 409 = có tiến trình khác đang chạy cùng token
            continue
        for u in updates:
            offset = u["update_id"] + 1
            msg = u.get("message")
            if not msg:
                continue
            chat_id = msg["chat"]["id"]
            if chat_id not in allowed:
                tg.send(chat_id, f"Chat này chưa được phép dùng bot. Chat id: {chat_id}")
                continue
            try:
                handle(tg, client, histories, msg)
            except Exception as e:
                print(f"[chatbot] lỗi xử lý tin: {e!r}", flush=True)
                try:
                    tg.send(chat_id, f"Có lỗi: {e}")
                except Exception:
                    pass


if __name__ == "__main__":
    main()
