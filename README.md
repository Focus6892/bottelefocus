# bottelefocus

Bot Telegram theo dõi biến động BTC, ETH, SOL cho giao dịch swing. Chạy miễn phí bằng GitHub Actions, dữ liệu lấy từ API công khai của Binance Futures và Deribit, không cần khóa API nào.

## Hoạt động

- Mỗi 15 phút quét một lần. Nếu xu hướng đổi (đi ngang sang tăng/giảm rõ, hoặc ngược lại) hay có tín hiệu mức cao (giá bung, long quá nóng, short quá đông, ATR tăng vọt) thì gửi cảnh báo ngay.
- Đầu mỗi giờ gửi bản tin tổng hợp 3 đồng.
- Cùng một cảnh báo không lặp lại trong 4 giờ.
- Chỉ báo lưu vào `state/history/` mỗi lần chạy để sau này chỉnh ngưỡng.

Xu hướng rõ = EMA20 và EMA50 cùng chiều trên cả 4h lẫn 1D, giá cùng phía EMA20, ADX14 trên 25. ADX trên 35 là xu hướng mạnh.

## Cài đặt (một lần)

1. Tạo bot với [@BotFather](https://t.me/BotFather), lấy token.
2. Thêm bot vào nhóm (hoặc chat riêng), gửi một tin bất kỳ, rồi mở `https://api.telegram.org/bot<TOKEN>/getUpdates` để lấy `chat.id`.
3. Trong repo: Settings → Secrets and variables → Actions → New repository secret, thêm:
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_CHAT_ID`
4. Vào tab Actions, chọn workflow "Quét chỉ báo BTC ETH SOL", bấm Run workflow để nhận bản tin đầu tiên.

Lưu ý: lịch GitHub Actions có thể trễ vài phút lúc cao điểm. Repo công khai không bị tính phút chạy; repo riêng tư có 2.000 phút miễn phí mỗi tháng, đủ cho lịch mỗi giờ (đổi cron thành `0 * * * *`).

## Chỉnh ngưỡng

Tất cả ngưỡng nằm trong `bot/config.py`.

## Chạy thử tại máy

```bash
pip install -r requirements.txt
python -m pytest tests -q
python -m bot.main --digest --dry   # in tin nhắn ra màn hình, không gửi
```
