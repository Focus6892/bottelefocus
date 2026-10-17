# bottelefocus

Bot Telegram theo dõi biến động BTC, ETH, SOL cho giao dịch swing. Chạy miễn phí bằng GitHub Actions, dữ liệu lấy từ API công khai của Binance Futures và Deribit, không cần khóa API nào.

## Hoạt động

- Mỗi 15 phút quét một lần. Cảnh báo ngay khi: EMA20 cắt EMA50 trên **khung ngày** (tín hiệu xu hướng chính, kèm dừng lỗ gợi ý 3,5 ATR ngày); Bollinger ngày nén rồi bung (ETH, SOL); nến 4h đóng ngoài vùng giá trị volume profile 30 ngày hoặc nến ngày đóng ngoài vùng 90 ngày (thoát qua VAH/VAL, thoát lệnh khi quay qua POC); hoặc tín hiệu khẩn 4h (giá bung, long quá nóng, short quá đông, ATR tăng vọt).
- Đầu mỗi giờ gửi bản tin tổng hợp 3 đồng, mở đầu bằng khối **Thị trường chung**: BTC.D, USDT.D, OTHERS.D (khung ngày, từ TradingView scanner; dự phòng CoinGecko) kèm hướng theo EMA20/50 và cách đọc dòng tiền (risk-off, mùa BTC, mùa alt...). Khi dòng tiền đổi trạng thái, bot báo riêng. Quy tắc đọc dominance là quy tắc kinh điển, chưa backtest; giá trị mỗi ngày được lưu vào `state/dominance.jsonl` để kiểm chứng sau.
- Cùng một cảnh báo không lặp lại trong 4 giờ.
- Chỉ báo lưu vào `state/history/` mỗi lần chạy để sau này chỉnh ngưỡng.

Vì sao chọn khung ngày: backtest 6 năm (`backtest/results_1d.md`) cho thấy cắt EMA20/50 ngày có profit factor 2,4–3,2 ở cả ba đồng, trong khi mọi tín hiệu trên 4h (`backtest/results.md`) không vượt được mức nền. Pha 4h (EMA20/50 + ADX) chỉ hiển thị để tham khảo. Các chiến lược SMC (BOS/CHoCH, order block, fair value gap, quét thanh khoản) và price action (nhấn chìm, pin bar, phá rồi retest, inside bar) nằm ở `backtest/smc.py`, kết quả trong cùng bảng. Chạy lại backtest bằng workflow "Backtest xu hướng" (bỏ chọn `scalp` nếu chỉ cần 4h và 1D).

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
