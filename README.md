# bottelefocus

Bot Telegram theo dõi biến động BTC, ETH, SOL cho giao dịch swing. Chạy miễn phí bằng GitHub Actions, dữ liệu lấy từ API công khai của Binance Futures và Deribit, không cần khóa API nào.

## Hoạt động

- Mỗi 15 phút quét một lần. Cảnh báo ngay khi: EMA20 cắt EMA50 trên **khung ngày** (tín hiệu xu hướng chính, kèm dừng lỗ gợi ý 3,5 ATR ngày); Bollinger ngày nén rồi bung (ETH, SOL); nến 4h đóng ngoài vùng giá trị volume profile 30 ngày hoặc nến ngày đóng ngoài vùng 90 ngày (thoát qua VAH/VAL, thoát lệnh khi quay qua POC); nến 4h đóng ngoài nến mẹ (inside bar) cùng chiều EMA20/50 4h; hoặc tín hiệu khẩn 4h (giá bung, long quá nóng, short quá đông, ATR tăng vọt).
- Đầu mỗi giờ gửi bản tin tổng hợp 3 đồng, mở đầu bằng khối **Thị trường chung**: BTC.D, USDT.D, OTHERS.D (khung ngày, từ TradingView scanner; dự phòng CoinGecko) kèm hướng theo EMA20/50 và cách đọc dòng tiền (risk-off, mùa BTC, mùa alt...). Khi dòng tiền đổi trạng thái, bot báo riêng. Quy tắc đọc dominance là quy tắc kinh điển, chưa backtest; giá trị mỗi ngày được lưu vào `state/dominance.jsonl` để kiểm chứng sau.
- Mỗi đồng có dòng 🔮 dự báo biến động 24 giờ và 7 ngày tới từ volume profile 1h/4h/1D, tra theo thống kê 3 năm gộp 3 đồng trong `backtest/vp_vol.json` (nghiên cứu: `backtest/vp_vol.py`, kết quả `backtest/vp_vol.md`). Chỉ nhóm lệch nền |z| ≥ 2 mới được tính; hiệu ứng nhỏ (3–6 điểm) nên dùng để chỉnh dừng lỗ / khối lượng, không phải tín hiệu vào lệnh.
- Scalp 1h (⚡): hai cách còn lãi ngoài mẫu trong `backtest/scalp_1h.md` (lệnh chờ tại mép vùng giá trị 7 ngày cho ETH/SOL; nén Bollinger 48 giờ rồi bung cùng chiều ngày). Khung 15m lỗ ở mọi cách nên không dùng. Tắt bằng `SCALP_ALERTS = False` trong `bot/config.py`. Khung backtest scalp riêng: `backtest/scalp.py` (TP/SL/thời gian giữ, phí maker/taker, tối ưu 70% đầu, kiểm tra 30% cuối), chạy bằng workflow "Nghiên cứu VP biến động và scalp". Backtest scalp đa khung (`backtest/scalp_mtf.py`, kết quả `backtest/scalp_mtf.md`): 21 cách (thêm RSI2, Stoch RSI, dải EMA, MACD, TTM Squeeze, Donchian, VWAP theo xu hướng, phiên Á, đỉnh/đáy ngày trước, mùa vụ giờ, động lượng trong ngày) trên 5m/15m/30m/1h với lọc xu hướng 1h/4h/ngày, phí taker 0,05% + trượt 0,01%, chốt lời bằng lệnh chờ 0,02%. Chỉ lệnh chờ VAL/VAH 1h đạt chuẩn giữ; 5m/15m/30m không cách nào lãi ngoài mẫu, kể cả trước phí cũng gần hòa (`backtest/scalp_mtf_gross.md`). Chạy lại bằng workflow "Backtest scalp đa khung" (nến 5m được giữ trong cache, lần sau chỉ tải phần mới).
- Cùng một cảnh báo không lặp lại trong 4 giờ.
- Chỉ báo lưu vào `state/history/` mỗi lần chạy để sau này chỉnh ngưỡng.

Vì sao chọn khung ngày: backtest 6 năm (`backtest/results_1d.md`) cho thấy cắt EMA20/50 ngày có profit factor 2,4–3,2 ở cả ba đồng, trong khi mọi tín hiệu trên 4h (`backtest/results.md`) không vượt được mức nền. Pha 4h (EMA20/50 + ADX) chỉ hiển thị để tham khảo. Các chiến lược SMC (BOS/CHoCH, order block, fair value gap, quét thanh khoản) và price action (nhấn chìm, pin bar, phá rồi retest, inside bar) nằm ở `backtest/smc.py`, kết quả trong cùng bảng. Chạy lại backtest bằng workflow "Backtest xu hướng" (bỏ chọn `scalp` nếu chỉ cần 4h và 1D).

## Cơ chế nhiều agent (0 đồng, chạy bằng quy tắc)

- `bot/advisor.py` (agent đề xuất): gom hướng của từng biểu đồ (EMA20/50 ngày, Ichimoku ngày, SMA30 ngày theo Weinstein, VP 90 ngày, VP 30 ngày 4h, inside bar 4h, pha 4h, dòng tiền dominance) với trọng số theo profit factor backtest, ra khuyến nghị LONG / SHORT / ĐỨNG NGOÀI, độ tin cậy và dừng lỗ.
- `bot/reviewer.py` (agent review): soát lại trước khi gửi: bỏ nguồn có backtest yếu ở đồng đó (PF < 1,2 trong `backtest/results*.json`), bác khuyến nghị ngược khung ngày, giữ lại khi long alt lúc tiền rút về stablecoin hoặc biến động cực đoan, cảnh báo funding quá nóng và dừng lỗ quá xa, gợi ý khối lượng theo rủi ro 1% vốn.
- Kết quả hiện ở hai dòng 🤖 / 🧑‍⚖️ cuối mỗi đồng trong bản tin; khi khuyến nghị đã duyệt đổi, bot báo riêng. Backtest (`backtest/stock.py`, `smc.py`, `run.py`) là agent đánh giá: mọi trọng số phải có số liệu từ đó.

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
