# Chat với Claude Opus 5.5 qua Telegram

Nhắn tin cho bot trên Telegram, bot chuyển câu hỏi tới API Anthropic (model `claude-opus-5-5`) và trả lời lại. Bot nhớ 20 lượt hỏi gần nhất của mỗi chat, đọc được cả ảnh, và chỉ trả lời các chat id được phép.

Lệnh: `/new` xóa ngữ cảnh để bắt đầu chủ đề mới, `/id` xem chat id.

Phần này tách riêng khỏi bot cảnh báo (`bot/`): không dùng chung file, không đổi workflow nào.

## Vì sao không chạy bằng GitHub Actions

Bot cảnh báo chạy theo lịch 15 phút một lần, nên Actions là đủ. Chat thì cần trả lời ngay, nên bot phải chạy liên tục và hỏi Telegram có tin mới không (long polling). Actions không dành cho tiến trình chạy suốt ngày đêm, lịch lại trễ vài phút. Vì vậy bot chat chạy trên Railway (hoặc máy của bạn), không cần tên miền hay webhook.

## Cần chuẩn bị

1. **Khóa API Anthropic**: vào https://console.anthropic.com → Settings → API Keys → Create Key. Khóa này tính tiền riêng, không nằm trong gói claude.ai; cần nạp credit ở mục Billing. Giá Opus 5.5: 4 USD / 1 triệu token đầu vào, 20 USD / 1 triệu token đầu ra.
2. **Token bot Telegram**: dùng lại đúng token của bot cảnh báo được, vì bot cảnh báo chỉ gửi tin, không đọc tin. Muốn tách riêng thì tạo bot mới với [@BotFather](https://t.me/BotFather).
3. **Chat id của bạn**: nếu bot cảnh báo gửi vào chat riêng với bạn thì đó chính là `TELEGRAM_CHAT_ID`. Nếu nó gửi vào nhóm, cứ chạy bot trước rồi nhắn bất kỳ tin nào cho bot trong chat riêng; bot sẽ trả lời kèm chat id của bạn.

Không dán các giá trị này vào chat hay commit vào repo; chỉ nhập ở phần biến môi trường của nơi chạy bot.

## Chạy trên Railway (khuyên dùng, luôn bật)

1. Vào https://railway.com, đăng nhập bằng GitHub.
2. New Project → Deploy from GitHub repo → chọn `bottelefocus`. Railway đọc `railway.json` và build bằng `chatbot/Dockerfile`.
3. Mở service → tab Variables, thêm:
   - `ANTHROPIC_API_KEY`
   - `TELEGRAM_BOT_TOKEN`
   - `ALLOWED_CHAT_IDS` (chat id của bạn; nhiều id thì cách nhau dấu phẩy)
4. Railway tự deploy lại. Tab Deployments → Logs hiện dòng `@tên_bot đang chạy` là xong. Mở Telegram và nhắn cho bot.

Railway tính phí theo mức dùng (gói Hobby khoảng 5 USD/tháng, bot này dùng rất ít tài nguyên). Mỗi lần nhánh chính có thay đổi trong `chatbot/`, Railway tự build lại.

## Chạy trên máy của bạn (miễn phí, chỉ chạy khi máy bật)

```bash
pip install -r chatbot/requirements.txt
export ANTHROPIC_API_KEY=...        # Windows PowerShell: $env:ANTHROPIC_API_KEY="..."
export TELEGRAM_BOT_TOKEN=...
export ALLOWED_CHAT_IDS=...
python -m chatbot.main
```

Chỉ chạy một nơi một lúc: hai tiến trình cùng token sẽ tranh nhau đọc tin (log báo lỗi 409).

## Tùy chỉnh

| Biến | Mặc định | Ý nghĩa |
|---|---|---|
| `CLAUDE_MODEL` | `claude-opus-5-5` | Model dùng để trả lời |
| `CLAUDE_EFFORT` | `medium` | Mức suy nghĩ: `low`, `medium`, `high`, `xhigh`, `max`. Cao hơn thì kỹ hơn nhưng chậm và tốn hơn |
| `HISTORY_TURNS` | `20` | Số lượt hỏi gần nhất giữ làm ngữ cảnh |

Ngữ cảnh lưu trong bộ nhớ, nên mất khi bot khởi động lại. Nếu Claude từ chối vì bộ lọc an toàn, máy chủ Anthropic tự chạy lại bằng model dự phòng (`fallbacks: "default"`).
