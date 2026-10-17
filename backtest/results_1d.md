# Kết quả backtest dự đoán xu hướng · khung 1D

## BTC · 2199 nến 1D · 2020-10-09 đến 2026-10-16

| Chiến lược | Số tín hiệu | Đúng hướng 1 tuần | 2 tuần | 4 tuần | Nền 4 tuần | LN TB 4 tuần |
|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 35 | 51% | 66% | 57% | 55% | 8.07% |
| Cắt EMA20/50 | 35 | 63% | 54% | 54% | 55% | 3.84% |
| Phá đỉnh/đáy 20 nến | 59 | 45% | 43% | 53% | 55% | 1.31% |
| Nén Bollinger rồi bung | 20 | 40% | 40% | 50% | 55% | -1.87% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 33 | 55% | 55% | 58% | 55% | 7.13% |
| Volume profile: thoát vùng giá trị | 44 | 57% | 55% | 57% | 55% | 1.44% |
| Volume profile: hồi về POC | 83 | 53% | 49% | 51% | 55% | -0.80% |
| Volume profile: cắt EMA lọc theo POC | 82 | 61% | 50% | 43% | 55% | -0.65% |
| RSI14 qua 50 (chuẩn so sánh) | 185 | 54% | 52% | 50% | 55% | 0.64% |
| VP thoát vùng + RSI xác nhận | 64 | 58% | 55% | 50% | 55% | 1.83% |
| VP thoát vùng + RSI + khối lượng 1,5x | 36 | 50% | 67% | 58% | 55% | 2.98% |
| VP thoát vùng + RSI + ADX20 | 40 | 50% | 57% | 55% | 55% | 1.89% |
| VP hồi trong vùng + RSI 30/70 | 6 | 67% | 33% | 50% | 55% | 1.45% |
| Đồng thuận POC + EMA + RSI | 60 | 67% | 48% | 45% | 55% | -0.22% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 34 | 47% | 62% | 56% | 55% | 2.64% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 34 | 47% | 62% | 56% | 55% | 2.64% |
| SMC: cấu trúc BOS/CHoCH | 75 | 46% | 44% | 49% | 55% | 0.47% |
| SMC: hồi về order block sau BOS | 52 | 44% | 35% | 44% | 55% | -1.80% |
| SMC: hồi về fair value gap | 27 | 52% | 44% | 37% | 55% | -0.75% |
| SMC: quét thanh khoản đảo chiều | 117 | 53% | 59% | 48% | 55% | -1.09% |
| SMC: quét thanh khoản + displacement | 64 | 56% | 56% | 53% | 55% | 0.16% |
| PA: nến nhấn chìm theo EMA50 | 134 | 56% | 53% | 49% | 55% | 2.23% |
| PA: pin bar tại đỉnh/đáy swing | 31 | 53% | 44% | 42% | 55% | -5.66% |
| PA: phá đỉnh/đáy rồi retest | 54 | 44% | 46% | 46% | 55% | -2.91% |
| PA: inside bar theo xu hướng EMA | 35 | 60% | 51% | 49% | 55% | 3.46% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 88 | 53% | 51% | 43% | 55% | 0.75% |
| CK: cắt SMA50/200 (golden/death cross) | 13 | 46% | 62% | 62% | 55% | 2.70% |
| CK: MACD histogram + lọc EMA200 | 110 | 43% | 42% | 53% | 55% | 0.18% |
| CK: Supertrend 10/3 | 55 | 42% | 44% | 49% | 55% | 0.83% |
| CK: Parabolic SAR | 185 | 49% | 49% | 48% | 55% | 0.40% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 69 | 54% | 48% | 46% | 55% | -0.21% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 41 | 57% | 64% | 63% | 55% | 6.01% |
| CK: Bollinger hồi về trung bình + SMA200 | 36 | 64% | 64% | 50% | 55% | 0.48% |
| CK: Minervini trend template | 40 | 52% | 50% | 52% | 55% | 1.70% |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 4 | 50% | 50% | 50% | 55% | 3.59% |
| CK: Elder Triple Screen (khung cao + Force Index) | 27 | 48% | 56% | 56% | 55% | 4.29% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 22 | 59% | 59% | 50% | 55% | -2.08% |
| CK: Turtle Donchian 55/20 | 30 | 61% | 68% | 67% | 55% | 6.40% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 0 | - | - | - | 55% | - |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 0 | - | - | - | 55% | - |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 28 | 46% | 43% | 50% | 55% | -0.17% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 33 | 64% | 61% | 42% | 55% | -0.66% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 75 | 56% | 52% | 53% | 55% | 0.77% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 41 | 63% | 71% | 63% | 55% | 6.20% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 31 | 68% | 65% | 61% | 55% | 3.23% |

| Chiến lược | Số lệnh | Thắng | LN/lệnh | Profit factor | Tổng LN cả kỳ | Sụt giảm tối đa | Mua và giữ | Tổng LN 24 tháng |
|---|---|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 35 | 43% | 3.00% | 2.39 | 140% | 28% | 638% | 47% |
| Cắt EMA20/50 | 39 | 44% | 7.70% | 2.37 | 323% | 51% | 638% | 35% |
| Phá đỉnh/đáy 20 nến | 63 | 40% | 3.73% | 1.71 | 101% | 56% | 638% | 6% |
| Nén Bollinger rồi bung | 30 | 40% | -2.01% | 0.73 | -61% | 76% | 638% | -0% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 33 | 36% | 2.00% | 1.57 | 56% | 29% | 638% | 44% |
| Volume profile: thoát vùng giá trị | 46 | 43% | 3.31% | 1.71 | 153% | 46% | 638% | 48% |
| Volume profile: hồi về POC | 83 | 42% | 0.19% | 1.08 | -0% | 36% | 638% | -6% |
| Volume profile: cắt EMA lọc theo POC | 83 | 30% | 2.49% | 1.81 | 280% | 40% | 638% | 49% |
| RSI14 qua 50 (chuẩn so sánh) | 190 | 26% | 1.72% | 1.76 | 571% | 50% | 638% | 51% |
| VP thoát vùng + RSI xác nhận | 65 | 34% | 1.71% | 1.49 | 91% | 46% | 638% | 45% |
| VP thoát vùng + RSI + khối lượng 1,5x | 37 | 49% | 4.39% | 1.95 | 193% | 37% | 638% | 45% |
| VP thoát vùng + RSI + ADX20 | 42 | 43% | 3.50% | 1.79 | 156% | 48% | 638% | 72% |
| VP hồi trong vùng + RSI 30/70 | 6 | 33% | -1.63% | 0.70 | -12% | 20% | 638% | 9% |
| Đồng thuận POC + EMA + RSI | 61 | 36% | 3.45% | 1.95 | 308% | 36% | 638% | 49% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 35 | 46% | 4.08% | 1.87 | 149% | 37% | 638% | 38% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 35 | 46% | 4.08% | 1.87 | 149% | 37% | 638% | 38% |
| SMC: cấu trúc BOS/CHoCH | 79 | 37% | 3.55% | 1.65 | 110% | 64% | 638% | -8% |
| SMC: hồi về order block sau BOS | 53 | 32% | 3.99% | 1.78 | 56% | 68% | 638% | -15% |
| SMC: hồi về fair value gap | 27 | 22% | 4.41% | 1.96 | 59% | 50% | 638% | -6% |
| SMC: quét thanh khoản đảo chiều | 119 | 42% | 0.53% | 1.16 | 12% | 55% | 638% | -23% |
| SMC: quét thanh khoản + displacement | 66 | 47% | 1.30% | 1.62 | 69% | 44% | 638% | 11% |
| PA: nến nhấn chìm theo EMA50 | 136 | 40% | 2.07% | 1.88 | 702% | 42% | 638% | 95% |
| PA: pin bar tại đỉnh/đáy swing | 33 | 30% | -0.82% | 0.81 | -35% | 51% | 638% | -3% |
| PA: phá đỉnh/đáy rồi retest | 56 | 18% | 4.85% | 3.23 | 254% | 34% | 638% | 11% |
| PA: inside bar theo xu hướng EMA | 36 | 14% | 0.89% | 1.14 | -41% | 77% | 638% | -23% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 99 | 64% | 0.23% | 1.12 | 3% | 54% | 638% | -3% |
| CK: cắt SMA50/200 (golden/death cross) | 22 | 27% | -0.35% | 0.96 | -44% | 57% | 638% | -31% |
| CK: MACD histogram + lọc EMA200 | 111 | 27% | 0.47% | 1.18 | 20% | 48% | 638% | 5% |
| CK: Supertrend 10/3 | 57 | 32% | 1.46% | 1.19 | -44% | 83% | 638% | -27% |
| CK: Parabolic SAR | 186 | 36% | 0.28% | 1.07 | -44% | 91% | 638% | -4% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 69 | 30% | 3.87% | 2.45 | 537% | 49% | 638% | 69% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 42 | 48% | 4.43% | 2.37 | 327% | 25% | 638% | 52% |
| CK: Bollinger hồi về trung bình + SMA200 | 46 | 76% | 1.29% | 1.41 | 45% | 54% | 638% | 42% |
| CK: Minervini trend template | 40 | 22% | 1.85% | 1.87 | 66% | 28% | 638% | -21% |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 4 | 50% | 3.50% | 2.12 | 12% | 7% | 638% | -1% |
| CK: Elder Triple Screen (khung cao + Force Index) | 37 | 30% | 1.80% | 1.30 | -0% | 61% | 638% | 1% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 25 | 48% | 1.38% | 1.26 | -4% | 49% | 638% | 5% |
| CK: Turtle Donchian 55/20 | 33 | 42% | 4.39% | 1.98 | 137% | 44% | 638% | 14% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 0 | | | | | | | |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 0 | | | | | | | |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 33 | 30% | -1.06% | 0.87 | -58% | 74% | 638% | -21% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 48 | 62% | 0.03% | 1.01 | -22% | 46% | 638% | -1% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 78 | 37% | 1.79% | 1.67 | 81% | 42% | 638% | 30% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 41 | 51% | 3.00% | 1.67 | 113% | 46% | 638% | 17% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 31 | 45% | 0.63% | 1.14 | -7% | 45% | 638% | -16% |

## ETH · 2199 nến 1D · 2020-10-09 đến 2026-10-16

| Chiến lược | Số tín hiệu | Đúng hướng 1 tuần | 2 tuần | 4 tuần | Nền 4 tuần | LN TB 4 tuần |
|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 30 | 40% | 63% | 63% | 53% | 2.82% |
| Cắt EMA20/50 | 37 | 54% | 59% | 59% | 53% | 4.19% |
| Phá đỉnh/đáy 20 nến | 58 | 53% | 47% | 62% | 53% | 3.29% |
| Nén Bollinger rồi bung | 16 | 69% | 81% | 62% | 53% | 10.69% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 32 | 50% | 59% | 59% | 53% | 2.07% |
| Volume profile: thoát vùng giá trị | 37 | 59% | 59% | 59% | 53% | 6.34% |
| Volume profile: hồi về POC | 84 | 53% | 57% | 62% | 53% | 2.80% |
| Volume profile: cắt EMA lọc theo POC | 91 | 52% | 53% | 52% | 53% | -0.44% |
| RSI14 qua 50 (chuẩn so sánh) | 199 | 48% | 48% | 52% | 53% | 1.19% |
| VP thoát vùng + RSI xác nhận | 56 | 50% | 50% | 46% | 53% | 3.44% |
| VP thoát vùng + RSI + khối lượng 1,5x | 28 | 68% | 68% | 61% | 53% | 10.42% |
| VP thoát vùng + RSI + ADX20 | 35 | 57% | 54% | 60% | 53% | 5.70% |
| VP hồi trong vùng + RSI 30/70 | 7 | 57% | 29% | 57% | 53% | 0.28% |
| Đồng thuận POC + EMA + RSI | 62 | 56% | 56% | 56% | 53% | 5.35% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 26 | 65% | 73% | 65% | 53% | 11.50% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 26 | 65% | 73% | 65% | 53% | 11.50% |
| SMC: cấu trúc BOS/CHoCH | 72 | 51% | 49% | 54% | 53% | 1.44% |
| SMC: hồi về order block sau BOS | 44 | 49% | 50% | 39% | 53% | -1.75% |
| SMC: hồi về fair value gap | 32 | 47% | 66% | 59% | 53% | 2.96% |
| SMC: quét thanh khoản đảo chiều | 110 | 58% | 52% | 49% | 53% | -0.97% |
| SMC: quét thanh khoản + displacement | 67 | 52% | 57% | 52% | 53% | 0.61% |
| PA: nến nhấn chìm theo EMA50 | 135 | 50% | 48% | 54% | 53% | 2.80% |
| PA: pin bar tại đỉnh/đáy swing | 35 | 47% | 50% | 51% | 53% | 3.25% |
| PA: phá đỉnh/đáy rồi retest | 65 | 41% | 38% | 55% | 53% | -0.37% |
| PA: inside bar theo xu hướng EMA | 29 | 45% | 69% | 66% | 53% | 5.57% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 85 | 45% | 45% | 45% | 53% | -3.33% |
| CK: cắt SMA50/200 (golden/death cross) | 13 | 69% | 62% | 62% | 53% | 7.32% |
| CK: MACD histogram + lọc EMA200 | 92 | 46% | 46% | 42% | 53% | -3.13% |
| CK: Supertrend 10/3 | 47 | 48% | 51% | 62% | 53% | 2.20% |
| CK: Parabolic SAR | 174 | 48% | 46% | 45% | 53% | -0.52% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 62 | 53% | 58% | 61% | 53% | 7.00% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 45 | 48% | 54% | 62% | 53% | 5.56% |
| CK: Bollinger hồi về trung bình + SMA200 | 35 | 44% | 60% | 29% | 53% | -3.96% |
| CK: Minervini trend template | 37 | 32% | 27% | 27% | 53% | -5.68% |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 7 | 43% | 43% | 86% | 53% | 6.34% |
| CK: Elder Triple Screen (khung cao + Force Index) | 33 | 55% | 48% | 55% | 53% | 3.18% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 21 | 67% | 52% | 67% | 53% | 3.33% |
| CK: Turtle Donchian 55/20 | 26 | 62% | 77% | 73% | 53% | 11.47% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 0 | - | - | - | 53% | - |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 0 | - | - | - | 53% | - |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 19 | 26% | 37% | 42% | 53% | 2.16% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 33 | 53% | 64% | 36% | 53% | -2.56% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 67 | 46% | 52% | 52% | 53% | 1.01% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 41 | 54% | 61% | 56% | 53% | 3.38% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 28 | 64% | 61% | 64% | 53% | 2.52% |

| Chiến lược | Số lệnh | Thắng | LN/lệnh | Profit factor | Tổng LN cả kỳ | Sụt giảm tối đa | Mua và giữ | Tổng LN 24 tháng |
|---|---|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 30 | 30% | 1.66% | 1.66 | 43% | 30% | 564% | 32% |
| Cắt EMA20/50 | 40 | 45% | 13.16% | 3.19 | 826% | 56% | 564% | 182% |
| Phá đỉnh/đáy 20 nến | 59 | 41% | 5.47% | 1.85 | 183% | 76% | 564% | 8% |
| Nén Bollinger rồi bung | 19 | 58% | 10.21% | 3.52 | 362% | 22% | 564% | 114% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 32 | 38% | 1.50% | 1.53 | 35% | 37% | 564% | -11% |
| Volume profile: thoát vùng giá trị | 38 | 47% | 7.29% | 2.44 | 523% | 59% | 564% | 202% |
| Volume profile: hồi về POC | 86 | 42% | -0.78% | 0.76 | -60% | 63% | 564% | -10% |
| Volume profile: cắt EMA lọc theo POC | 92 | 28% | 3.04% | 1.83 | 390% | 66% | 564% | 169% |
| RSI14 qua 50 (chuẩn so sánh) | 200 | 28% | 2.19% | 1.88 | 1299% | 56% | 564% | 405% |
| VP thoát vùng + RSI xác nhận | 56 | 36% | 3.19% | 1.72 | 218% | 50% | 564% | 138% |
| VP thoát vùng + RSI + khối lượng 1,5x | 28 | 57% | 10.53% | 3.89 | 774% | 35% | 564% | 168% |
| VP thoát vùng + RSI + ADX20 | 36 | 50% | 6.76% | 2.27 | 365% | 58% | 564% | 160% |
| VP hồi trong vùng + RSI 30/70 | 7 | 29% | -5.41% | 0.09 | -33% | 33% | 564% | -16% |
| Đồng thuận POC + EMA + RSI | 63 | 33% | 4.81% | 2.11 | 568% | 57% | 564% | 267% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 26 | 62% | 12.04% | 5.23 | 996% | 18% | 564% | 168% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 26 | 62% | 12.37% | 5.91 | 1108% | 18% | 564% | 168% |
| SMC: cấu trúc BOS/CHoCH | 75 | 40% | 4.54% | 1.69 | 94% | 61% | 564% | -42% |
| SMC: hồi về order block sau BOS | 45 | 31% | 5.85% | 2.10 | 85% | 58% | 564% | -33% |
| SMC: hồi về fair value gap | 32 | 41% | 13.14% | 3.57 | 626% | 41% | 564% | 17% |
| SMC: quét thanh khoản đảo chiều | 111 | 43% | 0.12% | 1.03 | -47% | 87% | 564% | -31% |
| SMC: quét thanh khoản + displacement | 69 | 33% | 4.60% | 2.54 | 226% | 68% | 564% | 55% |
| PA: nến nhấn chìm theo EMA50 | 135 | 30% | 0.71% | 1.22 | 16% | 70% | 564% | 31% |
| PA: pin bar tại đỉnh/đáy swing | 37 | 32% | -0.17% | 0.97 | -30% | 60% | 564% | -41% |
| PA: phá đỉnh/đáy rồi retest | 66 | 15% | -0.97% | 0.73 | -61% | 72% | 564% | -35% |
| PA: inside bar theo xu hướng EMA | 30 | 27% | 6.30% | 1.87 | 28% | 76% | 564% | 7% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 98 | 56% | -1.02% | 0.66 | -73% | 77% | 564% | -2% |
| CK: cắt SMA50/200 (golden/death cross) | 23 | 43% | -3.64% | 0.66 | -75% | 83% | 564% | -55% |
| CK: MACD histogram + lọc EMA200 | 94 | 35% | 1.49% | 1.36 | 72% | 49% | 564% | 12% |
| CK: Supertrend 10/3 | 50 | 48% | 7.26% | 2.10 | 339% | 63% | 564% | 114% |
| CK: Parabolic SAR | 176 | 32% | -0.47% | 0.92 | -92% | 99% | 564% | -76% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 62 | 34% | 5.27% | 2.21 | 555% | 50% | 564% | 295% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 46 | 48% | 2.31% | 1.46 | 64% | 48% | 564% | -2% |
| CK: Bollinger hồi về trung bình + SMA200 | 47 | 72% | 1.72% | 1.44 | 65% | 33% | 564% | -15% |
| CK: Minervini trend template | 37 | 14% | -0.10% | 0.97 | -25% | 53% | 564% | -3% |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 7 | 43% | -1.12% | 0.85 | -14% | 32% | 564% | 11% |
| CK: Elder Triple Screen (khung cao + Force Index) | 43 | 35% | -0.18% | 0.98 | -62% | 85% | 564% | 45% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 26 | 31% | -1.29% | 0.83 | -56% | 69% | 564% | -42% |
| CK: Turtle Donchian 55/20 | 27 | 48% | 13.95% | 3.98 | 567% | 59% | 564% | 122% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 0 | | | | | | | |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 0 | | | | | | | |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 21 | 33% | 11.79% | 2.32 | 224% | 49% | 564% | 70% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 50 | 58% | 0.08% | 1.01 | -35% | 56% | 564% | -53% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 73 | 30% | 1.89% | 1.47 | 48% | 72% | 564% | 7% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 41 | 44% | 2.82% | 1.52 | 75% | 66% | 564% | 13% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 28 | 50% | 2.17% | 1.42 | 27% | 54% | 564% | -5% |

## SOL · 2093 nến 1D · 2021-01-23 đến 2026-10-16

| Chiến lược | Số tín hiệu | Đúng hướng 1 tuần | 2 tuần | 4 tuần | Nền 4 tuần | LN TB 4 tuần |
|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 31 | 52% | 45% | 42% | 51% | -4.59% |
| Cắt EMA20/50 | 41 | 44% | 49% | 49% | 51% | 8.02% |
| Phá đỉnh/đáy 20 nến | 59 | 54% | 51% | 61% | 51% | 10.97% |
| Nén Bollinger rồi bung | 16 | 81% | 62% | 75% | 51% | 11.78% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 34 | 47% | 47% | 50% | 51% | 0.06% |
| Volume profile: thoát vùng giá trị | 40 | 48% | 42% | 48% | 51% | 5.96% |
| Volume profile: hồi về POC | 86 | 62% | 60% | 56% | 51% | 1.38% |
| Volume profile: cắt EMA lọc theo POC | 96 | 53% | 49% | 46% | 51% | 0.81% |
| RSI14 qua 50 (chuẩn so sánh) | 219 | 52% | 51% | 49% | 51% | 2.04% |
| VP thoát vùng + RSI xác nhận | 56 | 50% | 46% | 52% | 51% | 6.02% |
| VP thoát vùng + RSI + khối lượng 1,5x | 32 | 44% | 47% | 53% | 51% | 8.42% |
| VP thoát vùng + RSI + ADX20 | 37 | 38% | 35% | 46% | 51% | 4.72% |
| VP hồi trong vùng + RSI 30/70 | 10 | 80% | 50% | 40% | 51% | 1.98% |
| Đồng thuận POC + EMA + RSI | 73 | 51% | 52% | 45% | 51% | 2.38% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 30 | 47% | 47% | 53% | 51% | 9.58% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 30 | 47% | 47% | 53% | 51% | 9.58% |
| SMC: cấu trúc BOS/CHoCH | 73 | 45% | 52% | 60% | 51% | 8.62% |
| SMC: hồi về order block sau BOS | 52 | 45% | 54% | 54% | 51% | 10.71% |
| SMC: hồi về fair value gap | 27 | 41% | 41% | 48% | 51% | 2.84% |
| SMC: quét thanh khoản đảo chiều | 110 | 55% | 48% | 41% | 51% | -3.28% |
| SMC: quét thanh khoản + displacement | 74 | 51% | 54% | 39% | 51% | -5.51% |
| PA: nến nhấn chìm theo EMA50 | 116 | 51% | 53% | 53% | 51% | 4.51% |
| PA: pin bar tại đỉnh/đáy swing | 33 | 39% | 39% | 36% | 51% | -9.86% |
| PA: phá đỉnh/đáy rồi retest | 58 | 49% | 60% | 59% | 51% | 5.32% |
| PA: inside bar theo xu hướng EMA | 22 | 50% | 55% | 45% | 51% | 13.01% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 85 | 47% | 49% | 44% | 51% | -2.13% |
| CK: cắt SMA50/200 (golden/death cross) | 13 | 46% | 38% | 62% | 51% | 29.21% |
| CK: MACD histogram + lọc EMA200 | 88 | 48% | 49% | 58% | 51% | 4.41% |
| CK: Supertrend 10/3 | 41 | 51% | 56% | 66% | 51% | 14.96% |
| CK: Parabolic SAR | 159 | 58% | 52% | 53% | 51% | 3.76% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 73 | 59% | 51% | 62% | 51% | 11.37% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 40 | 57% | 52% | 55% | 51% | 9.31% |
| CK: Bollinger hồi về trung bình + SMA200 | 29 | 47% | 52% | 41% | 51% | -0.26% |
| CK: Minervini trend template | 32 | 61% | 52% | 44% | 51% | 4.36% |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 11 | 36% | 45% | 36% | 51% | -7.13% |
| CK: Elder Triple Screen (khung cao + Force Index) | 33 | 36% | 42% | 48% | 51% | 4.48% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 21 | 48% | 67% | 71% | 51% | 8.98% |
| CK: Turtle Donchian 55/20 | 25 | 60% | 60% | 56% | 51% | 22.37% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 0 | - | - | - | 51% | - |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 0 | - | - | - | 51% | - |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 18 | 61% | 67% | 72% | 51% | 17.90% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 24 | 46% | 38% | 33% | 51% | -3.75% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 93 | 47% | 54% | 52% | 51% | 2.15% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 38 | 47% | 58% | 63% | 51% | 12.96% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 27 | 44% | 59% | 67% | 51% | 9.97% |

| Chiến lược | Số lệnh | Thắng | LN/lệnh | Profit factor | Tổng LN cả kỳ | Sụt giảm tối đa | Mua và giữ | Tổng LN 24 tháng |
|---|---|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 31 | 32% | 1.49% | 1.38 | 18% | 47% | 2876% | -9% |
| Cắt EMA20/50 | 45 | 31% | 17.87% | 2.74 | 223% | 76% | 2876% | -27% |
| Phá đỉnh/đáy 20 nến | 60 | 42% | 8.79% | 2.22 | 459% | 71% | 2876% | -30% |
| Nén Bollinger rồi bung | 18 | 67% | 10.85% | 2.63 | 246% | 58% | 2876% | 5% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 34 | 32% | -0.64% | 0.88 | -42% | 59% | 2876% | -8% |
| Volume profile: thoát vùng giá trị | 42 | 31% | 19.01% | 2.92 | 463% | 67% | 2876% | -1% |
| Volume profile: hồi về POC | 87 | 44% | -0.02% | 1.00 | -44% | 67% | 2876% | -17% |
| Volume profile: cắt EMA lọc theo POC | 98 | 21% | 7.96% | 2.53 | 266% | 71% | 2876% | -15% |
| RSI14 qua 50 (chuẩn so sánh) | 220 | 28% | 4.31% | 2.38 | 4932% | 58% | 2876% | 52% |
| VP thoát vùng + RSI xác nhận | 56 | 36% | 8.62% | 2.38 | 382% | 53% | 2876% | 24% |
| VP thoát vùng + RSI + khối lượng 1,5x | 35 | 37% | 21.50% | 3.28 | 790% | 59% | 2876% | 10% |
| VP thoát vùng + RSI + ADX20 | 41 | 32% | 17.44% | 2.70 | 169% | 83% | 2876% | -21% |
| VP hồi trong vùng + RSI 30/70 | 10 | 50% | 5.58% | 2.25 | 47% | 35% | 2876% | - |
| Đồng thuận POC + EMA + RSI | 75 | 25% | 10.23% | 2.63 | 246% | 71% | 2876% | -10% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 34 | 38% | 22.10% | 3.33 | 787% | 62% | 2876% | 10% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 33 | 36% | 20.98% | 3.13 | 457% | 67% | 2876% | 10% |
| SMC: cấu trúc BOS/CHoCH | 77 | 40% | 6.19% | 1.72 | 51% | 82% | 2876% | -45% |
| SMC: hồi về order block sau BOS | 53 | 36% | 9.37% | 2.20 | 331% | 72% | 2876% | 11% |
| SMC: hồi về fair value gap | 28 | 32% | -1.29% | 0.87 | -67% | 87% | 2876% | 13% |
| SMC: quét thanh khoản đảo chiều | 111 | 35% | -2.23% | 0.68 | -97% | 98% | 2876% | -37% |
| SMC: quét thanh khoản + displacement | 74 | 43% | -0.49% | 0.84 | -52% | 67% | 2876% | -5% |
| PA: nến nhấn chìm theo EMA50 | 117 | 38% | 4.47% | 2.21 | 2359% | 52% | 2876% | 38% |
| PA: pin bar tại đỉnh/đáy swing | 33 | 30% | -2.40% | 0.65 | -67% | 71% | 2876% | -12% |
| PA: phá đỉnh/đáy rồi retest | 59 | 19% | 2.55% | 1.56 | 10% | 54% | 2876% | -18% |
| PA: inside bar theo xu hướng EMA | 22 | 27% | 17.83% | 2.27 | -54% | 95% | 2876% | 1% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 91 | 60% | 0.38% | 1.16 | 7% | 43% | 2876% | 32% |
| CK: cắt SMA50/200 (golden/death cross) | 24 | 38% | 13.77% | 2.08 | 1% | 84% | 2876% | -68% |
| CK: MACD histogram + lọc EMA200 | 89 | 37% | 5.74% | 2.40 | 1132% | 56% | 2876% | 9% |
| CK: Supertrend 10/3 | 43 | 51% | 31.02% | 6.18 | 28864% | 40% | 2876% | 15% |
| CK: Parabolic SAR | 160 | 46% | 4.12% | 1.73 | 1879% | 81% | 2876% | -38% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 73 | 27% | 9.60% | 2.97 | 1312% | 67% | 2876% | 35% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 40 | 50% | 16.68% | 3.62 | 1934% | 72% | 2876% | -32% |
| CK: Bollinger hồi về trung bình + SMA200 | 37 | 59% | 0.01% | 1.00 | -33% | 75% | 2876% | 41% |
| CK: Minervini trend template | 33 | 27% | 7.46% | 2.88 | 310% | 56% | 2876% | -49% |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 11 | 27% | -7.20% | 0.45 | -67% | 71% | 2876% | 7% |
| CK: Elder Triple Screen (khung cao + Force Index) | 40 | 32% | 9.07% | 1.95 | -27% | 85% | 2876% | -63% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 24 | 17% | 13.83% | 2.40 | -17% | 90% | 2876% | -79% |
| CK: Turtle Donchian 55/20 | 30 | 43% | 24.49% | 4.16 | 1282% | 64% | 2876% | -53% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 0 | | | | | | | |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 0 | | | | | | | |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 24 | 42% | 6.79% | 1.59 | 22% | 70% | 2876% | -14% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 37 | 54% | -2.82% | 0.70 | -84% | 89% | 2876% | -51% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 98 | 29% | 4.80% | 1.86 | -34% | 77% | 2876% | -31% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 39 | 44% | 20.61% | 4.15 | 2107% | 77% | 2876% | -39% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 28 | 39% | 12.81% | 3.21 | 438% | 69% | 2876% | -47% |
