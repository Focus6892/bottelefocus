# Scalp đa khung · 5m, 15m, 30m, 1h · nến 5m OKX 3 năm gộp lên

Mỗi ô: PF trung bình NGOÀI MẪU của 3 đồng (BTC, ETH, SOL) · lãi trung bình mỗi đồng · lệnh/ngày/đồng · kết luận. Bộ lọc khung lớn và tham số TP/SL/giữ đều chọn TRONG MẪU (70% đầu); ngoài mẫu là 30% cuối, chưa từng dùng để chọn. Chi phí: vào lệnh thị trường 0,05% + trượt 0,01%; chốt lời bằng lệnh chờ 0,02%; dừng lỗ 0,05% + trượt 0,01%.

- 5m: 315359 nến BTC, 2023-10-19 đến 2026-10-18, ngoài mẫu từ 2025-11-23
- 15m: 105119 nến BTC, 2023-10-19 đến 2026-10-18, ngoài mẫu từ 2025-11-23
- 30m: 52560 nến BTC, 2023-10-19 đến 2026-10-18, ngoài mẫu từ 2025-11-23
- 1h: 26280 nến BTC, 2023-10-19 đến 2026-10-18, ngoài mẫu từ 2025-11-23

## Tổng hợp: bộ lọc chọn trong mẫu

| Cách | 5m | 15m | 30m | 1h |
|---|---|---|---|---|
| VP: từ chối tại VAL/VAH | 0.63 · -78% · 4.1/ngày · không lọc · **BỎ** | 0.74 · -61% · 2.4/ngày · không lọc · **BỎ** | 0.78 · -43% · 1.1/ngày · không lọc · **BỎ** | 0.81 · -5% · 0.1/ngày · lọc 4h + ngày · **BỎ** |
| VP: từ chối tại VAL/VAH, chốt ở POC | 0.46 · -45% · 1.7/ngày · lọc 4h + ngày · **BỎ** | 0.51 · -50% · 1.8/ngày · lọc 4h · **BỎ** | 0.64 · -25% · 0.8/ngày · lọc 4h · **BỎ** | 0.82 · -9% · 0.3/ngày · lọc ngày · **BỎ** |
| VP: lệnh chờ tại VAL/VAH | 0.75 · -28% · 2.8/ngày · lọc 1h · **BỎ** | 0.96 · -5% · 1.2/ngày · lọc 4h + ngày · **BỎ** | 0.85 · -9% · 0.6/ngày · lọc 4h + ngày · **BỎ** | 1.25 · +26% · 0.7/ngày · không lọc · **GIỮ** |
| Hồi theo xu hướng 4h rồi vượt đỉnh nến trước | 0.62 · -79% · 4.2/ngày · lọc 1h · **BỎ** | 0.81 · -42% · 2.0/ngày · không lọc · **BỎ** | 0.91 · -13% · 0.8/ngày · lọc 1h · **BỎ** | 0.70 · -24% · 0.4/ngày · lọc 4h + ngày · **BỎ** |
| VWAP phiên: xuyên -1 sd rồi đóng lại | 0.63 · -98% · 10.5/ngày · không lọc · **BỎ** | 0.76 · -64% · 2.8/ngày · lọc 4h · **BỎ** | 0.82 · -43% · 1.5/ngày · lọc 1h · **BỎ** | 0.93 · -20% · 0.9/ngày · lọc ngày · **BỎ** |
| VWAP phiên: hồi chạm VWAP theo xu hướng EMA | 0.60 · -68% · 3.0/ngày · lọc 1h · **BỎ** | 0.80 · -53% · 2.7/ngày · không lọc · **BỎ** | 0.94 · -13% · 1.0/ngày · lọc 4h · **BỎ** | 1.00 · +2% · 0.8/ngày · lọc 4h · **BỎ** |
| Nén Bollinger 48 nến rồi bung + khối lượng | 0.55 · -54% · 1.9/ngày · lọc 1h · **BỎ** | 0.71 · -38% · 1.4/ngày · không lọc · **BỎ** | 0.87 · -15% · 0.7/ngày · không lọc · **BỎ** | 1.12 · +10% · 0.3/ngày · không lọc · **THEO DÕI** |
| TTM Squeeze (Bollinger trong Keltner) bung | 0.55 · -46% · 1.4/ngày · lọc 1h · **BỎ** | 0.74 · -30% · 1.2/ngày · không lọc · **BỎ** | 0.75 · -11% · 0.4/ngày · lọc 4h · **BỎ** | 1.25 · +5% · 0.1/ngày · lọc 4h + ngày · **THEO DÕI** |
| VP: thoát vùng qua node thấp + khối lượng | 0.68 · -22% · 0.7/ngày · lọc 4h + ngày · **BỎ** | 0.86 · -16% · 0.8/ngày · lọc 4h · **BỎ** | 0.94 · -4% · 0.3/ngày · lọc 4h + ngày · **BỎ** | 1.11 · +3% · 0.1/ngày · lọc ngày · **THEO DÕI** |
| Bung biên độ 60 phút đầu ngày UTC | 0.63 · -24% · 0.8/ngày · lọc 1h · **BỎ** | 0.86 · -9% · 0.5/ngày · lọc 4h + ngày · **BỎ** | 0.77 · -16% · 0.5/ngày · lọc 4h + ngày · **BỎ** | 0.93 · -8% · 0.4/ngày · lọc 4h + ngày · **BỎ** |
| Dải EMA 8/13/21 hồi chạm EMA21 | 0.61 · -78% · 4.1/ngày · lọc 4h · **BỎ** | 0.76 · -40% · 1.4/ngày · lọc 4h · **BỎ** | 1.04 · +4% · 0.7/ngày · lọc ngày · **BỎ** | 0.87 · -8% · 0.2/ngày · lọc 4h + ngày · **BỎ** |
| Stoch RSI cắt ở vùng quá mua/bán theo EMA50 | 0.64 · -52% · 1.9/ngày · lọc 4h + ngày · **BỎ** | 0.86 · -22% · 1.1/ngày · lọc 4h · **BỎ** | 0.90 · -14% · 0.7/ngày · lọc 4h · **BỎ** | 0.90 · -11% · 0.5/ngày · lọc 4h · **BỎ** |
| Connors RSI(2) < 10 / > 90 theo EMA200 | 0.66 · -76% · 4.3/ngày · lọc 4h · **BỎ** | 0.89 · -16% · 0.9/ngày · lọc 4h + ngày · **BỎ** | 0.87 · -26% · 1.0/ngày · lọc 4h · **BỎ** | 0.82 · -19% · 0.3/ngày · lọc 4h + ngày · **BỎ** |
| MACD histogram đổi dấu theo EMA200 | 0.66 · -49% · 2.3/ngày · lọc 4h · **BỎ** | 0.63 · -39% · 0.9/ngày · lọc 4h · **BỎ** | 0.77 · -13% · 0.3/ngày · lọc 4h + ngày · **BỎ** | 0.62 · -17% · 0.2/ngày · lọc 4h + ngày · **BỎ** |
| Phá đỉnh/đáy 20 nến (Donchian) | 0.63 · -88% · 6.1/ngày · lọc 1h · **BỎ** | 0.72 · -78% · 3.5/ngày · không lọc · **BỎ** | 0.87 · -24% · 0.9/ngày · lọc 4h · **BỎ** | 0.90 · -14% · 0.5/ngày · lọc ngày · **BỎ** |
| Quét đỉnh/đáy phiên Á rồi quay lại | 0.50 · -12% · 0.3/ngày · lọc 4h + ngày · **BỎ** | 0.71 · -31% · 1.1/ngày · không lọc · **BỎ** | 0.77 · -17% · 0.5/ngày · lọc 4h · **BỎ** | 0.82 · -16% · 0.5/ngày · lọc 4h · **BỎ** |
| Phá biên phiên Á giờ London | 0.39 · -13% · 0.3/ngày · lọc 1h · **BỎ** | 0.60 · -6% · 0.2/ngày · lọc 4h + ngày · **BỎ** | 0.95 · -3% · 0.3/ngày · lọc ngày · **BỎ** | 0.80 · -11% · 0.3/ngày · lọc ngày · **BỎ** |
| Quét đỉnh/đáy ngày trước rồi quay lại | 0.79 · -8% · 0.4/ngày · lọc ngày · **BỎ** | 0.76 · -23% · 0.8/ngày · không lọc · **BỎ** | 0.77 · -26% · 0.7/ngày · không lọc · **BỎ** | 0.82 · -12% · 0.3/ngày · lọc ngày · **BỎ** |
| Mùa vụ giờ: mua 22:00, bán 00:00 UTC | 0.48 · -28% · 0.5/ngày · lọc 1h · **BỎ** | 0.48 · -28% · 0.5/ngày · lọc 1h · **BỎ** | 0.48 · -28% · 0.5/ngày · lọc 1h · **BỎ** | 0.70 · -7% · 0.2/ngày · lọc 4h + ngày · **BỎ** |
| Động lượng đầu ngày -> cuối ngày UTC | 0.26 · -14% · 0.3/ngày · lọc 4h + ngày · **BỎ** | 0.26 · -14% · 0.3/ngày · lọc 4h + ngày · **BỎ** | 0.26 · -14% · 0.3/ngày · lọc 4h + ngày · **BỎ** | 0.67 · -6% · 0.3/ngày · lọc 4h + ngày · **BỎ** |
| Động lượng đầu phiên Mỹ -> cuối phiên | 0.16 · -24% · 0.4/ngày · lọc 1h · **BỎ** | 0.16 · -24% · 0.4/ngày · lọc 1h · **BỎ** | 0.16 · -24% · 0.4/ngày · lọc 1h · **BỎ** | không đủ lệnh |

## Các biến thể đạt GIỮ hoặc THEO DÕI (mọi bộ lọc)

Dấu ✓ ở cột cuối: đây là bộ lọc được chọn trong mẫu. Biến thể không có ✓ chỉ đẹp khi nhìn ngoài mẫu, dễ là may.

| Khung | Cách | Lọc | TP/SL/giữ | PF trong mẫu | BTC | ETH | SOL | Hai nửa ngoài mẫu | Lệnh/ngày | Kết luận | Chọn trong mẫu |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1h | TTM Squeeze (Bollinger trong Keltner) bung | lọc ngày | 1.0/1.5/8 | 1.27 | PF 1.22 · +3% · 56 lệnh | PF 1.58 · +12% · 62 lệnh | PF 1.02 · +0% · 49 lệnh | 1.28 / 1.24 | 0.2 | GIỮ: lãi ngoài mẫu ở >= 2 đồng, không đồng nào lỗ rõ, hai nửa ngoài mẫu đều dương |  |
| 1h | VP: lệnh chờ tại VAL/VAH | không lọc | 1.0/1.5/8 | 1.20 | PF 1.06 · +4% · 247 lệnh | PF 1.32 · +29% · 214 lệnh | PF 1.37 · +45% · 250 lệnh | 1.51 / 1.02 | 0.7 | GIỮ: lãi ngoài mẫu ở >= 2 đồng, không đồng nào lỗ rõ, hai nửa ngoài mẫu đều dương | ✓ |
| 1h | Nén Bollinger 48 nến rồi bung + khối lượng | lọc 4h + ngày | 3.0/1.5/8 | 1.00 | PF 1.14 · +2% · 41 lệnh | PF 1.80 · +16% · 36 lệnh | PF 1.48 · +11% · 34 lệnh | 1.72 / 1.25 | 0.1 | THEO DÕI: ngoài mẫu hơi dương nhưng chưa đủ chuẩn giữ: trong mẫu yếu |  |
| 1h | Nén Bollinger 48 nến rồi bung + khối lượng | lọc 4h | 3.0/1.5/8 | 0.99 | PF 1.00 · -0% · 71 lệnh | PF 1.37 · +14% · 65 lệnh | PF 1.96 · +33% · 64 lệnh | 1.55 / 1.34 | 0.2 | THEO DÕI: ngoài mẫu hơi dương nhưng chưa đủ chuẩn giữ: trong mẫu yếu |  |
| 1h | VP: thoát vùng qua node thấp + khối lượng | lọc 4h | 3.0/1.5/16 | 1.04 | PF 1.14 · +4% · 54 lệnh | PF 1.26 · +10% · 56 lệnh | PF 1.60 · +23% · 54 lệnh | 1.67 / 1.00 | 0.2 | THEO DÕI: ngoài mẫu hơi dương nhưng chưa đủ chuẩn giữ: trong mẫu yếu |  |
| 1h | Nén Bollinger 48 nến rồi bung + khối lượng | lọc ngày | 3.0/1.5/8 | 1.01 | PF 1.15 · +4% · 68 lệnh | PF 1.42 · +15% · 65 lệnh | PF 1.33 · +12% · 56 lệnh | 1.76 / 0.91 | 0.2 | THEO DÕI: ngoài mẫu hơi dương nhưng chưa đủ chuẩn giữ: một nửa ngoài mẫu âm, trong mẫu yếu |  |
| 1h | TTM Squeeze (Bollinger trong Keltner) bung | lọc 4h + ngày | 2.0/1.5/8 | 1.31 | PF 0.98 · -1% · 37 lệnh | PF 1.64 · +12% · 38 lệnh | PF 1.12 · +2% · 33 lệnh | 1.29 / 1.19 | 0.1 | THEO DÕI: ngoài mẫu hơi dương nhưng chưa đủ chuẩn giữ: ít đồng đạt PF 1,15 | ✓ |
| 1h | TTM Squeeze (Bollinger trong Keltner) bung | lọc 4h | 2.0/1.5/8 | 1.18 | PF 1.03 · +0% · 58 lệnh | PF 1.67 · +19% · 58 lệnh | PF 0.97 · -2% · 59 lệnh | 1.14 / 1.27 | 0.2 | THEO DÕI: ngoài mẫu hơi dương nhưng chưa đủ chuẩn giữ: ít đồng đạt PF 1,15 |  |
| 1h | VP: lệnh chờ tại VAL/VAH | lọc 4h + ngày | 1.0/1.5/8 | 1.20 | PF 0.87 · -2% · 47 lệnh | PF 1.42 · +8% · 55 lệnh | PF 1.32 · +6% · 48 lệnh | 1.68 / 0.88 | 0.2 | THEO DÕI: ngoài mẫu hơi dương nhưng chưa đủ chuẩn giữ: có đồng lỗ, một nửa ngoài mẫu âm |  |
| 1h | VP: lệnh chờ tại VAL/VAH | lọc 4h | 1.0/1.5/8 | 1.18 | PF 0.93 · -2% · 74 lệnh | PF 1.34 · +9% · 73 lệnh | PF 1.32 · +10% · 77 lệnh | 1.46 / 1.00 | 0.2 | THEO DÕI: ngoài mẫu hơi dương nhưng chưa đủ chuẩn giữ: có đồng lỗ |  |
| 1h | VP: thoát vùng qua node thấp + khối lượng | không lọc | 3.0/1.5/48 | 1.08 | PF 0.91 · -6% · 77 lệnh | PF 1.20 · +12% · 82 lệnh | PF 1.29 · +18% · 74 lệnh | 1.14 / 1.15 | 0.2 | THEO DÕI: ngoài mẫu hơi dương nhưng chưa đủ chuẩn giữ: có đồng lỗ |  |
| 30m | Dải EMA 8/13/21 hồi chạm EMA21 | lọc 4h + ngày | 3.0/1.5/48 | 0.95 | PF 0.96 · -4% · 142 lệnh | PF 1.19 · +14% · 129 lệnh | PF 1.23 · +19% · 117 lệnh | 0.97 / 1.38 | 0.4 | THEO DÕI: ngoài mẫu hơi dương nhưng chưa đủ chuẩn giữ: một nửa ngoài mẫu âm, trong mẫu yếu |  |
| 30m | Dải EMA 8/13/21 hồi chạm EMA21 | lọc 4h | 3.0/1.5/48 | 0.94 | PF 0.93 · -8% · 227 lệnh | PF 1.15 · +16% · 203 lệnh | PF 1.29 · +41% · 202 lệnh | 1.02 / 1.30 | 0.6 | THEO DÕI: ngoài mẫu hơi dương nhưng chưa đủ chuẩn giữ: có đồng lỗ, trong mẫu yếu |  |
| 1h | TTM Squeeze (Bollinger trong Keltner) bung | không lọc | 2.0/1.5/8 | 1.09 | PF 1.06 · +2% · 113 lệnh | PF 1.32 · +21% · 132 lệnh | PF 0.98 · -2% · 106 lệnh | 1.05 / 1.22 | 0.4 | THEO DÕI: ngoài mẫu hơi dương nhưng chưa đủ chuẩn giữ: ít đồng đạt PF 1,15 |  |
| 1h | Nén Bollinger 48 nến rồi bung + khối lượng | không lọc | 3.0/1.5/48 | 1.08 | PF 0.96 · -3% · 113 lệnh | PF 1.07 · +4% · 111 lệnh | PF 1.33 · +30% · 105 lệnh | 1.20 / 1.05 | 0.3 | THEO DÕI: ngoài mẫu hơi dương nhưng chưa đủ chuẩn giữ: ít đồng đạt PF 1,15 | ✓ |
| 1h | VP: từ chối tại VAL/VAH | không lọc | 3.0/1.5/48 | 1.03 | PF 1.21 · +19% · 148 lệnh | PF 1.06 · +5% · 143 lệnh | PF 1.09 · +10% · 151 lệnh | 1.11 / 1.11 | 0.4 | THEO DÕI: ngoài mẫu hơi dương nhưng chưa đủ chuẩn giữ: ít đồng đạt PF 1,15, trong mẫu yếu |  |
| 1h | VP: từ chối tại VAL/VAH | lọc ngày | 3.0/1.0/48 | 1.03 | PF 1.27 · +11% · 91 lệnh | PF 1.08 · +3% · 86 lệnh | PF 1.00 · -1% · 81 lệnh | 1.25 / 0.94 | 0.3 | THEO DÕI: ngoài mẫu hơi dương nhưng chưa đủ chuẩn giữ: ít đồng đạt PF 1,15, một nửa ngoài mẫu âm, trong mẫu yếu |  |
| 1h | VP: lệnh chờ tại VAL/VAH | lọc ngày | 1.0/1.5/8 | 1.10 | PF 1.17 · +6% · 122 lệnh | PF 0.90 · -6% · 127 lệnh | PF 1.26 · +13% · 117 lệnh | 1.27 / 0.93 | 0.4 | THEO DÕI: ngoài mẫu hơi dương nhưng chưa đủ chuẩn giữ: có đồng lỗ, một nửa ngoài mẫu âm |  |
| 30m | Phá biên phiên Á giờ London | lọc 4h + ngày | 2.0/1.5/48 | 0.77 | PF 0.81 · -5% · 60 lệnh | PF 1.28 · +6% · 54 lệnh | PF 1.23 · +5% · 48 lệnh | 0.87 / 1.46 | 0.2 | THEO DÕI: ngoài mẫu hơi dương nhưng chưa đủ chuẩn giữ: có đồng lỗ, một nửa ngoài mẫu âm, trong mẫu yếu |  |
| 1h | VP: thoát vùng qua node thấp + khối lượng | lọc ngày | 3.0/1.5/48 | 1.17 | PF 0.76 · -8% · 38 lệnh | PF 1.14 · +4% · 41 lệnh | PF 1.41 · +13% · 36 lệnh | 1.04 / 1.22 | 0.1 | THEO DÕI: ngoài mẫu hơi dương nhưng chưa đủ chuẩn giữ: ít đồng đạt PF 1,15, có đồng lỗ | ✓ |
| 1h | VWAP phiên: hồi chạm VWAP theo xu hướng EMA | lọc 4h + ngày | 3.0/1.0/48 | 0.93 | PF 0.96 · -5% · 142 lệnh | PF 1.03 · +1% · 164 lệnh | PF 1.19 · +22% · 148 lệnh | 1.16 / 0.98 | 0.5 | THEO DÕI: ngoài mẫu hơi dương nhưng chưa đủ chuẩn giữ: ít đồng đạt PF 1,15, một nửa ngoài mẫu âm, trong mẫu yếu |  |

## Chi tiết khung 5m

| Cách | Lọc | Tín hiệu BTC/ETH/SOL | TP/SL/giữ | PF trong mẫu | BTC ngoài mẫu | ETH ngoài mẫu | SOL ngoài mẫu | Kết luận |
|---|---|---|---|---|---|---|---|---|
| VP: từ chối tại VAL/VAH | không lọc | 7947/8852/9081 | 3.0/1.5/48 | 0.66 | PF 0.57 · -75% · 1279 lệnh | PF 0.68 · -75% · 1375 lệnh | PF 0.64 · -84% · 1411 lệnh | BỎ |
| VP: từ chối tại VAL/VAH | lọc 1h | 3187/3881/3684 | 3.0/1.5/48 | 0.65 | PF 0.57 · -43% · 529 lệnh | PF 0.72 · -37% · 558 lệnh | PF 0.70 · -43% · 550 lệnh | BỎ |
| VP: từ chối tại VAL/VAH | lọc 4h | 3889/4551/4348 | 3.0/1.5/48 | 0.65 | PF 0.57 · -50% · 638 lệnh | PF 0.68 · -49% · 696 lệnh | PF 0.62 · -59% · 673 lệnh | BỎ |
| VP: từ chối tại VAL/VAH | lọc ngày | 4088/4597/4664 | 3.0/1.5/48 | 0.63 | PF 0.54 · -53% · 650 lệnh | PF 0.66 · -51% · 695 lệnh | PF 0.62 · -63% · 741 lệnh | BỎ |
| VP: từ chối tại VAL/VAH | lọc 4h + ngày | 2545/3043/2840 | 3.0/1.5/48 | 0.64 | PF 0.58 · -35% · 398 lệnh | PF 0.65 · -39% · 448 lệnh | PF 0.69 · -38% · 427 lệnh | BỎ |
| VP: từ chối tại VAL/VAH, chốt ở POC | không lọc | 7947/8852/9081 | 1.0/0.5/48 | 0.52 | PF 0.40 · -82% · 1596 lệnh | PF 0.58 · -78% · 1750 lệnh | PF 0.44 · -91% · 1870 lệnh | BỎ |
| VP: từ chối tại VAL/VAH, chốt ở POC | lọc 1h | 3187/3881/3684 | 1.0/0.5/48 | 0.51 | PF 0.38 · -50% · 639 lệnh | PF 0.55 · -47% · 714 lệnh | PF 0.47 · -57% · 721 lệnh | BỎ |
| VP: từ chối tại VAL/VAH, chốt ở POC | lọc 4h | 3889/4551/4348 | 1.0/0.5/48 | 0.51 | PF 0.40 · -57% · 802 lệnh | PF 0.55 · -55% · 861 lệnh | PF 0.43 · -68% · 883 lệnh | BỎ |
| VP: từ chối tại VAL/VAH, chốt ở POC | lọc ngày | 4088/4597/4664 | 1.0/0.5/48 | 0.53 | PF 0.40 · -58% · 818 lệnh | PF 0.58 · -54% · 876 lệnh | PF 0.41 · -73% · 1005 lệnh | BỎ |
| VP: từ chối tại VAL/VAH, chốt ở POC | lọc 4h + ngày | 2545/3043/2840 | 1.0/0.5/48 | 0.54 | PF 0.40 · -42% · 504 lệnh | PF 0.55 · -41% · 563 lệnh | PF 0.42 · -53% · 577 lệnh | BỎ |
| VP: lệnh chờ tại VAL/VAH | không lọc | 15192/15560/16175 | 1.0/1.5/48 | 0.79 | PF 0.66 · -63% · 2216 lệnh | PF 0.80 · -52% · 2196 lệnh | PF 0.84 · -50% · 2431 lệnh | BỎ |
| VP: lệnh chờ tại VAL/VAH | lọc 1h | 6007/6515/6399 | 1.0/1.5/48 | 0.82 | PF 0.64 · -34% · 882 lệnh | PF 0.79 · -26% · 924 lệnh | PF 0.83 · -24% · 947 lệnh | BỎ |
| VP: lệnh chờ tại VAL/VAH | lọc 4h | 7553/7915/7794 | 1.0/1.5/48 | 0.81 | PF 0.62 · -42% · 1111 lệnh | PF 0.76 · -35% · 1109 lệnh | PF 0.78 · -37% · 1159 lệnh | BỎ |
| VP: lệnh chờ tại VAL/VAH | lọc ngày | 7676/7899/8193 | 1.0/1.5/48 | 0.81 | PF 0.62 · -44% · 1122 lệnh | PF 0.74 · -36% · 1072 lệnh | PF 0.80 · -36% · 1281 lệnh | BỎ |
| VP: lệnh chờ tại VAL/VAH | lọc 4h + ngày | 4906/5229/4993 | 1.0/1.5/48 | 0.81 | PF 0.61 · -31% · 687 lệnh | PF 0.75 · -25% · 694 lệnh | PF 0.82 · -21% · 729 lệnh | BỎ |
| Hồi theo xu hướng 4h rồi vượt đỉnh nến trước | không lọc | 11898/11574/11038 | 3.0/1.5/48 | 0.73 | PF 0.52 · -91% · 2078 lệnh | PF 0.61 · -91% · 2024 lệnh | PF 0.66 · -90% · 2016 lệnh | BỎ |
| Hồi theo xu hướng 4h rồi vượt đỉnh nến trước | lọc 1h | 8747/8303/7850 | 3.0/1.5/48 | 0.75 | PF 0.55 · -81% · 1445 lệnh | PF 0.64 · -79% · 1375 lệnh | PF 0.68 · -79% · 1349 lệnh | BỎ |
| Hồi theo xu hướng 4h rồi vượt đỉnh nến trước | lọc 4h | 11898/11574/11038 | 3.0/1.5/48 | 0.73 | PF 0.52 · -91% · 2078 lệnh | PF 0.61 · -91% · 2024 lệnh | PF 0.66 · -90% · 2016 lệnh | BỎ |
| Hồi theo xu hướng 4h rồi vượt đỉnh nến trước | lọc ngày | 7602/7395/6785 | 3.0/1.5/48 | 0.73 | PF 0.55 · -77% · 1245 lệnh | PF 0.62 · -77% · 1239 lệnh | PF 0.68 · -74% · 1154 lệnh | BỎ |
| Hồi theo xu hướng 4h rồi vượt đỉnh nến trước | lọc 4h + ngày | 7602/7395/6785 | 3.0/1.5/48 | 0.73 | PF 0.55 · -77% · 1245 lệnh | PF 0.62 · -77% · 1239 lệnh | PF 0.68 · -74% · 1154 lệnh | BỎ |
| VWAP phiên: xuyên -1 sd rồi đóng lại | không lọc | 26695/26975/26814 | 3.0/1.5/48 | 0.66 | PF 0.58 · -97% · 3532 lệnh | PF 0.64 · -98% · 3433 lệnh | PF 0.66 · -98% · 3368 lệnh | BỎ |
| VWAP phiên: xuyên -1 sd rồi đóng lại | lọc 1h | 12509/12831/12379 | 3.0/1.5/48 | 0.64 | PF 0.53 · -86% · 1835 lệnh | PF 0.62 · -86% · 1771 lệnh | PF 0.62 · -89% · 1772 lệnh | BỎ |
| VWAP phiên: xuyên -1 sd rồi đóng lại | lọc 4h | 13360/13713/13168 | 3.0/1.5/48 | 0.65 | PF 0.56 · -87% · 1974 lệnh | PF 0.63 · -87% · 1914 lệnh | PF 0.63 · -91% · 1915 lệnh | BỎ |
| VWAP phiên: xuyên -1 sd rồi đóng lại | lọc ngày | 13219/13583/13338 | 3.0/1.5/48 | 0.65 | PF 0.57 · -86% · 1918 lệnh | PF 0.67 · -83% · 1862 lệnh | PF 0.68 · -86% · 1885 lệnh | BỎ |
| VWAP phiên: xuyên -1 sd rồi đóng lại | lọc 4h + ngày | 8517/8769/8144 | 3.0/1.5/48 | 0.65 | PF 0.57 · -70% · 1156 lệnh | PF 0.68 · -67% · 1122 lệnh | PF 0.68 · -69% · 1072 lệnh | BỎ |
| VWAP phiên: hồi chạm VWAP theo xu hướng EMA | không lọc | 12875/13287/12742 | 3.0/1.5/48 | 0.70 | PF 0.50 · -89% · 1826 lệnh | PF 0.65 · -85% · 1840 lệnh | PF 0.64 · -89% · 1806 lệnh | BỎ |
| VWAP phiên: hồi chạm VWAP theo xu hướng EMA | lọc 1h | 6466/6872/6486 | 3.0/1.5/48 | 0.71 | PF 0.52 · -67% · 979 lệnh | PF 0.66 · -64% · 1035 lệnh | PF 0.61 · -73% · 955 lệnh | BỎ |
| VWAP phiên: hồi chạm VWAP theo xu hướng EMA | lọc 4h | 6445/6960/6606 | 3.0/1.5/48 | 0.69 | PF 0.50 · -69% · 979 lệnh | PF 0.63 · -70% · 1084 lệnh | PF 0.64 · -72% · 1028 lệnh | BỎ |
| VWAP phiên: hồi chạm VWAP theo xu hướng EMA | lọc ngày | 6345/6711/6444 | 3.0/1.5/48 | 0.68 | PF 0.51 · -69% · 990 lệnh | PF 0.65 · -65% · 1018 lệnh | PF 0.67 · -66% · 951 lệnh | BỎ |
| VWAP phiên: hồi chạm VWAP theo xu hướng EMA | lọc 4h + ngày | 4078/4452/4167 | 3.0/1.5/48 | 0.67 | PF 0.51 · -51% · 583 lệnh | PF 0.65 · -50% · 647 lệnh | PF 0.66 · -51% · 582 lệnh | BỎ |
| Nén Bollinger 48 nến rồi bung + khối lượng | không lọc | 7128/7714/6889 | 3.0/1.5/48 | 0.66 | PF 0.55 · -69% · 1190 lệnh | PF 0.55 · -81% · 1288 lệnh | PF 0.62 · -75% · 1136 lệnh | BỎ |
| Nén Bollinger 48 nến rồi bung + khối lượng | lọc 1h | 3732/3942/3540 | 3.0/1.5/48 | 0.69 | PF 0.52 · -49% · 642 lệnh | PF 0.51 · -61% · 653 lệnh | PF 0.61 · -52% · 593 lệnh | BỎ |
| Nén Bollinger 48 nến rồi bung + khối lượng | lọc 4h | 3708/3925/3586 | 3.0/1.5/48 | 0.67 | PF 0.56 · -44% · 611 lệnh | PF 0.56 · -58% · 684 lệnh | PF 0.66 · -46% · 579 lệnh | BỎ |
| Nén Bollinger 48 nến rồi bung + khối lượng | lọc ngày | 3674/3939/3546 | 3.0/1.5/48 | 0.67 | PF 0.56 · -45% · 623 lệnh | PF 0.56 · -59% · 692 lệnh | PF 0.63 · -51% · 590 lệnh | BỎ |
| Nén Bollinger 48 nến rồi bung + khối lượng | lọc 4h + ngày | 2393/2529/2274 | 3.0/1.5/48 | 0.67 | PF 0.57 · -32% · 379 lệnh | PF 0.57 · -42% · 426 lệnh | PF 0.73 · -25% · 324 lệnh | BỎ |
| TTM Squeeze (Bollinger trong Keltner) bung | không lọc | 2562/3514/3202 | 3.0/1.5/48 | 0.68 | PF 0.55 · -54% · 743 lệnh | PF 0.57 · -73% · 1022 lệnh | PF 0.62 · -71% · 991 lệnh | BỎ |
| TTM Squeeze (Bollinger trong Keltner) bung | lọc 1h | 1282/1725/1570 | 3.0/1.5/48 | 0.71 | PF 0.58 · -32% · 398 lệnh | PF 0.52 · -53% · 517 lệnh | PF 0.55 · -52% · 496 lệnh | BỎ |
| TTM Squeeze (Bollinger trong Keltner) bung | lọc 4h | 1306/1824/1616 | 3.0/1.5/48 | 0.70 | PF 0.62 · -29% · 396 lệnh | PF 0.62 · -45% · 550 lệnh | PF 0.67 · -41% · 509 lệnh | BỎ |
| TTM Squeeze (Bollinger trong Keltner) bung | lọc ngày | 1303/1785/1618 | 3.0/1.5/48 | 0.67 | PF 0.64 · -27% · 387 lệnh | PF 0.66 · -40% · 530 lệnh | PF 0.55 · -54% · 523 lệnh | BỎ |
| TTM Squeeze (Bollinger trong Keltner) bung | lọc 4h + ngày | 842/1168/1009 | 3.0/1.5/48 | 0.71 | PF 0.66 · -17% · 241 lệnh | PF 0.71 · -24% · 330 lệnh | PF 0.63 · -30% · 285 lệnh | BỎ |
| VP: thoát vùng qua node thấp + khối lượng | không lọc | 2655/2692/2667 | 3.0/1.5/48 | 0.76 | PF 0.56 · -59% · 778 lệnh | PF 0.64 · -60% · 737 lệnh | PF 0.68 · -57% · 723 lệnh | BỎ |
| VP: thoát vùng qua node thấp + khối lượng | lọc 1h | 1593/1604/1673 | 3.0/1.5/48 | 0.78 | PF 0.58 · -39% · 447 lệnh | PF 0.58 · -48% · 423 lệnh | PF 0.67 · -40% · 431 lệnh | BỎ |
| VP: thoát vùng qua node thấp + khối lượng | lọc 4h | 1356/1355/1435 | 3.0/1.5/48 | 0.79 | PF 0.62 · -31% · 385 lệnh | PF 0.71 · -30% · 365 lệnh | PF 0.70 · -33% · 373 lệnh | BỎ |
| VP: thoát vùng qua node thấp + khối lượng | lọc ngày | 1313/1399/1358 | 3.0/1.5/48 | 0.78 | PF 0.60 · -32% · 389 lệnh | PF 0.72 · -30% · 388 lệnh | PF 0.59 · -45% · 370 lệnh | BỎ |
| VP: thoát vùng qua node thấp + khối lượng | lọc 4h + ngày | 849/892/900 | 3.0/1.5/48 | 0.80 | PF 0.71 · -16% · 232 lệnh | PF 0.73 · -21% · 242 lệnh | PF 0.59 · -30% · 219 lệnh | BỎ |
| Bung biên độ 60 phút đầu ngày UTC | không lọc | 1838/1813/1838 | 3.0/1.5/48 | 0.73 | PF 0.58 · -41% · 550 lệnh | PF 0.61 · -47% · 543 lệnh | PF 0.64 · -49% · 550 lệnh | BỎ |
| Bung biên độ 60 phút đầu ngày UTC | lọc 1h | 873/859/881 | 3.0/1.5/48 | 0.84 | PF 0.60 · -21% · 261 lệnh | PF 0.59 · -28% · 262 lệnh | PF 0.71 · -22% · 253 lệnh | BỎ |
| Bung biên độ 60 phút đầu ngày UTC | lọc 4h | 910/889/914 | 3.0/1.5/48 | 0.78 | PF 0.53 · -26% · 271 lệnh | PF 0.62 · -26% · 267 lệnh | PF 0.68 · -25% · 264 lệnh | BỎ |
| Bung biên độ 60 phút đầu ngày UTC | lọc ngày | 914/901/930 | 3.0/1.5/48 | 0.78 | PF 0.58 · -24% · 276 lệnh | PF 0.61 · -28% · 278 lệnh | PF 0.69 · -25% · 275 lệnh | BỎ |
| Bung biên độ 60 phút đầu ngày UTC | lọc 4h + ngày | 578/567/575 | 3.0/1.5/48 | 0.83 | PF 0.64 · -12% · 162 lệnh | PF 0.67 · -16% · 165 lệnh | PF 0.75 · -12% · 150 lệnh | BỎ |
| Dải EMA 8/13/21 hồi chạm EMA21 | không lọc | 15758/16018/15395 | 3.0/1.5/48 | 0.71 | PF 0.52 · -95% · 2602 lệnh | PF 0.61 · -96% · 2654 lệnh | PF 0.67 · -94% · 2512 lệnh | BỎ |
| Dải EMA 8/13/21 hồi chạm EMA21 | lọc 1h | 8070/8063/7729 | 3.0/1.5/48 | 0.72 | PF 0.55 · -78% · 1391 lệnh | PF 0.61 · -81% · 1373 lệnh | PF 0.61 · -82% · 1290 lệnh | BỎ |
| Dải EMA 8/13/21 hồi chạm EMA21 | lọc 4h | 8044/8027/7792 | 3.0/1.5/48 | 0.73 | PF 0.56 · -76% · 1368 lệnh | PF 0.64 · -78% · 1399 lệnh | PF 0.62 · -82% · 1279 lệnh | BỎ |
| Dải EMA 8/13/21 hồi chạm EMA21 | lọc ngày | 7921/8146/7920 | 3.0/1.5/48 | 0.70 | PF 0.52 · -79% · 1335 lệnh | PF 0.62 · -80% · 1417 lệnh | PF 0.63 · -81% · 1290 lệnh | BỎ |
| Dải EMA 8/13/21 hồi chạm EMA21 | lọc 4h + ngày | 5082/5159/4914 | 3.0/1.5/48 | 0.72 | PF 0.59 · -57% · 813 lệnh | PF 0.65 · -61% · 867 lệnh | PF 0.63 · -62% · 725 lệnh | BỎ |
| Stoch RSI cắt ở vùng quá mua/bán theo EMA50 | không lọc | 10017/10440/10195 | 3.0/1.5/48 | 0.73 | PF 0.55 · -91% · 2059 lệnh | PF 0.60 · -92% · 2026 lệnh | PF 0.62 · -94% · 2067 lệnh | BỎ |
| Stoch RSI cắt ở vùng quá mua/bán theo EMA50 | lọc 1h | 5587/5720/5610 | 3.0/1.5/48 | 0.74 | PF 0.58 · -72% · 1141 lệnh | PF 0.57 · -81% · 1131 lệnh | PF 0.56 · -85% · 1118 lệnh | BỎ |
| Stoch RSI cắt ở vùng quá mua/bán theo EMA50 | lọc 4h | 5083/5241/5235 | 3.0/1.5/48 | 0.75 | PF 0.60 · -66% · 1040 lệnh | PF 0.60 · -75% · 1048 lệnh | PF 0.60 · -80% · 1082 lệnh | BỎ |
| Stoch RSI cắt ở vùng quá mua/bán theo EMA50 | lọc ngày | 5085/5314/5120 | 3.0/1.5/48 | 0.72 | PF 0.54 · -70% · 1026 lệnh | PF 0.66 · -67% · 1041 lệnh | PF 0.68 · -70% · 1057 lệnh | BỎ |
| Stoch RSI cắt ở vùng quá mua/bán theo EMA50 | lọc 4h + ngày | 3265/3388/3232 | 3.0/1.5/48 | 0.75 | PF 0.60 · -49% · 624 lệnh | PF 0.65 · -53% · 632 lệnh | PF 0.68 · -54% · 626 lệnh | BỎ |
| Connors RSI(2) < 10 / > 90 theo EMA200 | không lọc | 15119/15212/15270 | 3.0/1.5/48 | 0.74 | PF 0.58 · -94% · 2755 lệnh | PF 0.66 · -93% · 2613 lệnh | PF 0.71 · -93% · 2676 lệnh | BỎ |
| Connors RSI(2) < 10 / > 90 theo EMA200 | lọc 1h | 10517/10413/10635 | 3.0/1.5/48 | 0.74 | PF 0.58 · -85% · 1854 lệnh | PF 0.65 · -86% · 1780 lệnh | PF 0.65 · -89% · 1832 lệnh | BỎ |
| Connors RSI(2) < 10 / > 90 theo EMA200 | lọc 4h | 8179/8008/8364 | 3.0/1.5/48 | 0.75 | PF 0.61 · -76% · 1436 lệnh | PF 0.70 · -73% · 1370 lệnh | PF 0.69 · -80% · 1440 lệnh | BỎ |
| Connors RSI(2) < 10 / > 90 theo EMA200 | lọc ngày | 7666/7645/7599 | 3.0/1.5/48 | 0.74 | PF 0.59 · -75% · 1343 lệnh | PF 0.67 · -73% · 1302 lệnh | PF 0.73 · -71% · 1329 lệnh | BỎ |
| Connors RSI(2) < 10 / > 90 theo EMA200 | lọc 4h + ngày | 5183/5088/5081 | 3.0/1.5/48 | 0.75 | PF 0.63 · -56% · 831 lệnh | PF 0.72 · -53% · 811 lệnh | PF 0.71 · -60% · 816 lệnh | BỎ |
| MACD histogram đổi dấu theo EMA200 | không lọc | 5281/5178/5173 | 3.0/1.5/48 | 0.69 | PF 0.56 · -74% · 1418 lệnh | PF 0.66 · -72% · 1359 lệnh | PF 0.70 · -74% · 1433 lệnh | BỎ |
| MACD histogram đổi dấu theo EMA200 | lọc 1h | 3805/3743/3871 | 3.0/1.5/48 | 0.70 | PF 0.57 · -61% · 1007 lệnh | PF 0.64 · -63% · 1001 lệnh | PF 0.72 · -62% · 1072 lệnh | BỎ |
| MACD histogram đổi dấu theo EMA200 | lọc 4h | 2889/2807/2847 | 3.0/1.5/48 | 0.72 | PF 0.56 · -53% · 736 lệnh | PF 0.66 · -52% · 739 lệnh | PF 0.77 · -43% · 780 lệnh | BỎ |
| MACD histogram đổi dấu theo EMA200 | lọc ngày | 2670/2617/2544 | 3.0/1.5/48 | 0.70 | PF 0.52 · -53% · 701 lệnh | PF 0.67 · -48% · 700 lệnh | PF 0.72 · -47% · 718 lệnh | BỎ |
| MACD histogram đổi dấu theo EMA200 | lọc 4h + ngày | 1819/1791/1700 | 3.0/1.5/48 | 0.71 | PF 0.52 · -40% · 425 lệnh | PF 0.69 · -35% · 451 lệnh | PF 0.79 · -26% · 440 lệnh | BỎ |
| Phá đỉnh/đáy 20 nến (Donchian) | không lọc | 22813/20654/22547 | 3.0/1.5/48 | 0.67 | PF 0.53 · -99% · 3907 lệnh | PF 0.64 · -98% · 3559 lệnh | PF 0.67 · -98% · 3652 lệnh | BỎ |
| Phá đỉnh/đáy 20 nến (Donchian) | lọc 1h | 11264/10195/11226 | 3.0/1.5/48 | 0.68 | PF 0.55 · -90% · 2128 lệnh | PF 0.66 · -86% · 1877 lệnh | PF 0.68 · -89% · 1959 lệnh | BỎ |
| Phá đỉnh/đáy 20 nến (Donchian) | lọc 4h | 11613/10507/11519 | 3.0/1.5/48 | 0.67 | PF 0.54 · -91% · 2111 lệnh | PF 0.66 · -86% · 1898 lệnh | PF 0.68 · -89% · 1965 lệnh | BỎ |
| Phá đỉnh/đáy 20 nến (Donchian) | lọc ngày | 11599/10680/11505 | 3.0/1.5/48 | 0.68 | PF 0.55 · -90% · 2069 lệnh | PF 0.67 · -86% · 1927 lệnh | PF 0.69 · -88% · 1971 lệnh | BỎ |
| Phá đỉnh/đáy 20 nến (Donchian) | lọc 4h + ngày | 7491/6907/7147 | 3.0/1.5/48 | 0.68 | PF 0.57 · -75% · 1275 lệnh | PF 0.69 · -68% · 1170 lệnh | PF 0.71 · -70% · 1136 lệnh | BỎ |
| Quét đỉnh/đáy phiên Á rồi quay lại | không lọc | 1277/1270/1253 | 3.0/0.5/48 | 0.61 | PF 0.52 · -34% · 374 lệnh | PF 0.58 · -37% · 378 lệnh | PF 0.69 · -30% · 391 lệnh | BỎ |
| Quét đỉnh/đáy phiên Á rồi quay lại | lọc 1h | 633/630/606 | 1.5/0.5/48 | 0.56 | PF 0.42 · -18% · 180 lệnh | PF 0.62 · -13% · 176 lệnh | PF 0.59 · -17% · 190 lệnh | BỎ |
| Quét đỉnh/đáy phiên Á rồi quay lại | lọc 4h | 629/652/619 | 2.0/0.5/48 | 0.61 | PF 0.56 · -14% · 181 lệnh | PF 0.54 · -20% · 191 lệnh | PF 0.64 · -17% · 207 lệnh | BỎ |
| Quét đỉnh/đáy phiên Á rồi quay lại | lọc ngày | 632/626/628 | 2.0/0.5/48 | 0.58 | PF 0.47 · -18% · 184 lệnh | PF 0.48 · -23% · 186 lệnh | PF 0.61 · -18% · 197 lệnh | BỎ |
| Quét đỉnh/đáy phiên Á rồi quay lại | lọc 4h + ngày | 397/413/388 | 1.5/0.5/48 | 0.62 | PF 0.49 · -9% · 105 lệnh | PF 0.53 · -12% · 117 lệnh | PF 0.49 · -14% · 116 lệnh | BỎ |
| Phá biên phiên Á giờ London | không lọc | 715/714/733 | 1.5/1.5/48 | 0.60 | PF 0.36 · -20% · 206 lệnh | PF 0.50 · -19% · 201 lệnh | PF 0.45 · -26% · 211 lệnh | BỎ |
| Phá biên phiên Á giờ London | lọc 1h | 353/344/382 | 1.5/1.5/48 | 0.65 | PF 0.28 · -13% · 105 lệnh | PF 0.39 · -13% · 99 lệnh | PF 0.51 · -13% · 112 lệnh | BỎ |
| Phá biên phiên Á giờ London | lọc 4h | 368/339/377 | 1.5/1.5/48 | 0.62 | PF 0.38 · -10% · 105 lệnh | PF 0.44 · -11% · 101 lệnh | PF 0.74 · -5% · 97 lệnh | BỎ |
| Phá biên phiên Á giờ London | lọc ngày | 363/361/371 | 3.0/1.5/48 | 0.64 | PF 0.70 · -6% · 107 lệnh | PF 0.52 · -14% · 109 lệnh | PF 0.74 · -8% · 107 lệnh | BỎ |
| Phá biên phiên Á giờ London | lọc 4h + ngày | 240/224/234 | 2.0/1.5/48 | 0.64 | PF 0.54 · -5% · 65 lệnh | PF 0.42 · -9% · 67 lệnh | PF 0.89 · -1% · 53 lệnh | BỎ |
| Quét đỉnh/đáy ngày trước rồi quay lại | không lọc | 874/854/913 | 3.0/0.5/48 | 0.69 | PF 0.71 · -18% · 261 lệnh | PF 0.70 · -22% · 249 lệnh | PF 0.64 · -29% · 262 lệnh | BỎ |
| Quét đỉnh/đáy ngày trước rồi quay lại | lọc 1h | 285/269/279 | 3.0/0.5/48 | 0.62 | PF 0.68 · -6% · 94 lệnh | PF 0.61 · -11% · 87 lệnh | PF 0.39 · -17% · 86 lệnh | BỎ |
| Quét đỉnh/đáy ngày trước rồi quay lại | lọc 4h | 407/406/432 | 3.0/0.5/48 | 0.70 | PF 0.91 · -3% · 130 lệnh | PF 0.62 · -14% · 120 lệnh | PF 0.54 · -19% · 124 lệnh | BỎ |
| Quét đỉnh/đáy ngày trước rồi quay lại | lọc ngày | 431/413/453 | 3.0/0.5/48 | 0.72 | PF 0.67 · -10% · 131 lệnh | PF 0.89 · -4% · 126 lệnh | PF 0.80 · -9% · 144 lệnh | BỎ |
| Quét đỉnh/đáy ngày trước rồi quay lại | lọc 4h + ngày | 260/264/264 | 3.0/0.5/48 | 0.68 | PF 0.75 · -5% · 81 lệnh | PF 0.72 · -7% · 78 lệnh | PF 0.55 · -13% · 77 lệnh | BỎ |
| Mùa vụ giờ: mua 22:00, bán 00:00 UTC | không lọc | 1095/1095/1095 | 1.0/0.5/8 | 0.76 | PF 0.41 · -42% · 329 lệnh | PF 0.48 · -48% · 329 lệnh | PF 0.59 · -43% · 329 lệnh | BỎ |
| Mùa vụ giờ: mua 22:00, bán 00:00 UTC | lọc 1h | 597/550/557 | 1.0/0.5/8 | 0.91 | PF 0.52 · -22% · 171 lệnh | PF 0.39 · -34% · 161 lệnh | PF 0.53 · -28% · 165 lệnh | BỎ |
| Mùa vụ giờ: mua 22:00, bán 00:00 UTC | lọc 4h | 602/565/567 | 1.0/0.5/8 | 0.87 | PF 0.46 · -21% · 162 lệnh | PF 0.53 · -26% · 173 lệnh | PF 0.63 · -21% · 158 lệnh | BỎ |
| Mùa vụ giờ: mua 22:00, bán 00:00 UTC | lọc ngày | 652/572/570 | 1.0/0.5/8 | 0.83 | PF 0.35 · -17% · 107 lệnh | PF 0.31 · -26% · 127 lệnh | PF 0.64 · -10% · 80 lệnh | BỎ |
| Mùa vụ giờ: mua 22:00, bán 00:00 UTC | lọc 4h + ngày | 427/366/357 | 1.0/0.5/8 | 0.89 | PF 0.49 · -8% · 69 lệnh | PF 0.40 · -15% · 84 lệnh | PF 1.22 · +2% · 47 lệnh | BỎ |
| Động lượng đầu ngày -> cuối ngày UTC | không lọc | 1094/1093/1083 | 1.0/0.5/8 | 0.47 | PF 0.15 · -39% · 329 lệnh | PF 0.24 · -38% · 328 lệnh | PF 0.30 · -36% · 322 lệnh | BỎ |
| Động lượng đầu ngày -> cuối ngày UTC | lọc 1h | 555/549/540 | 1.0/0.5/8 | 0.51 | PF 0.15 · -22% · 164 lệnh | PF 0.21 · -23% · 161 lệnh | PF 0.27 · -22% · 155 lệnh | BỎ |
| Động lượng đầu ngày -> cuối ngày UTC | lọc 4h | 575/596/589 | 1.0/0.5/8 | 0.51 | PF 0.19 · -21% · 164 lệnh | PF 0.23 · -24% · 167 lệnh | PF 0.29 · -24% · 171 lệnh | BỎ |
| Động lượng đầu ngày -> cuối ngày UTC | lọc ngày | 535/550/557 | 1.0/0.5/8 | 0.51 | PF 0.20 · -19% · 161 lệnh | PF 0.21 · -22% · 170 lệnh | PF 0.30 · -21% · 165 lệnh | BỎ |
| Động lượng đầu ngày -> cuối ngày UTC | lọc 4h + ngày | 355/371/364 | 1.0/0.5/8 | 0.58 | PF 0.26 · -12% · 97 lệnh | PF 0.23 · -14% · 103 lệnh | PF 0.30 · -16% · 98 lệnh | BỎ |
| Động lượng đầu phiên Mỹ -> cuối phiên | không lọc | 782/782/776 | 1.0/0.5/8 | 0.56 | PF 0.24 · -30% · 235 lệnh | PF 0.24 · -35% · 235 lệnh | PF 0.30 · -33% · 233 lệnh | BỎ |
| Động lượng đầu phiên Mỹ -> cuối phiên | lọc 1h | 427/430/410 | 1.0/0.5/8 | 0.61 | PF 0.15 · -22% · 134 lệnh | PF 0.12 · -26% · 128 lệnh | PF 0.21 · -25% · 125 lệnh | BỎ |
| Động lượng đầu phiên Mỹ -> cuối phiên | lọc 4h | 388/397/382 | 1.0/0.5/8 | 0.57 | PF 0.24 · -16% · 121 lệnh | PF 0.20 · -21% · 120 lệnh | PF 0.28 · -21% · 124 lệnh | BỎ |
| Động lượng đầu phiên Mỹ -> cuối phiên | lọc ngày | 392/391/384 | 1.0/0.5/8 | 0.50 | PF 0.20 · -19% · 119 lệnh | PF 0.20 · -22% · 112 lệnh | PF 0.27 · -20% · 114 lệnh | BỎ |
| Động lượng đầu phiên Mỹ -> cuối phiên | lọc 4h + ngày | 246/253/231 | 1.0/0.5/8 | 0.51 | PF 0.19 · -11% · 69 lệnh | PF 0.15 · -15% · 67 lệnh | PF 0.30 · -11% · 68 lệnh | BỎ |

## Chi tiết khung 15m

| Cách | Lọc | Tín hiệu BTC/ETH/SOL | TP/SL/giữ | PF trong mẫu | BTC ngoài mẫu | ETH ngoài mẫu | SOL ngoài mẫu | Kết luận |
|---|---|---|---|---|---|---|---|---|
| VP: từ chối tại VAL/VAH | không lọc | 5424/5824/5856 | 3.0/1.5/48 | 0.78 | PF 0.66 · -64% · 772 lệnh | PF 0.80 · -53% · 769 lệnh | PF 0.77 · -66% · 802 lệnh | BỎ |
| VP: từ chối tại VAL/VAH | lọc 1h | 2171/2488/2324 | 3.0/1.5/48 | 0.77 | PF 0.60 · -40% · 320 lệnh | PF 0.79 · -28% · 339 lệnh | PF 0.74 · -38% · 323 lệnh | BỎ |
| VP: từ chối tại VAL/VAH | lọc 4h | 2688/2998/2847 | 3.0/1.5/48 | 0.78 | PF 0.69 · -38% · 411 lệnh | PF 0.72 · -43% · 408 lệnh | PF 0.71 · -48% · 412 lệnh | BỎ |
| VP: từ chối tại VAL/VAH | lọc ngày | 2814/3054/3018 | 3.0/1.5/48 | 0.75 | PF 0.64 · -45% · 424 lệnh | PF 0.79 · -35% · 415 lệnh | PF 0.69 · -54% · 446 lệnh | BỎ |
| VP: từ chối tại VAL/VAH | lọc 4h + ngày | 1754/2029/1853 | 3.0/1.5/48 | 0.76 | PF 0.70 · -25% · 248 lệnh | PF 0.68 · -34% · 259 lệnh | PF 0.67 · -38% · 251 lệnh | BỎ |
| VP: từ chối tại VAL/VAH, chốt ở POC | không lọc | 5424/5824/5856 | 1.0/0.5/48 | 0.56 | PF 0.50 · -70% · 1098 lệnh | PF 0.67 · -62% · 1136 lệnh | PF 0.59 · -74% · 1205 lệnh | BỎ |
| VP: từ chối tại VAL/VAH, chốt ở POC | lọc 1h | 2171/2488/2324 | 1.0/0.5/48 | 0.55 | PF 0.46 · -39% · 448 lệnh | PF 0.71 · -28% · 478 lệnh | PF 0.63 · -37% · 468 lệnh | BỎ |
| VP: từ chối tại VAL/VAH, chốt ở POC | lọc 4h | 2688/2998/2847 | 1.0/0.5/48 | 0.57 | PF 0.46 · -48% · 562 lệnh | PF 0.58 · -45% · 571 lệnh | PF 0.49 · -56% · 594 lệnh | BỎ |
| VP: từ chối tại VAL/VAH, chốt ở POC | lọc ngày | 2814/3054/3018 | 1.0/0.5/48 | 0.53 | PF 0.42 · -52% · 582 lệnh | PF 0.69 · -36% · 574 lệnh | PF 0.50 · -60% · 650 lệnh | BỎ |
| VP: từ chối tại VAL/VAH, chốt ở POC | lọc 4h + ngày | 1754/2029/1853 | 1.0/0.5/48 | 0.54 | PF 0.40 · -37% · 347 lệnh | PF 0.60 · -31% · 370 lệnh | PF 0.44 · -45% · 376 lệnh | BỎ |
| VP: lệnh chờ tại VAL/VAH | không lọc | 9241/9441/9527 | 1.0/1.5/48 | 0.93 | PF 0.92 · -19% · 1281 lệnh | PF 0.94 · -20% · 1280 lệnh | PF 0.89 · -37% · 1337 lệnh | BỎ |
| VP: lệnh chờ tại VAL/VAH | lọc 1h | 3726/3998/3837 | 1.0/1.5/48 | 0.92 | PF 0.87 · -12% · 517 lệnh | PF 0.93 · -9% · 525 lệnh | PF 0.83 · -23% · 514 lệnh | BỎ |
| VP: lệnh chờ tại VAL/VAH | lọc 4h | 4582/4796/4686 | 1.0/1.5/48 | 0.97 | PF 0.93 · -8% · 643 lệnh | PF 0.94 · -10% · 639 lệnh | PF 0.90 · -18% · 648 lệnh | BỎ |
| VP: lệnh chờ tại VAL/VAH | lọc ngày | 4618/4813/4800 | 1.0/1.5/48 | 0.96 | PF 0.86 · -17% · 646 lệnh | PF 0.96 · -8% · 642 lệnh | PF 0.92 · -15% · 706 lệnh | BỎ |
| VP: lệnh chờ tại VAL/VAH | lọc 4h + ngày | 2982/3148/2971 | 1.0/1.5/48 | 1.00 | PF 0.96 · -3% · 398 lệnh | PF 1.01 · +0% · 397 lệnh | PF 0.90 · -12% · 392 lệnh | BỎ |
| Hồi theo xu hướng 4h rồi vượt đỉnh nến trước | không lọc | 4067/3726/3727 | 3.0/1.5/48 | 0.86 | PF 0.74 · -48% · 659 lệnh | PF 0.78 · -52% · 649 lệnh | PF 0.92 · -27% · 668 lệnh | BỎ |
| Hồi theo xu hướng 4h rồi vượt đỉnh nến trước | lọc 1h | 3361/3030/3041 | 3.0/1.5/48 | 0.84 | PF 0.73 · -42% · 514 lệnh | PF 0.77 · -45% · 500 lệnh | PF 0.96 · -13% · 514 lệnh | BỎ |
| Hồi theo xu hướng 4h rồi vượt đỉnh nến trước | lọc 4h | 4067/3726/3727 | 3.0/1.5/48 | 0.86 | PF 0.74 · -48% · 659 lệnh | PF 0.78 · -52% · 649 lệnh | PF 0.92 · -27% · 668 lệnh | BỎ |
| Hồi theo xu hướng 4h rồi vượt đỉnh nến trước | lọc ngày | 2592/2417/2278 | 3.0/1.5/48 | 0.84 | PF 0.75 · -33% · 400 lệnh | PF 0.86 · -26% · 403 lệnh | PF 0.88 · -25% · 392 lệnh | BỎ |
| Hồi theo xu hướng 4h rồi vượt đỉnh nến trước | lọc 4h + ngày | 2592/2417/2278 | 3.0/1.5/48 | 0.84 | PF 0.75 · -33% · 400 lệnh | PF 0.86 · -26% · 403 lệnh | PF 0.88 · -25% · 392 lệnh | BỎ |
| VWAP phiên: xuyên -1 sd rồi đóng lại | không lọc | 14313/14294/14001 | 3.0/1.5/48 | 0.77 | PF 0.74 · -77% · 1457 lệnh | PF 0.75 · -83% · 1385 lệnh | PF 0.79 · -82% · 1419 lệnh | BỎ |
| VWAP phiên: xuyên -1 sd rồi đóng lại | lọc 1h | 6592/6713/6326 | 3.0/1.5/48 | 0.77 | PF 0.74 · -55% · 835 lệnh | PF 0.81 · -53% · 819 lệnh | PF 0.78 · -64% · 821 lệnh | BỎ |
| VWAP phiên: xuyên -1 sd rồi đóng lại | lọc 4h | 7124/7265/6882 | 3.0/1.5/48 | 0.78 | PF 0.72 · -62% · 924 lệnh | PF 0.77 · -63% · 901 lệnh | PF 0.78 · -68% · 916 lệnh | BỎ |
| VWAP phiên: xuyên -1 sd rồi đóng lại | lọc ngày | 7058/7210/6933 | 3.0/1.5/48 | 0.76 | PF 0.70 · -65% · 932 lệnh | PF 0.88 · -39% · 859 lệnh | PF 0.80 · -64% · 898 lệnh | BỎ |
| VWAP phiên: xuyên -1 sd rồi đóng lại | lọc 4h + ngày | 4488/4654/4281 | 3.0/1.5/48 | 0.78 | PF 0.71 · -47% · 546 lệnh | PF 0.86 · -30% · 528 lệnh | PF 0.78 · -49% · 527 lệnh | BỎ |
| VWAP phiên: hồi chạm VWAP theo xu hướng EMA | không lọc | 7294/7357/6941 | 3.0/1.5/48 | 0.85 | PF 0.71 · -62% · 897 lệnh | PF 0.86 · -45% · 877 lệnh | PF 0.84 · -53% · 879 lệnh | BỎ |
| VWAP phiên: hồi chạm VWAP theo xu hướng EMA | lọc 1h | 4976/5038/4940 | 3.0/1.5/48 | 0.85 | PF 0.68 · -53% · 615 lệnh | PF 0.86 · -35% · 621 lệnh | PF 0.87 · -37% · 628 lệnh | BỎ |
| VWAP phiên: hồi chạm VWAP theo xu hướng EMA | lọc 4h | 3935/4017/3880 | 3.0/1.5/48 | 0.85 | PF 0.77 · -34% · 486 lệnh | PF 0.85 · -33% · 499 lệnh | PF 0.90 · -26% · 506 lệnh | BỎ |
| VWAP phiên: hồi chạm VWAP theo xu hướng EMA | lọc ngày | 3678/3786/3541 | 3.0/1.5/48 | 0.83 | PF 0.78 · -33% · 477 lệnh | PF 0.94 · -14% · 461 lệnh | PF 0.83 · -36% · 456 lệnh | BỎ |
| VWAP phiên: hồi chạm VWAP theo xu hướng EMA | lọc 4h + ngày | 2490/2603/2433 | 3.0/1.5/48 | 0.82 | PF 0.80 · -21% · 287 lệnh | PF 0.94 · -11% · 305 lệnh | PF 0.90 · -17% · 293 lệnh | BỎ |
| Nén Bollinger 48 nến rồi bung + khối lượng | không lọc | 2746/2767/2490 | 2.0/1.5/48 | 0.80 | PF 0.62 · -41% · 458 lệnh | PF 0.76 · -34% · 466 lệnh | PF 0.75 · -38% · 427 lệnh | BỎ |
| Nén Bollinger 48 nến rồi bung + khối lượng | lọc 1h | 1493/1486/1385 | 2.0/1.5/48 | 0.78 | PF 0.59 · -26% · 243 lệnh | PF 0.65 · -30% · 260 lệnh | PF 0.59 · -38% · 242 lệnh | BỎ |
| Nén Bollinger 48 nến rồi bung + khối lượng | lọc 4h | 1480/1381/1303 | 2.0/1.5/48 | 0.77 | PF 0.65 · -23% · 252 lệnh | PF 0.77 · -18% · 234 lệnh | PF 0.71 · -27% · 233 lệnh | BỎ |
| Nén Bollinger 48 nến rồi bung + khối lượng | lọc ngày | 1374/1366/1219 | 3.0/1.5/48 | 0.75 | PF 0.67 · -23% · 225 lệnh | PF 0.90 · -9% · 224 lệnh | PF 0.69 · -30% · 217 lệnh | BỎ |
| Nén Bollinger 48 nến rồi bung + khối lượng | lọc 4h + ngày | 957/885/782 | 3.0/1.5/48 | 0.73 | PF 0.73 · -14% · 153 lệnh | PF 1.07 · +3% · 131 lệnh | PF 0.72 · -18% · 128 lệnh | BỎ |
| TTM Squeeze (Bollinger trong Keltner) bung | không lọc | 1355/1525/1330 | 2.0/1.5/48 | 0.79 | PF 0.58 · -38% · 363 lệnh | PF 0.74 · -35% · 423 lệnh | PF 0.89 · -19% · 440 lệnh | BỎ |
| TTM Squeeze (Bollinger trong Keltner) bung | lọc 1h | 679/737/633 | 2.0/1.5/48 | 0.77 | PF 0.62 · -19% · 191 lệnh | PF 0.67 · -25% · 209 lệnh | PF 0.77 · -20% · 221 lệnh | BỎ |
| TTM Squeeze (Bollinger trong Keltner) bung | lọc 4h | 679/761/674 | 2.0/1.5/48 | 0.71 | PF 0.57 · -21% · 185 lệnh | PF 0.76 · -18% · 216 lệnh | PF 0.88 · -12% · 234 lệnh | BỎ |
| TTM Squeeze (Bollinger trong Keltner) bung | lọc ngày | 676/765/637 | 3.0/1.5/16 | 0.74 | PF 0.63 · -19% · 190 lệnh | PF 0.92 · -7% · 227 lệnh | PF 0.91 · -8% · 216 lệnh | BỎ |
| TTM Squeeze (Bollinger trong Keltner) bung | lọc 4h + ngày | 436/490/402 | 2.0/1.5/48 | 0.72 | PF 0.72 · -8% · 110 lệnh | PF 0.91 · -5% · 132 lệnh | PF 0.89 · -6% · 125 lệnh | BỎ |
| VP: thoát vùng qua node thấp + khối lượng | không lọc | 1861/1902/1840 | 2.0/1.5/48 | 0.90 | PF 0.70 · -40% · 528 lệnh | PF 0.76 · -43% · 515 lệnh | PF 0.74 · -46% · 488 lệnh | BỎ |
| VP: thoát vùng qua node thấp + khối lượng | lọc 1h | 1108/1148/1119 | 2.0/1.5/48 | 0.92 | PF 0.71 · -24% · 304 lệnh | PF 0.72 · -34% · 316 lệnh | PF 0.73 · -32% · 285 lệnh | BỎ |
| VP: thoát vùng qua node thấp + khối lượng | lọc 4h | 961/987/956 | 3.0/1.5/48 | 0.96 | PF 0.87 · -12% · 261 lệnh | PF 0.82 · -22% · 252 lệnh | PF 0.90 · -14% · 241 lệnh | BỎ |
| VP: thoát vùng qua node thấp + khối lượng | lọc ngày | 947/969/911 | 3.0/1.5/48 | 0.92 | PF 0.73 · -25% · 277 lệnh | PF 0.92 · -11% · 250 lệnh | PF 0.78 · -26% · 241 lệnh | BỎ |
| VP: thoát vùng qua node thấp + khối lượng | lọc 4h + ngày | 619/645/575 | 3.0/1.5/48 | 0.96 | PF 0.76 · -16% · 174 lệnh | PF 0.82 · -15% · 164 lệnh | PF 0.79 · -17% · 140 lệnh | BỎ |
| Bung biên độ 60 phút đầu ngày UTC | không lọc | 1795/1758/1792 | 3.0/1.5/48 | 0.82 | PF 0.58 · -56% · 504 lệnh | PF 0.81 · -35% · 485 lệnh | PF 0.72 · -54% · 500 lệnh | BỎ |
| Bung biên độ 60 phút đầu ngày UTC | lọc 1h | 856/833/857 | 3.0/1.5/48 | 0.79 | PF 0.56 · -36% · 259 lệnh | PF 0.77 · -24% · 253 lệnh | PF 0.83 · -20% · 245 lệnh | BỎ |
| Bung biên độ 60 phút đầu ngày UTC | lọc 4h | 886/862/890 | 3.0/1.5/48 | 0.86 | PF 0.59 · -34% · 264 lệnh | PF 0.72 · -30% · 260 lệnh | PF 0.77 · -28% · 258 lệnh | BỎ |
| Bung biên độ 60 phút đầu ngày UTC | lọc ngày | 891/871/903 | 3.0/1.5/48 | 0.90 | PF 0.69 · -26% · 271 lệnh | PF 1.00 · -2% · 270 lệnh | PF 0.86 · -18% · 269 lệnh | BỎ |
| Bung biên độ 60 phút đầu ngày UTC | lọc 4h + ngày | 560/549/557 | 3.0/1.5/48 | 0.96 | PF 0.77 · -13% · 157 lệnh | PF 0.88 · -9% · 160 lệnh | PF 0.93 · -6% · 145 lệnh | BỎ |
| Dải EMA 8/13/21 hồi chạm EMA21 | không lọc | 5175/5103/5070 | 3.0/1.5/48 | 0.91 | PF 0.69 · -62% · 858 lệnh | PF 0.73 · -67% · 823 lệnh | PF 0.78 · -63% · 819 lệnh | BỎ |
| Dải EMA 8/13/21 hồi chạm EMA21 | lọc 1h | 2782/2725/2849 | 3.0/1.5/48 | 0.92 | PF 0.70 · -41% · 479 lệnh | PF 0.72 · -51% · 490 lệnh | PF 0.77 · -46% · 476 lệnh | BỎ |
| Dải EMA 8/13/21 hồi chạm EMA21 | lọc 4h | 2608/2632/2664 | 3.0/1.5/48 | 0.95 | PF 0.68 · -42% · 456 lệnh | PF 0.77 · -40% · 462 lệnh | PF 0.82 · -37% · 451 lệnh | BỎ |
| Dải EMA 8/13/21 hồi chạm EMA21 | lọc ngày | 2636/2569/2600 | 3.0/1.5/48 | 0.87 | PF 0.67 · -44% · 467 lệnh | PF 0.91 · -17% · 418 lệnh | PF 0.76 · -44% · 422 lệnh | BỎ |
| Dải EMA 8/13/21 hồi chạm EMA21 | lọc 4h + ngày | 1694/1684/1674 | 3.0/1.5/48 | 0.90 | PF 0.69 · -29% · 279 lệnh | PF 0.88 · -16% · 276 lệnh | PF 0.82 · -26% · 253 lệnh | BỎ |
| Stoch RSI cắt ở vùng quá mua/bán theo EMA50 | không lọc | 3510/3596/3460 | 3.0/1.5/48 | 0.83 | PF 0.76 · -48% · 695 lệnh | PF 0.78 · -52% · 668 lệnh | PF 0.88 · -38% · 696 lệnh | BỎ |
| Stoch RSI cắt ở vùng quá mua/bán theo EMA50 | lọc 1h | 2558/2631/2587 | 2.0/1.5/48 | 0.85 | PF 0.72 · -39% · 516 lệnh | PF 0.73 · -48% · 508 lệnh | PF 0.83 · -37% · 541 lệnh | BỎ |
| Stoch RSI cắt ở vùng quá mua/bán theo EMA50 | lọc 4h | 1879/1948/1910 | 3.0/1.5/48 | 0.90 | PF 0.81 · -25% · 370 lệnh | PF 0.85 · -26% · 359 lệnh | PF 0.94 · -16% · 390 lệnh | BỎ |
| Stoch RSI cắt ở vùng quá mua/bán theo EMA50 | lọc ngày | 1778/1832/1718 | 3.0/1.5/48 | 0.85 | PF 0.75 · -31% · 359 lệnh | PF 0.88 · -20% · 344 lệnh | PF 0.97 · -8% · 357 lệnh | BỎ |
| Stoch RSI cắt ở vùng quá mua/bán theo EMA50 | lọc 4h + ngày | 1185/1248/1150 | 3.0/1.5/48 | 0.89 | PF 0.82 · -16% · 217 lệnh | PF 0.95 · -7% · 222 lệnh | PF 1.04 · +3% · 231 lệnh | BỎ |
| Connors RSI(2) < 10 / > 90 theo EMA200 | không lọc | 4947/4799/4973 | 3.0/1.5/48 | 0.84 | PF 0.78 · -51% · 866 lệnh | PF 0.84 · -50% · 842 lệnh | PF 0.84 · -55% · 880 lệnh | BỎ |
| Connors RSI(2) < 10 / > 90 theo EMA200 | lọc 1h | 4595/4425/4565 | 3.0/1.5/48 | 0.84 | PF 0.76 · -50% · 777 lệnh | PF 0.83 · -48% · 772 lệnh | PF 0.87 · -46% · 801 lệnh | BỎ |
| Connors RSI(2) < 10 / > 90 theo EMA200 | lọc 4h | 3261/3077/3223 | 3.0/1.5/48 | 0.86 | PF 0.80 · -34% · 550 lệnh | PF 0.80 · -42% · 510 lệnh | PF 0.88 · -33% · 556 lệnh | BỎ |
| Connors RSI(2) < 10 / > 90 theo EMA200 | lọc ngày | 2591/2469/2561 | 3.0/1.5/48 | 0.84 | PF 0.84 · -24% · 438 lệnh | PF 0.91 · -19% · 412 lệnh | PF 0.91 · -22% · 431 lệnh | BỎ |
| Connors RSI(2) < 10 / > 90 theo EMA200 | lọc 4h + ngày | 2006/1909/1934 | 3.0/1.5/48 | 0.87 | PF 0.88 · -14% · 316 lệnh | PF 0.86 · -21% · 289 lệnh | PF 0.94 · -13% · 301 lệnh | BỎ |
| MACD histogram đổi dấu theo EMA200 | không lọc | 1725/1719/1678 | 3.0/1.5/48 | 0.81 | PF 0.52 · -56% · 457 lệnh | PF 0.71 · -44% · 441 lệnh | PF 0.67 · -55% · 447 lệnh | BỎ |
| MACD histogram đổi dấu theo EMA200 | lọc 1h | 1598/1598/1546 | 3.0/1.5/48 | 0.81 | PF 0.49 · -57% · 433 lệnh | PF 0.67 · -47% · 413 lệnh | PF 0.67 · -52% · 409 lệnh | BỎ |
| MACD histogram đổi dấu theo EMA200 | lọc 4h | 1208/1148/1120 | 3.0/1.5/48 | 0.82 | PF 0.51 · -45% · 316 lệnh | PF 0.64 · -38% · 279 lệnh | PF 0.75 · -33% · 300 lệnh | BỎ |
| MACD histogram đổi dấu theo EMA200 | lọc ngày | 885/891/889 | 3.0/1.5/48 | 0.80 | PF 0.56 · -31% · 226 lệnh | PF 0.75 · -23% · 221 lệnh | PF 0.69 · -33% · 235 lệnh | BỎ |
| MACD histogram đổi dấu theo EMA200 | lọc 4h + ngày | 729/708/686 | 3.0/1.5/48 | 0.78 | PF 0.55 · -27% · 177 lệnh | PF 0.78 · -16% · 158 lệnh | PF 0.72 · -25% · 170 lệnh | BỎ |
| Phá đỉnh/đáy 20 nến (Donchian) | không lọc | 6858/6376/7174 | 3.0/1.5/48 | 0.84 | PF 0.62 · -84% · 1224 lệnh | PF 0.69 · -83% · 1108 lệnh | PF 0.83 · -67% · 1141 lệnh | BỎ |
| Phá đỉnh/đáy 20 nến (Donchian) | lọc 1h | 3456/3209/3665 | 3.0/1.5/48 | 0.81 | PF 0.61 · -66% · 682 lệnh | PF 0.66 · -68% · 622 lệnh | PF 0.72 · -67% · 671 lệnh | BỎ |
| Phá đỉnh/đáy 20 nến (Donchian) | lọc 4h | 3555/3217/3683 | 3.0/1.5/48 | 0.83 | PF 0.60 · -67% · 685 lệnh | PF 0.68 · -64% · 606 lệnh | PF 0.79 · -55% · 644 lệnh | BỎ |
| Phá đỉnh/đáy 20 nến (Donchian) | lọc ngày | 3509/3333/3659 | 3.0/1.5/48 | 0.83 | PF 0.61 · -64% · 651 lệnh | PF 0.74 · -55% · 602 lệnh | PF 0.80 · -52% · 620 lệnh | BỎ |
| Phá đỉnh/đáy 20 nến (Donchian) | lọc 4h + ngày | 2296/2129/2261 | 3.0/1.5/48 | 0.83 | PF 0.61 · -51% · 412 lệnh | PF 0.68 · -48% · 378 lệnh | PF 0.73 · -47% · 373 lệnh | BỎ |
| Quét đỉnh/đáy phiên Á rồi quay lại | không lọc | 1230/1234/1208 | 3.0/0.5/48 | 0.66 | PF 0.59 · -36% · 349 lệnh | PF 0.74 · -31% · 350 lệnh | PF 0.79 · -27% · 364 lệnh | BỎ |
| Quét đỉnh/đáy phiên Á rồi quay lại | lọc 1h | 599/605/574 | 3.0/0.5/48 | 0.62 | PF 0.63 · -17% · 167 lệnh | PF 0.68 · -19% · 168 lệnh | PF 0.96 · -4% · 184 lệnh | BỎ |
| Quét đỉnh/đáy phiên Á rồi quay lại | lọc 4h | 612/626/594 | 3.0/0.5/48 | 0.64 | PF 0.72 · -13% · 173 lệnh | PF 0.76 · -16% · 182 lệnh | PF 0.90 · -9% · 201 lệnh | BỎ |
| Quét đỉnh/đáy phiên Á rồi quay lại | lọc ngày | 608/609/611 | 3.0/0.5/48 | 0.61 | PF 0.60 · -19% · 177 lệnh | PF 0.69 · -21% · 180 lệnh | PF 0.89 · -9% · 193 lệnh | BỎ |
| Quét đỉnh/đáy phiên Á rồi quay lại | lọc 4h + ngày | 382/400/373 | 2.0/0.5/48 | 0.59 | PF 0.67 · -9% · 99 lệnh | PF 0.61 · -15% · 114 lệnh | PF 0.71 · -12% · 112 lệnh | BỎ |
| Phá biên phiên Á giờ London | không lọc | 666/667/686 | 3.0/1.5/48 | 0.72 | PF 0.60 · -24% · 196 lệnh | PF 0.79 · -15% · 184 lệnh | PF 0.65 · -30% · 197 lệnh | BỎ |
| Phá biên phiên Á giờ London | lọc 1h | 325/317/367 | 2.0/1.5/48 | 0.70 | PF 0.60 · -11% · 97 lệnh | PF 1.00 · -0% · 90 lệnh | PF 0.76 · -11% · 111 lệnh | BỎ |
| Phá biên phiên Á giờ London | lọc 4h | 342/312/353 | 1.0/1.5/48 | 0.73 | PF 0.63 · -7% · 100 lệnh | PF 0.68 · -7% · 91 lệnh | PF 0.70 · -8% · 94 lệnh | BỎ |
| Phá biên phiên Á giờ London | lọc ngày | 339/336/355 | 1.5/1.5/48 | 0.72 | PF 0.65 · -8% · 99 lệnh | PF 0.72 · -8% · 98 lệnh | PF 0.76 · -9% · 100 lệnh | BỎ |
| Phá biên phiên Á giờ London | lọc 4h + ngày | 222/206/224 | 1.0/1.5/48 | 0.74 | PF 0.57 · -5% · 61 lệnh | PF 0.65 · -5% · 60 lệnh | PF 0.56 · -7% · 51 lệnh | BỎ |
| Quét đỉnh/đáy ngày trước rồi quay lại | không lọc | 842/831/893 | 3.0/0.5/48 | 0.80 | PF 0.79 · -17% · 250 lệnh | PF 0.78 · -23% · 242 lệnh | PF 0.72 · -29% · 252 lệnh | BỎ |
| Quét đỉnh/đáy ngày trước rồi quay lại | lọc 1h | 270/256/264 | 3.0/0.5/48 | 0.68 | PF 0.78 · -6% · 90 lệnh | PF 0.69 · -11% · 83 lệnh | PF 0.38 · -20% · 82 lệnh | BỎ |
| Quét đỉnh/đáy ngày trước rồi quay lại | lọc 4h | 394/389/421 | 3.0/0.5/48 | 0.73 | PF 0.93 · -3% · 127 lệnh | PF 0.74 · -12% · 115 lệnh | PF 0.77 · -11% · 119 lệnh | BỎ |
| Quét đỉnh/đáy ngày trước rồi quay lại | lọc ngày | 413/401/441 | 3.0/0.5/48 | 0.77 | PF 0.69 · -13% · 127 lệnh | PF 0.88 · -6% · 122 lệnh | PF 0.81 · -12% · 139 lệnh | BỎ |
| Quét đỉnh/đáy ngày trước rồi quay lại | lọc 4h + ngày | 250/255/258 | 1.5/0.5/48 | 0.68 | PF 0.69 · -6% · 79 lệnh | PF 0.57 · -12% · 76 lệnh | PF 0.72 · -8% · 73 lệnh | BỎ |
| Mùa vụ giờ: mua 22:00, bán 00:00 UTC | không lọc | 1095/1095/1095 | 1.0/0.5/8 | 0.76 | PF 0.41 · -42% · 329 lệnh | PF 0.48 · -48% · 329 lệnh | PF 0.59 · -43% · 329 lệnh | BỎ |
| Mùa vụ giờ: mua 22:00, bán 00:00 UTC | lọc 1h | 597/550/557 | 1.0/0.5/8 | 0.91 | PF 0.52 · -22% · 171 lệnh | PF 0.39 · -34% · 161 lệnh | PF 0.53 · -28% · 165 lệnh | BỎ |
| Mùa vụ giờ: mua 22:00, bán 00:00 UTC | lọc 4h | 602/565/567 | 1.0/0.5/8 | 0.87 | PF 0.46 · -21% · 162 lệnh | PF 0.53 · -26% · 173 lệnh | PF 0.63 · -21% · 158 lệnh | BỎ |
| Mùa vụ giờ: mua 22:00, bán 00:00 UTC | lọc ngày | 652/572/570 | 1.0/0.5/8 | 0.83 | PF 0.35 · -17% · 107 lệnh | PF 0.31 · -26% · 127 lệnh | PF 0.64 · -10% · 80 lệnh | BỎ |
| Mùa vụ giờ: mua 22:00, bán 00:00 UTC | lọc 4h + ngày | 427/366/357 | 1.0/0.5/8 | 0.89 | PF 0.49 · -8% · 69 lệnh | PF 0.40 · -15% · 84 lệnh | PF 1.22 · +2% · 47 lệnh | BỎ |
| Động lượng đầu ngày -> cuối ngày UTC | không lọc | 1094/1093/1083 | 1.0/0.5/8 | 0.47 | PF 0.15 · -39% · 329 lệnh | PF 0.24 · -38% · 328 lệnh | PF 0.30 · -36% · 322 lệnh | BỎ |
| Động lượng đầu ngày -> cuối ngày UTC | lọc 1h | 555/549/540 | 1.0/0.5/8 | 0.51 | PF 0.15 · -22% · 164 lệnh | PF 0.21 · -23% · 161 lệnh | PF 0.27 · -22% · 155 lệnh | BỎ |
| Động lượng đầu ngày -> cuối ngày UTC | lọc 4h | 575/596/589 | 1.0/0.5/8 | 0.51 | PF 0.19 · -21% · 164 lệnh | PF 0.23 · -24% · 167 lệnh | PF 0.29 · -24% · 171 lệnh | BỎ |
| Động lượng đầu ngày -> cuối ngày UTC | lọc ngày | 535/550/557 | 1.0/0.5/8 | 0.51 | PF 0.20 · -19% · 161 lệnh | PF 0.21 · -22% · 170 lệnh | PF 0.30 · -21% · 165 lệnh | BỎ |
| Động lượng đầu ngày -> cuối ngày UTC | lọc 4h + ngày | 355/371/364 | 1.0/0.5/8 | 0.58 | PF 0.26 · -12% · 97 lệnh | PF 0.23 · -14% · 103 lệnh | PF 0.30 · -16% · 98 lệnh | BỎ |
| Động lượng đầu phiên Mỹ -> cuối phiên | không lọc | 782/782/776 | 1.0/0.5/8 | 0.56 | PF 0.24 · -30% · 235 lệnh | PF 0.24 · -35% · 235 lệnh | PF 0.30 · -33% · 233 lệnh | BỎ |
| Động lượng đầu phiên Mỹ -> cuối phiên | lọc 1h | 427/430/410 | 1.0/0.5/8 | 0.61 | PF 0.15 · -22% · 134 lệnh | PF 0.12 · -26% · 128 lệnh | PF 0.21 · -25% · 125 lệnh | BỎ |
| Động lượng đầu phiên Mỹ -> cuối phiên | lọc 4h | 388/397/382 | 1.0/0.5/8 | 0.57 | PF 0.24 · -16% · 121 lệnh | PF 0.20 · -21% · 120 lệnh | PF 0.28 · -21% · 124 lệnh | BỎ |
| Động lượng đầu phiên Mỹ -> cuối phiên | lọc ngày | 392/391/384 | 1.0/0.5/8 | 0.50 | PF 0.20 · -19% · 119 lệnh | PF 0.20 · -22% · 112 lệnh | PF 0.27 · -20% · 114 lệnh | BỎ |
| Động lượng đầu phiên Mỹ -> cuối phiên | lọc 4h + ngày | 246/253/231 | 1.0/0.5/8 | 0.51 | PF 0.19 · -11% · 69 lệnh | PF 0.15 · -15% · 67 lệnh | PF 0.30 · -11% · 68 lệnh | BỎ |

## Chi tiết khung 30m

| Cách | Lọc | Tín hiệu BTC/ETH/SOL | TP/SL/giữ | PF trong mẫu | BTC ngoài mẫu | ETH ngoài mẫu | SOL ngoài mẫu | Kết luận |
|---|---|---|---|---|---|---|---|---|
| VP: từ chối tại VAL/VAH | không lọc | 2754/2798/2775 | 3.0/1.5/48 | 0.84 | PF 0.75 · -40% · 380 lệnh | PF 0.73 · -52% · 375 lệnh | PF 0.85 · -37% · 377 lệnh | BỎ |
| VP: từ chối tại VAL/VAH | lọc 1h | 833/915/832 | 3.0/1.0/48 | 0.83 | PF 0.79 · -12% · 151 lệnh | PF 0.56 · -28% · 136 lệnh | PF 0.79 · -17% · 136 lệnh | BỎ |
| VP: từ chối tại VAL/VAH | lọc 4h | 1251/1354/1304 | 3.0/1.5/48 | 0.82 | PF 0.88 · -12% · 195 lệnh | PF 0.65 · -37% · 188 lệnh | PF 0.80 · -24% · 176 lệnh | BỎ |
| VP: từ chối tại VAL/VAH | lọc ngày | 1406/1449/1445 | 3.0/1.0/48 | 0.81 | PF 0.95 · -6% · 240 lệnh | PF 0.81 · -22% · 237 lệnh | PF 0.70 · -35% · 236 lệnh | BỎ |
| VP: từ chối tại VAL/VAH | lọc 4h + ngày | 832/924/882 | 3.0/1.0/48 | 0.82 | PF 0.88 · -8% · 143 lệnh | PF 0.68 · -22% · 141 lệnh | PF 0.59 · -29% · 133 lệnh | BỎ |
| VP: từ chối tại VAL/VAH, chốt ở POC | không lọc | 2754/2798/2775 | 1.0/0.5/16 | 0.72 | PF 0.59 · -45% · 569 lệnh | PF 0.67 · -44% · 545 lệnh | PF 0.73 · -42% · 584 lệnh | BỎ |
| VP: từ chối tại VAL/VAH, chốt ở POC | lọc 1h | 833/915/832 | 1.0/0.5/48 | 0.72 | PF 0.49 · -21% · 178 lệnh | PF 0.52 · -23% · 166 lệnh | PF 0.76 · -13% · 160 lệnh | BỎ |
| VP: từ chối tại VAL/VAH, chốt ở POC | lọc 4h | 1251/1354/1304 | 1.0/0.5/48 | 0.75 | PF 0.71 · -17% · 249 lệnh | PF 0.50 · -35% · 252 lệnh | PF 0.72 · -22% · 264 lệnh | BỎ |
| VP: từ chối tại VAL/VAH, chốt ở POC | lọc ngày | 1406/1449/1445 | 1.0/0.5/48 | 0.70 | PF 0.73 · -18% · 290 lệnh | PF 0.74 · -22% · 280 lệnh | PF 0.81 · -18% · 303 lệnh | BỎ |
| VP: từ chối tại VAL/VAH, chốt ở POC | lọc 4h + ngày | 832/924/882 | 1.0/0.5/48 | 0.73 | PF 0.69 · -13% · 165 lệnh | PF 0.55 · -22% · 171 lệnh | PF 0.66 · -19% · 176 lệnh | BỎ |
| VP: lệnh chờ tại VAL/VAH | không lọc | 4420/4425/4489 | 1.0/1.5/16 | 0.98 | PF 0.85 · -24% · 632 lệnh | PF 0.86 · -28% · 607 lệnh | PF 0.99 · -5% · 639 lệnh | BỎ |
| VP: lệnh chờ tại VAL/VAH | lọc 1h | 1283/1369/1328 | 1.0/1.0/48 | 1.05 | PF 0.76 · -12% · 210 lệnh | PF 0.97 · -2% · 181 lệnh | PF 0.99 · -1% · 196 lệnh | BỎ |
| VP: lệnh chờ tại VAL/VAH | lọc 4h | 2025/2170/2067 | 1.0/1.5/16 | 1.02 | PF 0.83 · -14% · 306 lệnh | PF 0.94 · -7% · 293 lệnh | PF 1.04 · +3% · 291 lệnh | BỎ |
| VP: lệnh chờ tại VAL/VAH | lọc ngày | 2138/2260/2303 | 1.0/1.5/16 | 1.07 | PF 0.93 · -6% · 328 lệnh | PF 0.92 · -9% · 309 lệnh | PF 0.91 · -12% · 336 lệnh | BỎ |
| VP: lệnh chờ tại VAL/VAH | lọc 4h + ngày | 1307/1448/1359 | 1.0/1.0/16 | 1.10 | PF 0.80 · -10% · 210 lệnh | PF 0.86 · -9% · 202 lệnh | PF 0.90 · -7% · 200 lệnh | BỎ |
| Hồi theo xu hướng 4h rồi vượt đỉnh nến trước | không lọc | 2097/1974/1984 | 3.0/1.5/48 | 0.85 | PF 0.88 · -20% · 341 lệnh | PF 0.83 · -34% · 337 lệnh | PF 1.15 · +34% · 338 lệnh | BỎ |
| Hồi theo xu hướng 4h rồi vượt đỉnh nến trước | lọc 1h | 1866/1696/1715 | 3.0/1.5/48 | 0.85 | PF 0.81 · -25% · 281 lệnh | PF 0.79 · -35% · 274 lệnh | PF 1.12 · +21% · 272 lệnh | BỎ |
| Hồi theo xu hướng 4h rồi vượt đỉnh nến trước | lọc 4h | 2097/1974/1984 | 3.0/1.5/48 | 0.85 | PF 0.88 · -20% · 341 lệnh | PF 0.83 · -34% · 337 lệnh | PF 1.15 · +34% · 338 lệnh | BỎ |
| Hồi theo xu hướng 4h rồi vượt đỉnh nến trước | lọc ngày | 1312/1245/1193 | 3.0/1.5/48 | 0.84 | PF 0.94 · -8% · 214 lệnh | PF 0.84 · -22% · 210 lệnh | PF 1.06 · +6% · 201 lệnh | BỎ |
| Hồi theo xu hướng 4h rồi vượt đỉnh nến trước | lọc 4h + ngày | 1312/1245/1193 | 3.0/1.5/48 | 0.84 | PF 0.94 · -8% · 214 lệnh | PF 0.84 · -22% · 210 lệnh | PF 1.06 · +6% · 201 lệnh | BỎ |
| VWAP phiên: xuyên -1 sd rồi đóng lại | không lọc | 8876/8690/8487 | 3.0/1.5/48 | 0.81 | PF 0.79 · -59% · 776 lệnh | PF 0.89 · -47% · 756 lệnh | PF 0.86 · -58% · 755 lệnh | BỎ |
| VWAP phiên: xuyên -1 sd rồi đóng lại | lọc 1h | 4028/3978/3678 | 3.0/1.5/48 | 0.87 | PF 0.81 · -39% · 486 lệnh | PF 0.85 · -40% · 477 lệnh | PF 0.82 · -50% · 485 lệnh | BỎ |
| VWAP phiên: xuyên -1 sd rồi đóng lại | lọc 4h | 4373/4408/4156 | 3.0/1.5/48 | 0.82 | PF 0.86 · -33% · 541 lệnh | PF 0.86 · -40% · 532 lệnh | PF 0.92 · -30% · 546 lệnh | BỎ |
| VWAP phiên: xuyên -1 sd rồi đóng lại | lọc ngày | 4396/4392/4213 | 3.0/1.5/48 | 0.80 | PF 0.81 · -41% · 535 lệnh | PF 0.92 · -26% · 528 lệnh | PF 0.82 · -54% · 543 lệnh | BỎ |
| VWAP phiên: xuyên -1 sd rồi đóng lại | lọc 4h + ngày | 2778/2812/2576 | 3.0/1.5/48 | 0.79 | PF 0.86 · -23% · 325 lệnh | PF 0.91 · -19% · 327 lệnh | PF 0.87 · -30% · 314 lệnh | BỎ |
| VWAP phiên: hồi chạm VWAP theo xu hướng EMA | không lọc | 4687/4654/4471 | 3.0/1.5/48 | 0.94 | PF 0.81 · -41% · 530 lệnh | PF 0.91 · -29% · 523 lệnh | PF 0.86 · -45% · 545 lệnh | BỎ |
| VWAP phiên: hồi chạm VWAP theo xu hướng EMA | lọc 1h | 3851/3785/3761 | 3.0/1.5/48 | 0.93 | PF 0.81 · -36% · 440 lệnh | PF 0.89 · -31% · 444 lệnh | PF 0.90 · -32% · 464 lệnh | BỎ |
| VWAP phiên: hồi chạm VWAP theo xu hướng EMA | lọc 4h | 2764/2669/2686 | 3.0/1.5/48 | 0.95 | PF 0.88 · -19% · 311 lệnh | PF 0.96 · -10% · 304 lệnh | PF 0.98 · -9% · 332 lệnh | BỎ |
| VWAP phiên: hồi chạm VWAP theo xu hướng EMA | lọc ngày | 2430/2405/2277 | 3.0/1.5/48 | 0.90 | PF 0.86 · -19% · 272 lệnh | PF 1.01 · -2% · 269 lệnh | PF 0.97 · -10% · 276 lệnh | BỎ |
| VWAP phiên: hồi chạm VWAP theo xu hướng EMA | lọc 4h + ngày | 1736/1703/1650 | 3.0/1.5/48 | 0.90 | PF 0.85 · -15% · 187 lệnh | PF 1.00 · -3% · 182 lệnh | PF 1.00 · -3% · 186 lệnh | BỎ |
| Nén Bollinger 48 nến rồi bung + khối lượng | không lọc | 1389/1439/1298 | 3.0/1.5/48 | 0.92 | PF 0.77 · -22% · 229 lệnh | PF 0.99 · -3% · 227 lệnh | PF 0.86 · -21% · 225 lệnh | BỎ |
| Nén Bollinger 48 nến rồi bung + khối lượng | lọc 1h | 732/729/752 | 3.0/1.5/48 | 0.90 | PF 0.73 · -16% · 134 lệnh | PF 0.73 · -20% · 127 lệnh | PF 0.71 · -26% · 130 lệnh | BỎ |
| Nén Bollinger 48 nến rồi bung + khối lượng | lọc 4h | 714/668/672 | 3.0/1.5/48 | 0.86 | PF 0.72 · -15% · 125 lệnh | PF 0.79 · -14% · 113 lệnh | PF 0.76 · -20% · 117 lệnh | BỎ |
| Nén Bollinger 48 nến rồi bung + khối lượng | lọc ngày | 703/731/627 | 3.0/1.5/48 | 0.88 | PF 0.71 · -17% · 125 lệnh | PF 0.78 · -16% · 121 lệnh | PF 0.91 · -8% · 114 lệnh | BỎ |
| Nén Bollinger 48 nến rồi bung + khối lượng | lọc 4h + ngày | 447/419/395 | 3.0/1.5/48 | 0.84 | PF 0.69 · -12% · 76 lệnh | PF 0.62 · -15% · 65 lệnh | PF 0.88 · -6% · 65 lệnh | BỎ |
| TTM Squeeze (Bollinger trong Keltner) bung | không lọc | 759/795/680 | 1.5/1.5/16 | 0.89 | PF 0.65 · -23% · 221 lệnh | PF 0.91 · -10% · 261 lệnh | PF 0.68 · -35% · 249 lệnh | BỎ |
| TTM Squeeze (Bollinger trong Keltner) bung | lọc 1h | 366/358/321 | 1.5/1.5/48 | 0.90 | PF 0.51 · -19% · 108 lệnh | PF 0.94 · -3% · 112 lệnh | PF 0.68 · -20% · 120 lệnh | BỎ |
| TTM Squeeze (Bollinger trong Keltner) bung | lọc 4h | 394/372/332 | 1.5/1.5/8 | 0.90 | PF 0.55 · -16% · 119 lệnh | PF 1.07 · +3% · 128 lệnh | PF 0.63 · -21% · 127 lệnh | BỎ |
| TTM Squeeze (Bollinger trong Keltner) bung | lọc ngày | 384/415/327 | 1.5/1.5/8 | 0.88 | PF 0.60 · -12% · 107 lệnh | PF 1.10 · +4% · 137 lệnh | PF 0.60 · -22% · 117 lệnh | BỎ |
| TTM Squeeze (Bollinger trong Keltner) bung | lọc 4h + ngày | 247/250/208 | 1.5/1.5/8 | 0.88 | PF 0.55 · -9% · 64 lệnh | PF 1.05 · +1% · 83 lệnh | PF 0.53 · -17% · 69 lệnh | BỎ |
| VP: thoát vùng qua node thấp + khối lượng | không lọc | 985/965/949 | 3.0/1.5/16 | 0.96 | PF 0.86 · -15% · 257 lệnh | PF 0.84 · -25% · 267 lệnh | PF 0.91 · -17% · 268 lệnh | BỎ |
| VP: thoát vùng qua node thấp + khối lượng | lọc 1h | 646/658/675 | 3.0/1.5/48 | 0.96 | PF 1.12 · +7% · 146 lệnh | PF 0.74 · -29% · 173 lệnh | PF 0.91 · -14% · 182 lệnh | BỎ |
| VP: thoát vùng qua node thấp + khối lượng | lọc 4h | 541/522/537 | 3.0/1.5/48 | 1.02 | PF 1.07 · +3% · 127 lệnh | PF 0.89 · -11% · 136 lệnh | PF 1.05 · +3% · 147 lệnh | BỎ |
| VP: thoát vùng qua node thấp + khối lượng | lọc ngày | 501/510/468 | 3.0/1.5/16 | 1.01 | PF 0.84 · -9% · 130 lệnh | PF 0.87 · -12% · 134 lệnh | PF 0.98 · -3% · 137 lệnh | BỎ |
| VP: thoát vùng qua node thấp + khối lượng | lọc 4h + ngày | 347/350/325 | 3.0/1.5/48 | 1.02 | PF 0.88 · -5% · 82 lệnh | PF 0.86 · -10% · 87 lệnh | PF 1.08 · +4% · 86 lệnh | BỎ |
| Bung biên độ 60 phút đầu ngày UTC | không lọc | 1752/1709/1767 | 3.0/1.0/48 | 0.84 | PF 0.62 · -53% · 463 lệnh | PF 0.86 · -29% · 456 lệnh | PF 0.61 · -69% · 473 lệnh | BỎ |
| Bung biên độ 60 phút đầu ngày UTC | lọc 1h | 831/808/839 | 3.0/1.5/16 | 0.85 | PF 0.61 · -37% · 251 lệnh | PF 0.76 · -29% · 242 lệnh | PF 0.78 · -29% · 240 lệnh | BỎ |
| Bung biên độ 60 phút đầu ngày UTC | lọc 4h | 867/839/881 | 3.0/1.5/16 | 0.91 | PF 0.65 · -34% · 257 lệnh | PF 0.78 · -27% · 249 lệnh | PF 0.74 · -36% · 255 lệnh | BỎ |
| Bung biên độ 60 phút đầu ngày UTC | lọc ngày | 869/850/887 | 3.0/1.0/16 | 0.95 | PF 0.69 · -27% · 265 lệnh | PF 0.97 · -5% · 259 lệnh | PF 0.69 · -37% · 263 lệnh | BỎ |
| Bung biên độ 60 phút đầu ngày UTC | lọc 4h + ngày | 551/535/550 | 3.0/1.0/16 | 1.04 | PF 0.70 · -17% · 156 lệnh | PF 0.88 · -9% · 153 lệnh | PF 0.73 · -21% · 143 lệnh | BỎ |
| Dải EMA 8/13/21 hồi chạm EMA21 | không lọc | 2576/2351/2483 | 3.0/1.5/48 | 0.93 | PF 0.89 · -22% · 419 lệnh | PF 0.98 · -8% · 377 lệnh | PF 1.01 · -2% · 380 lệnh | BỎ |
| Dải EMA 8/13/21 hồi chạm EMA21 | lọc 1h | 1527/1395/1578 | 2.0/1.5/48 | 0.93 | PF 0.92 · -10% · 282 lệnh | PF 0.94 · -10% · 266 lệnh | PF 1.03 · +3% · 271 lệnh | BỎ |
| Dải EMA 8/13/21 hồi chạm EMA21 | lọc 4h | 1354/1170/1356 | 3.0/1.5/48 | 0.94 | PF 0.93 · -8% · 227 lệnh | PF 1.15 · +16% · 203 lệnh | PF 1.29 · +41% · 202 lệnh | THEO DÕI |
| Dải EMA 8/13/21 hồi chạm EMA21 | lọc ngày | 1316/1221/1220 | 3.0/1.5/48 | 0.97 | PF 0.91 · -10% · 228 lệnh | PF 1.10 · +11% · 213 lệnh | PF 1.10 · +11% · 202 lệnh | BỎ |
| Dải EMA 8/13/21 hồi chạm EMA21 | lọc 4h + ngày | 879/763/825 | 3.0/1.5/48 | 0.95 | PF 0.96 · -4% · 142 lệnh | PF 1.19 · +14% · 129 lệnh | PF 1.23 · +19% · 117 lệnh | THEO DÕI |
| Stoch RSI cắt ở vùng quá mua/bán theo EMA50 | không lọc | 1770/1808/1794 | 3.0/1.5/48 | 0.83 | PF 0.90 · -17% · 322 lệnh | PF 0.90 · -22% · 343 lệnh | PF 0.90 · -27% · 344 lệnh | BỎ |
| Stoch RSI cắt ở vùng quá mua/bán theo EMA50 | lọc 1h | 1565/1601/1605 | 2.0/1.5/48 | 0.83 | PF 0.92 · -11% · 304 lệnh | PF 0.86 · -26% · 331 lệnh | PF 0.90 · -21% · 320 lệnh | BỎ |
| Stoch RSI cắt ở vùng quá mua/bán theo EMA50 | lọc 4h | 1067/1102/1086 | 2.0/1.5/48 | 0.84 | PF 0.98 · -3% · 207 lệnh | PF 0.86 · -19% · 223 lệnh | PF 0.88 · -19% · 216 lệnh | BỎ |
| Stoch RSI cắt ở vùng quá mua/bán theo EMA50 | lọc ngày | 905/935/892 | 3.0/1.5/48 | 0.83 | PF 0.95 · -5% · 157 lệnh | PF 0.97 · -6% · 178 lệnh | PF 0.98 · -5% · 177 lệnh | BỎ |
| Stoch RSI cắt ở vùng quá mua/bán theo EMA50 | lọc 4h + ngày | 649/689/659 | 3.0/1.5/48 | 0.80 | PF 1.05 · +2% · 107 lệnh | PF 1.09 · +6% · 124 lệnh | PF 0.94 · -8% · 126 lệnh | BỎ |
| Connors RSI(2) < 10 / > 90 theo EMA200 | không lọc | 2485/2443/2479 | 3.0/1.5/48 | 0.85 | PF 0.90 · -22% · 437 lệnh | PF 0.91 · -26% · 422 lệnh | PF 0.84 · -45% · 454 lệnh | BỎ |
| Connors RSI(2) < 10 / > 90 theo EMA200 | lọc 1h | 2406/2360/2410 | 3.0/1.5/48 | 0.84 | PF 0.91 · -19% · 417 lệnh | PF 0.90 · -27% · 406 lệnh | PF 0.83 · -47% · 439 lệnh | BỎ |
| Connors RSI(2) < 10 / > 90 theo EMA200 | lọc 4h | 1948/1874/1901 | 3.0/1.5/48 | 0.85 | PF 0.84 · -25% · 329 lệnh | PF 0.89 · -25% · 324 lệnh | PF 0.89 · -28% · 346 lệnh | BỎ |
| Connors RSI(2) < 10 / > 90 theo EMA200 | lọc ngày | 1341/1350/1345 | 3.0/1.5/48 | 0.83 | PF 0.78 · -24% · 219 lệnh | PF 1.13 · +17% · 217 lệnh | PF 0.89 · -21% · 235 lệnh | BỎ |
| Connors RSI(2) < 10 / > 90 theo EMA200 | lọc 4h + ngày | 1180/1172/1147 | 3.0/1.5/48 | 0.82 | PF 0.81 · -18% · 182 lệnh | PF 1.07 · +7% · 185 lệnh | PF 0.97 · -7% · 188 lệnh | BỎ |
| MACD histogram đổi dấu theo EMA200 | không lọc | 836/858/771 | 2.0/1.5/48 | 0.96 | PF 0.64 · -32% · 237 lệnh | PF 0.67 · -35% · 228 lệnh | PF 0.76 · -29% · 214 lệnh | BỎ |
| MACD histogram đổi dấu theo EMA200 | lọc 1h | 694/695/641 | 3.0/1.5/48 | 0.99 | PF 0.55 · -36% · 190 lệnh | PF 0.69 · -30% · 181 lệnh | PF 0.66 · -36% · 173 lệnh | BỎ |
| MACD histogram đổi dấu theo EMA200 | lọc 4h | 715/699/615 | 2.0/1.5/48 | 0.99 | PF 0.66 · -26% · 197 lệnh | PF 0.72 · -25% · 186 lệnh | PF 0.84 · -16% · 164 lệnh | BỎ |
| MACD histogram đổi dấu theo EMA200 | lọc ngày | 470/489/444 | 2.0/1.5/48 | 1.02 | PF 0.75 · -12% · 119 lệnh | PF 0.69 · -20% · 122 lệnh | PF 0.83 · -12% · 113 lệnh | BỎ |
| MACD histogram đổi dấu theo EMA200 | lọc 4h + ngày | 437/440/384 | 2.0/1.5/48 | 1.04 | PF 0.72 · -13% · 109 lệnh | PF 0.74 · -15% · 109 lệnh | PF 0.86 · -9% · 92 lệnh | BỎ |
| Phá đỉnh/đáy 20 nến (Donchian) | không lọc | 3305/3105/3511 | 3.0/1.5/48 | 0.89 | PF 0.90 · -26% · 568 lệnh | PF 0.88 · -36% · 508 lệnh | PF 0.91 · -37% · 565 lệnh | BỎ |
| Phá đỉnh/đáy 20 nến (Donchian) | lọc 1h | 1790/1666/1937 | 3.0/1.5/48 | 0.91 | PF 0.86 · -23% · 345 lệnh | PF 0.82 · -33% · 299 lệnh | PF 0.93 · -20% · 344 lệnh | BỎ |
| Phá đỉnh/đáy 20 nến (Donchian) | lọc 4h | 1757/1596/1864 | 3.0/1.5/48 | 0.95 | PF 0.83 · -27% · 329 lệnh | PF 0.88 · -23% · 281 lệnh | PF 0.91 · -23% · 325 lệnh | BỎ |
| Phá đỉnh/đáy 20 nến (Donchian) | lọc ngày | 1716/1636/1822 | 3.0/1.5/48 | 0.92 | PF 0.82 · -27% · 322 lệnh | PF 0.89 · -21% · 283 lệnh | PF 0.95 · -14% · 302 lệnh | BỎ |
| Phá đỉnh/đáy 20 nến (Donchian) | lọc 4h + ngày | 1129/1043/1168 | 3.0/1.5/48 | 0.95 | PF 0.75 · -27% · 210 lệnh | PF 0.77 · -28% · 176 lệnh | PF 0.93 · -13% · 182 lệnh | BỎ |
| Quét đỉnh/đáy phiên Á rồi quay lại | không lọc | 1190/1186/1160 | 3.0/0.5/48 | 0.72 | PF 0.63 · -38% · 306 lệnh | PF 0.75 · -33% · 305 lệnh | PF 0.86 · -21% · 320 lệnh | BỎ |
| Quét đỉnh/đáy phiên Á rồi quay lại | lọc 1h | 577/572/550 | 3.0/0.5/48 | 0.72 | PF 0.60 · -22% · 157 lệnh | PF 0.72 · -20% · 154 lệnh | PF 0.97 · -4% · 172 lệnh | BỎ |
| Quét đỉnh/đáy phiên Á rồi quay lại | lọc 4h | 598/607/574 | 3.0/0.5/48 | 0.73 | PF 0.62 · -24% · 169 lệnh | PF 0.72 · -23% · 174 lệnh | PF 0.96 · -5% · 189 lệnh | BỎ |
| Quét đỉnh/đáy phiên Á rồi quay lại | lọc ngày | 588/582/589 | 3.0/0.5/48 | 0.68 | PF 0.70 · -18% · 168 lệnh | PF 0.71 · -23% · 166 lệnh | PF 0.83 · -16% · 184 lệnh | BỎ |
| Quét đỉnh/đáy phiên Á rồi quay lại | lọc 4h + ngày | 375/388/365 | 3.0/0.5/48 | 0.70 | PF 0.75 · -10% · 98 lệnh | PF 0.66 · -18% · 108 lệnh | PF 0.96 · -3% · 108 lệnh | BỎ |
| Phá biên phiên Á giờ London | không lọc | 628/616/649 | 3.0/1.5/48 | 0.77 | PF 0.82 · -14% · 183 lệnh | PF 0.88 · -12% · 171 lệnh | PF 0.84 · -20% · 181 lệnh | BỎ |
| Phá biên phiên Á giờ London | lọc 1h | 301/289/350 | 2.0/1.5/48 | 0.76 | PF 0.87 · -5% · 91 lệnh | PF 1.07 · +2% · 86 lệnh | PF 0.85 · -9% · 103 lệnh | BỎ |
| Phá biên phiên Á giờ London | lọc 4h | 329/285/334 | 2.0/1.5/48 | 0.79 | PF 0.82 · -7% · 99 lệnh | PF 1.04 · +1% · 85 lệnh | PF 1.09 · +3% · 88 lệnh | BỎ |
| Phá biên phiên Á giờ London | lọc ngày | 321/305/331 | 3.0/1.5/48 | 0.82 | PF 0.82 · -8% · 93 lệnh | PF 0.98 · -2% · 89 lệnh | PF 1.04 · +1% · 92 lệnh | BỎ |
| Phá biên phiên Á giờ London | lọc 4h + ngày | 215/185/210 | 2.0/1.5/48 | 0.77 | PF 0.81 · -5% · 60 lệnh | PF 1.28 · +6% · 54 lệnh | PF 1.23 · +5% · 48 lệnh | THEO DÕI |
| Quét đỉnh/đáy ngày trước rồi quay lại | không lọc | 810/807/861 | 3.0/0.5/48 | 0.92 | PF 0.75 · -24% · 236 lệnh | PF 0.90 · -14% · 229 lệnh | PF 0.67 · -41% · 240 lệnh | BỎ |
| Quét đỉnh/đáy ngày trước rồi quay lại | lọc 1h | 251/240/242 | 3.0/0.5/48 | 0.84 | PF 0.68 · -10% · 82 lệnh | PF 0.89 · -4% · 75 lệnh | PF 0.41 · -24% · 74 lệnh | BỎ |
| Quét đỉnh/đáy ngày trước rồi quay lại | lọc 4h | 383/377/404 | 3.0/0.5/48 | 0.88 | PF 0.89 · -6% · 123 lệnh | PF 0.78 · -12% · 112 lệnh | PF 0.59 · -25% · 114 lệnh | BỎ |
| Quét đỉnh/đáy ngày trước rồi quay lại | lọc ngày | 399/392/424 | 3.0/0.5/48 | 0.92 | PF 0.75 · -12% · 120 lệnh | PF 1.08 · +4% · 119 lệnh | PF 0.77 · -17% · 134 lệnh | BỎ |
| Quét đỉnh/đáy ngày trước rồi quay lại | lọc 4h + ngày | 243/249/245 | 3.0/0.5/48 | 0.86 | PF 0.79 · -6% · 76 lệnh | PF 0.88 · -4% · 73 lệnh | PF 0.74 · -12% · 70 lệnh | BỎ |
| Mùa vụ giờ: mua 22:00, bán 00:00 UTC | không lọc | 1095/1095/1095 | 1.0/0.5/8 | 0.76 | PF 0.41 · -42% · 329 lệnh | PF 0.48 · -48% · 329 lệnh | PF 0.59 · -43% · 329 lệnh | BỎ |
| Mùa vụ giờ: mua 22:00, bán 00:00 UTC | lọc 1h | 597/550/557 | 1.0/0.5/8 | 0.91 | PF 0.52 · -22% · 171 lệnh | PF 0.39 · -34% · 161 lệnh | PF 0.53 · -28% · 165 lệnh | BỎ |
| Mùa vụ giờ: mua 22:00, bán 00:00 UTC | lọc 4h | 602/565/567 | 1.0/0.5/8 | 0.87 | PF 0.46 · -21% · 162 lệnh | PF 0.53 · -26% · 173 lệnh | PF 0.63 · -21% · 158 lệnh | BỎ |
| Mùa vụ giờ: mua 22:00, bán 00:00 UTC | lọc ngày | 652/572/570 | 1.0/0.5/8 | 0.83 | PF 0.35 · -17% · 107 lệnh | PF 0.31 · -26% · 127 lệnh | PF 0.64 · -10% · 80 lệnh | BỎ |
| Mùa vụ giờ: mua 22:00, bán 00:00 UTC | lọc 4h + ngày | 427/366/357 | 1.0/0.5/8 | 0.89 | PF 0.49 · -8% · 69 lệnh | PF 0.40 · -15% · 84 lệnh | PF 1.22 · +2% · 47 lệnh | BỎ |
| Động lượng đầu ngày -> cuối ngày UTC | không lọc | 1094/1093/1083 | 1.0/0.5/8 | 0.47 | PF 0.15 · -39% · 329 lệnh | PF 0.24 · -38% · 328 lệnh | PF 0.30 · -36% · 322 lệnh | BỎ |
| Động lượng đầu ngày -> cuối ngày UTC | lọc 1h | 555/549/540 | 1.0/0.5/8 | 0.51 | PF 0.15 · -22% · 164 lệnh | PF 0.21 · -23% · 161 lệnh | PF 0.27 · -22% · 155 lệnh | BỎ |
| Động lượng đầu ngày -> cuối ngày UTC | lọc 4h | 575/596/589 | 1.0/0.5/8 | 0.51 | PF 0.19 · -21% · 164 lệnh | PF 0.23 · -24% · 167 lệnh | PF 0.29 · -24% · 171 lệnh | BỎ |
| Động lượng đầu ngày -> cuối ngày UTC | lọc ngày | 535/550/557 | 1.0/0.5/8 | 0.51 | PF 0.20 · -19% · 161 lệnh | PF 0.21 · -22% · 170 lệnh | PF 0.30 · -21% · 165 lệnh | BỎ |
| Động lượng đầu ngày -> cuối ngày UTC | lọc 4h + ngày | 355/371/364 | 1.0/0.5/8 | 0.58 | PF 0.26 · -12% · 97 lệnh | PF 0.23 · -14% · 103 lệnh | PF 0.30 · -16% · 98 lệnh | BỎ |
| Động lượng đầu phiên Mỹ -> cuối phiên | không lọc | 782/782/776 | 1.0/0.5/8 | 0.56 | PF 0.24 · -30% · 235 lệnh | PF 0.24 · -35% · 235 lệnh | PF 0.30 · -33% · 233 lệnh | BỎ |
| Động lượng đầu phiên Mỹ -> cuối phiên | lọc 1h | 427/430/410 | 1.0/0.5/8 | 0.61 | PF 0.15 · -22% · 134 lệnh | PF 0.12 · -26% · 128 lệnh | PF 0.21 · -25% · 125 lệnh | BỎ |
| Động lượng đầu phiên Mỹ -> cuối phiên | lọc 4h | 388/397/382 | 1.0/0.5/8 | 0.57 | PF 0.24 · -16% · 121 lệnh | PF 0.20 · -21% · 120 lệnh | PF 0.28 · -21% · 124 lệnh | BỎ |
| Động lượng đầu phiên Mỹ -> cuối phiên | lọc ngày | 392/391/384 | 1.0/0.5/8 | 0.50 | PF 0.20 · -19% · 119 lệnh | PF 0.20 · -22% · 112 lệnh | PF 0.27 · -20% · 114 lệnh | BỎ |
| Động lượng đầu phiên Mỹ -> cuối phiên | lọc 4h + ngày | 246/253/231 | 1.0/0.5/8 | 0.51 | PF 0.19 · -11% · 69 lệnh | PF 0.15 · -15% · 67 lệnh | PF 0.30 · -11% · 68 lệnh | BỎ |

## Chi tiết khung 1h

| Cách | Lọc | Tín hiệu BTC/ETH/SOL | TP/SL/giữ | PF trong mẫu | BTC ngoài mẫu | ETH ngoài mẫu | SOL ngoài mẫu | Kết luận |
|---|---|---|---|---|---|---|---|---|
| VP: từ chối tại VAL/VAH | không lọc | 1023/1023/1021 | 3.0/1.5/48 | 1.03 | PF 1.21 · +19% · 148 lệnh | PF 1.06 · +5% · 143 lệnh | PF 1.09 · +10% · 151 lệnh | THEO DÕI |
| VP: từ chối tại VAL/VAH | lọc 4h | 348/354/307 | 3.0/1.5/16 | 1.01 | PF 1.00 · -0% · 55 lệnh | PF 0.72 · -10% · 55 lệnh | PF 0.72 · -12% · 54 lệnh | BỎ |
| VP: từ chối tại VAL/VAH | lọc ngày | 545/494/466 | 3.0/1.0/48 | 1.03 | PF 1.27 · +11% · 91 lệnh | PF 1.08 · +3% · 86 lệnh | PF 1.00 · -1% · 81 lệnh | THEO DÕI |
| VP: từ chối tại VAL/VAH | lọc 4h + ngày | 252/240/209 | 3.0/1.5/16 | 1.07 | PF 0.97 · -1% · 37 lệnh | PF 0.70 · -7% · 38 lệnh | PF 0.74 · -8% · 35 lệnh | BỎ |
| VP: từ chối tại VAL/VAH, chốt ở POC | không lọc | 1023/1023/1021 | 1.0/0.5/48 | 0.89 | PF 1.22 · +14% · 201 lệnh | PF 0.73 · -22% · 186 lệnh | PF 1.05 · +4% · 225 lệnh | BỎ |
| VP: từ chối tại VAL/VAH, chốt ở POC | lọc 4h | 348/354/307 | 1.0/0.5/16 | 0.84 | PF 0.76 · -5% · 67 lệnh | PF 0.71 · -8% · 63 lệnh | PF 0.72 · -8% · 73 lệnh | BỎ |
| VP: từ chối tại VAL/VAH, chốt ở POC | lọc ngày | 545/494/466 | 1.0/0.5/48 | 0.98 | PF 0.99 · -1% · 106 lệnh | PF 0.59 · -19% · 103 lệnh | PF 0.87 · -6% · 102 lệnh | BỎ |
| VP: từ chối tại VAL/VAH, chốt ở POC | lọc 4h + ngày | 252/240/209 | 1.0/0.5/16 | 0.89 | PF 0.80 · -3% · 44 lệnh | PF 0.66 · -6% · 45 lệnh | PF 0.71 · -6% · 43 lệnh | BỎ |
| VP: lệnh chờ tại VAL/VAH | không lọc | 1629/1585/1660 | 1.0/1.5/8 | 1.20 | PF 1.06 · +4% · 247 lệnh | PF 1.32 · +29% · 214 lệnh | PF 1.37 · +45% · 250 lệnh | GIỮ |
| VP: lệnh chờ tại VAL/VAH | lọc 4h | 534/551/524 | 1.0/1.5/8 | 1.18 | PF 0.93 · -2% · 74 lệnh | PF 1.34 · +9% · 73 lệnh | PF 1.32 · +10% · 77 lệnh | THEO DÕI |
| VP: lệnh chờ tại VAL/VAH | lọc ngày | 818/803/787 | 1.0/1.5/8 | 1.10 | PF 1.17 · +6% · 122 lệnh | PF 0.90 · -6% · 127 lệnh | PF 1.26 · +13% · 117 lệnh | THEO DÕI |
| VP: lệnh chờ tại VAL/VAH | lọc 4h + ngày | 391/383/361 | 1.0/1.5/8 | 1.20 | PF 0.87 · -2% · 47 lệnh | PF 1.42 · +8% · 55 lệnh | PF 1.32 · +6% · 48 lệnh | THEO DÕI |
| Hồi theo xu hướng 4h rồi vượt đỉnh nến trước | không lọc | 1203/1138/1052 | 3.0/1.0/16 | 0.96 | PF 0.54 · -48% · 252 lệnh | PF 0.77 · -32% · 245 lệnh | PF 0.81 · -30% · 231 lệnh | BỎ |
| Hồi theo xu hướng 4h rồi vượt đỉnh nến trước | lọc 4h | 1203/1138/1052 | 3.0/1.0/16 | 0.96 | PF 0.54 · -48% · 252 lệnh | PF 0.77 · -32% · 245 lệnh | PF 0.81 · -30% · 231 lệnh | BỎ |
| Hồi theo xu hướng 4h rồi vượt đỉnh nến trước | lọc ngày | 764/708/655 | 3.0/1.0/16 | 1.00 | PF 0.52 · -33% · 146 lệnh | PF 0.76 · -22% · 146 lệnh | PF 0.82 · -18% · 136 lệnh | BỎ |
| Hồi theo xu hướng 4h rồi vượt đỉnh nến trước | lọc 4h + ngày | 764/708/655 | 3.0/1.0/16 | 1.00 | PF 0.52 · -33% · 146 lệnh | PF 0.76 · -22% · 146 lệnh | PF 0.82 · -18% · 136 lệnh | BỎ |
| VWAP phiên: xuyên -1 sd rồi đóng lại | không lọc | 4997/4883/4687 | 3.0/1.0/48 | 0.84 | PF 0.80 · -46% · 528 lệnh | PF 0.93 · -27% · 516 lệnh | PF 0.87 · -44% · 493 lệnh | BỎ |
| VWAP phiên: xuyên -1 sd rồi đóng lại | lọc 4h | 2441/2421/2331 | 3.0/1.5/16 | 0.85 | PF 0.76 · -43% · 375 lệnh | PF 0.86 · -35% · 375 lệnh | PF 1.04 · +4% · 353 lệnh | BỎ |
| VWAP phiên: xuyên -1 sd rồi đóng lại | lọc ngày | 2468/2450/2353 | 3.0/1.5/48 | 0.88 | PF 0.85 · -31% · 313 lệnh | PF 0.98 · -10% · 298 lệnh | PF 0.95 · -20% · 307 lệnh | BỎ |
| VWAP phiên: xuyên -1 sd rồi đóng lại | lọc 4h + ngày | 1552/1556/1438 | 3.0/1.5/16 | 0.85 | PF 0.78 · -27% · 221 lệnh | PF 0.85 · -25% · 222 lệnh | PF 0.95 · -12% · 205 lệnh | BỎ |
| VWAP phiên: hồi chạm VWAP theo xu hướng EMA | không lọc | 2976/2896/2782 | 3.0/1.0/48 | 0.93 | PF 0.80 · -37% · 394 lệnh | PF 0.84 · -42% · 420 lệnh | PF 1.07 · +15% · 400 lệnh | BỎ |
| VWAP phiên: hồi chạm VWAP theo xu hướng EMA | lọc 4h | 2087/1955/1881 | 3.0/1.0/48 | 0.96 | PF 0.89 · -17% · 267 lệnh | PF 0.92 · -20% · 290 lệnh | PF 1.20 · +43% · 272 lệnh | BỎ |
| VWAP phiên: hồi chạm VWAP theo xu hướng EMA | lọc ngày | 1591/1554/1451 | 3.0/1.0/48 | 0.94 | PF 0.89 · -13% · 185 lệnh | PF 1.00 · -3% · 209 lệnh | PF 1.18 · +26% · 197 lệnh | BỎ |
| VWAP phiên: hồi chạm VWAP theo xu hướng EMA | lọc 4h + ngày | 1302/1239/1142 | 3.0/1.0/48 | 0.93 | PF 0.96 · -5% · 142 lệnh | PF 1.03 · +1% · 164 lệnh | PF 1.19 · +22% · 148 lệnh | THEO DÕI |
| Nén Bollinger 48 nến rồi bung + khối lượng | không lọc | 721/642/617 | 3.0/1.5/48 | 1.08 | PF 0.96 · -3% · 113 lệnh | PF 1.07 · +4% · 111 lệnh | PF 1.33 · +30% · 105 lệnh | THEO DÕI |
| Nén Bollinger 48 nến rồi bung + khối lượng | lọc 4h | 378/337/351 | 3.0/1.5/8 | 0.99 | PF 1.00 · -0% · 71 lệnh | PF 1.37 · +14% · 65 lệnh | PF 1.96 · +33% · 64 lệnh | THEO DÕI |
| Nén Bollinger 48 nến rồi bung + khối lượng | lọc ngày | 354/331/293 | 3.0/1.5/8 | 1.01 | PF 1.15 · +4% · 68 lệnh | PF 1.42 · +15% · 65 lệnh | PF 1.33 · +12% · 56 lệnh | THEO DÕI |
| Nén Bollinger 48 nến rồi bung + khối lượng | lọc 4h + ngày | 229/207/194 | 3.0/1.5/8 | 1.00 | PF 1.14 · +2% · 41 lệnh | PF 1.80 · +16% · 36 lệnh | PF 1.48 · +11% · 34 lệnh | THEO DÕI |
| TTM Squeeze (Bollinger trong Keltner) bung | không lọc | 372/386/331 | 2.0/1.5/8 | 1.09 | PF 1.06 · +2% · 113 lệnh | PF 1.32 · +21% · 132 lệnh | PF 0.98 · -2% · 106 lệnh | THEO DÕI |
| TTM Squeeze (Bollinger trong Keltner) bung | lọc 4h | 179/182/161 | 2.0/1.5/8 | 1.18 | PF 1.03 · +0% · 58 lệnh | PF 1.67 · +19% · 58 lệnh | PF 0.97 · -2% · 59 lệnh | THEO DÕI |
| TTM Squeeze (Bollinger trong Keltner) bung | lọc ngày | 171/192/154 | 1.0/1.5/8 | 1.27 | PF 1.22 · +3% · 56 lệnh | PF 1.58 · +12% · 62 lệnh | PF 1.02 · +0% · 49 lệnh | GIỮ |
| TTM Squeeze (Bollinger trong Keltner) bung | lọc 4h + ngày | 111/123/98 | 2.0/1.5/8 | 1.31 | PF 0.98 · -1% · 37 lệnh | PF 1.64 · +12% · 38 lệnh | PF 1.12 · +2% · 33 lệnh | THEO DÕI |
| VP: thoát vùng qua node thấp + khối lượng | không lọc | 321/292/284 | 3.0/1.5/48 | 1.08 | PF 0.91 · -6% · 77 lệnh | PF 1.20 · +12% · 82 lệnh | PF 1.29 · +18% · 74 lệnh | THEO DÕI |
| VP: thoát vùng qua node thấp + khối lượng | lọc 4h | 221/181/189 | 3.0/1.5/16 | 1.04 | PF 1.14 · +4% · 54 lệnh | PF 1.26 · +10% · 56 lệnh | PF 1.60 · +23% · 54 lệnh | THEO DÕI |
| VP: thoát vùng qua node thấp + khối lượng | lọc ngày | 164/151/149 | 3.0/1.5/48 | 1.17 | PF 0.76 · -8% · 38 lệnh | PF 1.14 · +4% · 41 lệnh | PF 1.41 · +13% · 36 lệnh | THEO DÕI |
| VP: thoát vùng qua node thấp + khối lượng | lọc 4h + ngày | 144/115/110 | 3.0/1.5/48 | 1.08 | PF 0.90 · -3% · 33 lệnh | PF 0.97 · -2% · 33 lệnh | PF 1.35 · +8% · 24 lệnh | BỎ |
| Bung biên độ 60 phút đầu ngày UTC | không lọc | 1672/1644/1696 | 2.0/1.5/16 | 0.83 | PF 0.84 · -29% · 363 lệnh | PF 0.89 · -28% · 363 lệnh | PF 0.74 · -59% · 365 lệnh | BỎ |
| Bung biên độ 60 phút đầu ngày UTC | lọc 4h | 823/799/858 | 3.0/1.5/16 | 0.93 | PF 0.76 · -31% · 233 lệnh | PF 0.77 · -35% · 223 lệnh | PF 0.91 · -20% · 238 lệnh | BỎ |
| Bung biên độ 60 phút đầu ngày UTC | lọc ngày | 828/817/850 | 2.0/1.5/48 | 0.98 | PF 0.83 · -23% · 227 lệnh | PF 1.03 · +3% · 223 lệnh | PF 0.80 · -39% · 230 lệnh | BỎ |
| Bung biên độ 60 phút đầu ngày UTC | lọc 4h + ngày | 525/511/534 | 3.0/1.5/16 | 1.01 | PF 0.87 · -13% · 143 lệnh | PF 0.98 · -5% · 134 lệnh | PF 0.96 · -7% · 129 lệnh | BỎ |
| Dải EMA 8/13/21 hồi chạm EMA21 | không lọc | 1155/1119/1207 | 2.0/1.5/48 | 0.93 | PF 0.82 · -22% · 219 lệnh | PF 0.72 · -44% · 221 lệnh | PF 0.83 · -30% · 209 lệnh | BỎ |
| Dải EMA 8/13/21 hồi chạm EMA21 | lọc 4h | 627/571/684 | 2.0/1.5/48 | 0.89 | PF 0.78 · -16% · 125 lệnh | PF 0.69 · -31% · 125 lệnh | PF 1.10 · +8% · 129 lệnh | BỎ |
| Dải EMA 8/13/21 hồi chạm EMA21 | lọc ngày | 560/568/593 | 2.0/1.5/48 | 0.92 | PF 0.80 · -14% · 114 lệnh | PF 0.86 · -15% · 119 lệnh | PF 0.92 · -9% · 108 lệnh | BỎ |
| Dải EMA 8/13/21 hồi chạm EMA21 | lọc 4h + ngày | 373/383/403 | 2.0/1.5/48 | 0.94 | PF 0.73 · -13% · 79 lệnh | PF 0.81 · -14% · 82 lệnh | PF 1.08 · +4% · 75 lệnh | BỎ |
| Stoch RSI cắt ở vùng quá mua/bán theo EMA50 | không lọc | 935/965/883 | 3.0/1.0/48 | 0.83 | PF 0.74 · -29% · 219 lệnh | PF 0.90 · -17% · 228 lệnh | PF 0.90 · -18% · 200 lệnh | BỎ |
| Stoch RSI cắt ở vùng quá mua/bán theo EMA50 | lọc 4h | 693/692/639 | 3.0/1.0/48 | 0.85 | PF 0.78 · -20% · 160 lệnh | PF 0.88 · -15% · 156 lệnh | PF 1.04 · +1% · 139 lệnh | BỎ |
| Stoch RSI cắt ở vùng quá mua/bán theo EMA50 | lọc ngày | 506/514/460 | 2.0/1.5/48 | 0.84 | PF 0.93 · -5% · 107 lệnh | PF 0.99 · -2% · 101 lệnh | PF 1.03 · +1% · 99 lệnh | BỎ |
| Stoch RSI cắt ở vùng quá mua/bán theo EMA50 | lọc 4h + ngày | 426/427/361 | 3.0/1.0/48 | 0.83 | PF 0.86 · -9% · 92 lệnh | PF 1.10 · +5% · 86 lệnh | PF 1.06 · +2% · 75 lệnh | BỎ |
| Connors RSI(2) < 10 / > 90 theo EMA200 | không lọc | 1214/1206/1239 | 3.0/1.5/48 | 0.91 | PF 0.72 · -37% · 221 lệnh | PF 0.79 · -34% · 206 lệnh | PF 0.81 · -37% · 207 lệnh | BỎ |
| Connors RSI(2) < 10 / > 90 theo EMA200 | lọc 4h | 1097/1104/1132 | 3.0/1.5/48 | 0.92 | PF 0.76 · -29% · 196 lệnh | PF 0.77 · -36% · 188 lệnh | PF 0.88 · -25% · 190 lệnh | BỎ |
| Connors RSI(2) < 10 / > 90 theo EMA200 | lọc ngày | 721/739/735 | 3.0/1.5/48 | 0.94 | PF 0.83 · -17% · 133 lệnh | PF 0.76 · -25% · 114 lệnh | PF 0.91 · -13% · 119 lệnh | BỎ |
| Connors RSI(2) < 10 / > 90 theo EMA200 | lọc 4h + ngày | 680/704/696 | 3.0/1.5/48 | 0.94 | PF 0.87 · -12% · 121 lệnh | PF 0.69 · -30% · 107 lệnh | PF 0.90 · -13% · 110 lệnh | BỎ |
| MACD histogram đổi dấu theo EMA200 | không lọc | 370/415/377 | 2.0/1.0/48 | 0.90 | PF 0.41 · -31% · 113 lệnh | PF 0.86 · -10% · 117 lệnh | PF 1.04 · +2% · 123 lệnh | BỎ |
| MACD histogram đổi dấu theo EMA200 | lọc 4h | 351/392/353 | 2.0/1.0/48 | 0.91 | PF 0.40 · -30% · 105 lệnh | PF 0.77 · -16% · 111 lệnh | PF 0.97 · -3% · 113 lệnh | BỎ |
| MACD histogram đổi dấu theo EMA200 | lọc ngày | 234/280/238 | 2.0/1.0/48 | 0.90 | PF 0.35 · -26% · 76 lệnh | PF 0.72 · -14% · 81 lệnh | PF 0.87 · -7% · 79 lệnh | BỎ |
| MACD histogram đổi dấu theo EMA200 | lọc 4h + ngày | 228/269/226 | 2.0/1.0/48 | 0.93 | PF 0.36 · -25% · 73 lệnh | PF 0.67 · -16% · 77 lệnh | PF 0.83 · -9% · 72 lệnh | BỎ |
| Phá đỉnh/đáy 20 nến (Donchian) | không lọc | 1636/1570/1807 | 2.0/1.5/48 | 0.89 | PF 0.93 · -14% · 314 lệnh | PF 0.92 · -20% · 283 lệnh | PF 0.90 · -30% · 321 lệnh | BỎ |
| Phá đỉnh/đáy 20 nến (Donchian) | lọc 4h | 878/838/990 | 2.0/1.5/48 | 0.98 | PF 0.78 · -23% · 183 lệnh | PF 1.01 · -1% · 147 lệnh | PF 1.02 · -1% · 187 lệnh | BỎ |
| Phá đỉnh/đáy 20 nến (Donchian) | lọc ngày | 855/845/938 | 2.0/1.5/48 | 1.00 | PF 0.85 · -16% · 166 lệnh | PF 0.99 · -4% · 152 lệnh | PF 0.86 · -23% · 170 lệnh | BỎ |
| Phá đỉnh/đáy 20 nến (Donchian) | lọc 4h + ngày | 567/555/613 | 2.0/1.5/48 | 1.00 | PF 0.69 · -23% · 114 lệnh | PF 0.84 · -14% · 92 lệnh | PF 0.96 · -6% · 105 lệnh | BỎ |
| Quét đỉnh/đáy phiên Á rồi quay lại | không lọc | 1131/1133/1106 | 3.0/0.5/48 | 0.76 | PF 0.63 · -40% · 258 lệnh | PF 0.82 · -29% · 259 lệnh | PF 0.98 · -7% · 262 lệnh | BỎ |
| Quét đỉnh/đáy phiên Á rồi quay lại | lọc 4h | 574/584/549 | 3.0/0.5/48 | 0.81 | PF 0.67 · -24% · 155 lệnh | PF 0.74 · -26% · 159 lệnh | PF 1.06 · +4% · 173 lệnh | BỎ |
| Quét đỉnh/đáy phiên Á rồi quay lại | lọc ngày | 562/552/561 | 2.0/0.5/48 | 0.75 | PF 0.68 · -21% · 156 lệnh | PF 0.66 · -29% · 154 lệnh | PF 0.82 · -19% · 172 lệnh | BỎ |
| Quét đỉnh/đáy phiên Á rồi quay lại | lọc 4h + ngày | 362/369/349 | 2.0/0.5/48 | 0.79 | PF 0.74 · -12% · 98 lệnh | PF 0.61 · -24% · 100 lệnh | PF 0.93 · -6% · 101 lệnh | BỎ |
| Phá biên phiên Á giờ London | không lọc | 574/580/591 | 2.0/1.5/48 | 0.81 | PF 0.77 · -20% · 163 lệnh | PF 0.76 · -28% · 158 lệnh | PF 1.05 · +4% · 155 lệnh | BỎ |
| Phá biên phiên Á giờ London | lọc 4h | 304/268/306 | 2.0/1.5/8 | 0.82 | PF 0.90 · -5% · 92 lệnh | PF 0.65 · -19% · 82 lệnh | PF 1.28 · +13% · 77 lệnh | BỎ |
| Phá biên phiên Á giờ London | lọc ngày | 287/285/299 | 3.0/1.0/48 | 0.87 | PF 0.71 · -13% · 85 lệnh | PF 0.76 · -14% · 82 lệnh | PF 0.94 · -5% · 80 lệnh | BỎ |
| Phá biên phiên Á giờ London | lọc 4h + ngày | 195/173/192 | 3.0/1.5/8 | 0.84 | PF 1.02 · +0% · 54 lệnh | PF 0.85 · -6% · 53 lệnh | PF 1.21 · +6% · 44 lệnh | BỎ |
| Quét đỉnh/đáy ngày trước rồi quay lại | không lọc | 774/776/826 | 2.0/0.5/16 | 0.99 | PF 0.83 · -16% · 220 lệnh | PF 0.76 · -27% · 216 lệnh | PF 0.85 · -22% · 230 lệnh | BỎ |
| Quét đỉnh/đáy ngày trước rồi quay lại | lọc 4h | 367/364/380 | 3.0/0.5/48 | 0.91 | PF 1.10 · +5% · 110 lệnh | PF 0.68 · -20% · 103 lệnh | PF 0.62 · -26% · 99 lệnh | BỎ |
| Quét đỉnh/đáy ngày trước rồi quay lại | lọc ngày | 381/378/406 | 2.0/0.5/48 | 1.04 | PF 0.72 · -14% · 111 lệnh | PF 0.94 · -4% · 108 lệnh | PF 0.79 · -17% · 124 lệnh | BỎ |
| Quét đỉnh/đáy ngày trước rồi quay lại | lọc 4h + ngày | 232/240/231 | 3.0/0.5/16 | 0.92 | PF 0.73 · -9% · 72 lệnh | PF 0.47 · -21% · 69 lệnh | PF 0.78 · -9% · 61 lệnh | BỎ |
| Mùa vụ giờ: mua 22:00, bán 00:00 UTC | không lọc | 1095/1095/1095 | 1.0/0.5/8 | 0.76 | PF 0.41 · -42% · 329 lệnh | PF 0.48 · -48% · 329 lệnh | PF 0.59 · -43% · 329 lệnh | BỎ |
| Mùa vụ giờ: mua 22:00, bán 00:00 UTC | lọc 4h | 602/565/567 | 1.0/0.5/8 | 0.87 | PF 0.46 · -21% · 162 lệnh | PF 0.53 · -26% · 173 lệnh | PF 0.63 · -21% · 158 lệnh | BỎ |
| Mùa vụ giờ: mua 22:00, bán 00:00 UTC | lọc ngày | 652/572/570 | 1.0/0.5/8 | 0.83 | PF 0.35 · -17% · 107 lệnh | PF 0.31 · -26% · 127 lệnh | PF 0.64 · -10% · 80 lệnh | BỎ |
| Mùa vụ giờ: mua 22:00, bán 00:00 UTC | lọc 4h + ngày | 427/366/357 | 1.0/0.5/8 | 0.89 | PF 0.49 · -8% · 69 lệnh | PF 0.40 · -15% · 84 lệnh | PF 1.22 · +2% · 47 lệnh | BỎ |
| Động lượng đầu ngày -> cuối ngày UTC | không lọc | 1094/1093/1090 | 1.0/0.5/8 | 0.59 | PF 0.41 · -31% · 329 lệnh | PF 0.54 · -29% · 328 lệnh | PF 0.68 · -24% · 326 lệnh | BỎ |
| Động lượng đầu ngày -> cuối ngày UTC | lọc 4h | 541/560/557 | 1.0/0.5/8 | 0.67 | PF 0.45 · -15% · 157 lệnh | PF 0.59 · -14% · 162 lệnh | PF 0.68 · -14% · 164 lệnh | BỎ |
| Động lượng đầu ngày -> cuối ngày UTC | lọc ngày | 533/536/537 | 1.0/0.5/8 | 0.60 | PF 0.45 · -14% · 166 lệnh | PF 0.57 · -13% · 155 lệnh | PF 0.90 · -4% · 153 lệnh | BỎ |
| Động lượng đầu ngày -> cuối ngày UTC | lọc 4h + ngày | 337/346/336 | 1.0/0.5/8 | 0.68 | PF 0.53 · -8% · 96 lệnh | PF 0.64 · -7% · 93 lệnh | PF 0.86 · -3% · 87 lệnh | BỎ |
| Động lượng đầu phiên Mỹ -> cuối phiên | không lọc | 0/0/0 | không có | | | | | BỎ |
| Động lượng đầu phiên Mỹ -> cuối phiên | lọc 4h | 0/0/0 | không có | | | | | BỎ |
| Động lượng đầu phiên Mỹ -> cuối phiên | lọc ngày | 0/0/0 | không có | | | | | BỎ |
| Động lượng đầu phiên Mỹ -> cuối phiên | lọc 4h + ngày | 0/0/0 | không có | | | | | BỎ |
