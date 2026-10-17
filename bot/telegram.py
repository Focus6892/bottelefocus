"""Gửi tin nhắn Telegram qua Bot API."""
import os
import requests


def send(text, token=None, chat_id=None):
    token = token or os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = chat_id or os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print("[telegram] thiếu TELEGRAM_BOT_TOKEN hoặc TELEGRAM_CHAT_ID, in ra màn hình:\n" + text)
        return False
    r = requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={"chat_id": chat_id, "text": text, "parse_mode": "HTML", "disable_web_page_preview": True},
        timeout=20,
    )
    if r.status_code != 200:
        raise RuntimeError(f"Telegram lỗi {r.status_code}: {r.text[:200]}")
    return True
