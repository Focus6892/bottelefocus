# Kết quả backtest dự đoán xu hướng · khung 1D

## BTC · 2199 nến 1D · 2020-10-09 đến 2026-10-16

| Chiến lược | Số tín hiệu | Đúng hướng 1 tuần | 2 tuần | 4 tuần | Nền 4 tuần | LN TB 4 tuần |
|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 35 | 49% | 66% | 57% | 55% | 7.75% |
| Cắt EMA20/50 | 35 | 63% | 54% | 54% | 55% | 3.84% |
| Phá đỉnh/đáy 20 nến | 59 | 45% | 43% | 53% | 55% | 1.31% |
| Nén Bollinger rồi bung | 20 | 40% | 40% | 50% | 55% | -1.87% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 33 | 52% | 55% | 58% | 55% | 7.39% |
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
| SMC: hồi về order block sau BOS | 27 | 30% | 33% | 44% | 55% | -4.76% |
| SMC: hồi về fair value gap | 40 | 55% | 49% | 38% | 55% | -3.47% |
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
| CK: bung kênh Keltner EMA20 ± 2 ATR | 41 | 57% | 64% | 63% | 55% | 6.04% |
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
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 41 | 63% | 71% | 63% | 55% | 6.23% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 31 | 68% | 65% | 61% | 55% | 3.23% |

| Chiến lược | Số lệnh | Thắng | LN/lệnh | Profit factor | Tổng LN cả kỳ | Sụt giảm tối đa | Mua và giữ | Tổng LN 24 tháng |
|---|---|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 35 | 43% | 2.62% | 2.25 | 115% | 34% | 638% | 48% |
| Cắt EMA20/50 | 32 | 47% | 9.61% | 2.74 | 389% | 60% | 638% | 24% |
| Phá đỉnh/đáy 20 nến | 56 | 43% | 4.85% | 1.95 | 198% | 53% | 638% | -0% |
| Nén Bollinger rồi bung | 20 | 45% | -0.43% | 0.94 | -28% | 58% | 638% | 17% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 33 | 39% | 2.08% | 1.60 | 60% | 36% | 638% | 48% |
| Volume profile: thoát vùng giá trị | 43 | 42% | 2.08% | 1.42 | 53% | 56% | 638% | 26% |
| Volume profile: hồi về POC | 83 | 42% | 0.19% | 1.08 | -0% | 39% | 638% | -6% |
| Volume profile: cắt EMA lọc theo POC | 81 | 30% | 1.92% | 1.63 | 159% | 46% | 638% | 31% |
| RSI14 qua 50 (chuẩn so sánh) | 188 | 26% | 1.71% | 1.75 | 538% | 57% | 638% | 21% |
| VP thoát vùng + RSI xác nhận | 63 | 33% | 1.85% | 1.55 | 104% | 53% | 638% | 14% |
| VP thoát vùng + RSI + khối lượng 1,5x | 35 | 46% | 2.70% | 1.55 | 70% | 48% | 638% | 18% |
| VP thoát vùng + RSI + ADX20 | 40 | 42% | 2.31% | 1.50 | 68% | 53% | 638% | 39% |
| VP hồi trong vùng + RSI 30/70 | 6 | 33% | -1.63% | 0.70 | -12% | 24% | 638% | 9% |
| Đồng thuận POC + EMA + RSI | 60 | 35% | 2.53% | 1.68 | 158% | 45% | 638% | 20% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 34 | 44% | 2.47% | 1.51 | 57% | 45% | 638% | 12% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 34 | 44% | 2.47% | 1.51 | 57% | 45% | 638% | 12% |
| SMC: cấu trúc BOS/CHoCH | 73 | 38% | 4.32% | 1.81 | 203% | 68% | 638% | -17% |
| SMC: hồi về order block sau BOS | 27 | 26% | -0.55% | 0.90 | -34% | 59% | 638% | -10% |
| SMC: hồi về fair value gap | 42 | 29% | 2.47% | 1.53 | 23% | 73% | 638% | -15% |
| SMC: quét thanh khoản đảo chiều | 118 | 42% | 0.55% | 1.16 | 13% | 55% | 638% | -23% |
| SMC: quét thanh khoản + displacement | 65 | 48% | 1.38% | 1.66 | 75% | 45% | 638% | -13% |
| PA: nến nhấn chìm theo EMA50 | 135 | 41% | 2.12% | 1.90 | 738% | 42% | 638% | 115% |
| PA: pin bar tại đỉnh/đáy swing | 33 | 30% | -0.82% | 0.81 | -35% | 54% | 638% | -3% |
| PA: phá đỉnh/đáy rồi retest | 56 | 18% | 4.85% | 3.23 | 254% | 43% | 638% | -13% |
| PA: inside bar theo xu hướng EMA | 36 | 14% | 0.89% | 1.14 | -41% | 82% | 638% | -23% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 89 | 64% | 0.22% | 1.12 | 3% | 54% | 638% | 5% |
| CK: cắt SMA50/200 (golden/death cross) | 13 | 38% | 2.11% | 1.21 | -16% | 61% | 638% | 3% |
| CK: MACD histogram + lọc EMA200 | 111 | 27% | 0.47% | 1.18 | 20% | 50% | 638% | 4% |
| CK: Supertrend 10/3 | 47 | 30% | 2.00% | 1.24 | -35% | 85% | 638% | -38% |
| CK: Parabolic SAR | 182 | 35% | 0.00% | 1.00 | -64% | 94% | 638% | -26% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 69 | 30% | 3.87% | 2.45 | 537% | 57% | 638% | 36% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 42 | 48% | 4.35% | 2.34 | 317% | 36% | 638% | 54% |
| CK: Bollinger hồi về trung bình + SMA200 | 36 | 78% | 0.99% | 1.30 | 18% | 55% | 638% | 27% |
| CK: Minervini trend template | 40 | 22% | 1.85% | 1.87 | 66% | 38% | 638% | -21% |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 4 | 50% | 3.50% | 2.12 | 12% | 13% | 638% | -1% |
| CK: Elder Triple Screen (khung cao + Force Index) | 27 | 33% | 2.66% | 1.38 | 10% | 68% | 638% | -1% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 21 | 43% | -1.00% | 0.81 | -33% | 55% | 638% | 6% |
| CK: Turtle Donchian 55/20 | 31 | 45% | 4.88% | 2.06 | 152% | 46% | 638% | -2% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 0 | | | | | | | |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 0 | | | | | | | |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 23 | 22% | -4.81% | 0.52 | -77% | 80% | 638% | -63% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 33 | 70% | 0.95% | 1.23 | 11% | 44% | 638% | -7% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 72 | 38% | 1.73% | 1.66 | 63% | 55% | 638% | 51% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 41 | 51% | 2.92% | 1.66 | 108% | 54% | 638% | 19% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 31 | 45% | 0.63% | 1.14 | -7% | 54% | 638% | -16% |

## ETH · 2199 nến 1D · 2020-10-09 đến 2026-10-16

| Chiến lược | Số tín hiệu | Đúng hướng 1 tuần | 2 tuần | 4 tuần | Nền 4 tuần | LN TB 4 tuần |
|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 29 | 41% | 59% | 62% | 53% | 2.11% |
| Cắt EMA20/50 | 37 | 54% | 59% | 59% | 53% | 4.19% |
| Phá đỉnh/đáy 20 nến | 58 | 53% | 47% | 62% | 53% | 3.29% |
| Nén Bollinger rồi bung | 16 | 69% | 81% | 62% | 53% | 10.69% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 32 | 50% | 59% | 59% | 53% | 1.57% |
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
| SMC: hồi về order block sau BOS | 23 | 43% | 35% | 43% | 53% | -4.43% |
| SMC: hồi về fair value gap | 44 | 52% | 61% | 61% | 53% | 4.65% |
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
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 29 | 31% | 2.18% | 1.89 | 61% | 38% | 564% | 42% |
| Cắt EMA20/50 | 35 | 40% | 11.99% | 2.77 | 301% | 67% | 564% | -3% |
| Phá đỉnh/đáy 20 nến | 56 | 43% | 6.06% | 1.94 | 236% | 78% | 564% | 10% |
| Nén Bollinger rồi bung | 16 | 62% | 12.60% | 4.03 | 401% | 34% | 564% | 142% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 32 | 38% | 1.67% | 1.60 | 41% | 43% | 564% | -9% |
| Volume profile: thoát vùng giá trị | 37 | 49% | 7.96% | 2.68 | 655% | 57% | 564% | 229% |
| Volume profile: hồi về POC | 86 | 42% | -0.78% | 0.76 | -60% | 67% | 564% | -10% |
| Volume profile: cắt EMA lọc theo POC | 91 | 29% | 3.27% | 1.93 | 494% | 61% | 564% | 138% |
| RSI14 qua 50 (chuẩn so sánh) | 200 | 28% | 2.19% | 1.88 | 1299% | 71% | 564% | 394% |
| VP thoát vùng + RSI xác nhận | 56 | 36% | 3.19% | 1.72 | 218% | 60% | 564% | 159% |
| VP thoát vùng + RSI + khối lượng 1,5x | 28 | 57% | 10.53% | 3.89 | 774% | 51% | 564% | 192% |
| VP thoát vùng + RSI + ADX20 | 35 | 51% | 7.45% | 2.50 | 463% | 58% | 564% | 160% |
| VP hồi trong vùng + RSI 30/70 | 7 | 29% | -5.41% | 0.09 | -33% | 34% | 564% | -16% |
| Đồng thuận POC + EMA + RSI | 62 | 34% | 5.17% | 2.25 | 709% | 55% | 564% | 225% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 26 | 62% | 12.04% | 5.23 | 996% | 51% | 564% | 174% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 26 | 62% | 12.37% | 5.91 | 1108% | 51% | 564% | 174% |
| SMC: cấu trúc BOS/CHoCH | 68 | 40% | 5.34% | 1.81 | 158% | 70% | 564% | -49% |
| SMC: hồi về order block sau BOS | 23 | 26% | 11.80% | 3.41 | 146% | 52% | 564% | -40% |
| SMC: hồi về fair value gap | 44 | 45% | 10.79% | 3.33 | 972% | 63% | 564% | 8% |
| SMC: quét thanh khoản đảo chiều | 111 | 43% | 0.12% | 1.03 | -47% | 88% | 564% | -31% |
| SMC: quét thanh khoản + displacement | 67 | 33% | 4.72% | 2.57 | 224% | 79% | 564% | 69% |
| PA: nến nhấn chìm theo EMA50 | 132 | 29% | 0.63% | 1.19 | 5% | 72% | 564% | 10% |
| PA: pin bar tại đỉnh/đáy swing | 37 | 32% | -0.17% | 0.97 | -30% | 62% | 564% | -41% |
| PA: phá đỉnh/đáy rồi retest | 66 | 15% | -0.97% | 0.73 | -61% | 74% | 564% | -35% |
| PA: inside bar theo xu hướng EMA | 29 | 28% | 6.75% | 1.93 | 37% | 85% | 564% | -4% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 86 | 58% | -0.92% | 0.69 | -65% | 74% | 564% | 9% |
| CK: cắt SMA50/200 (golden/death cross) | 13 | 31% | -6.83% | 0.49 | -71% | 90% | 564% | 7% |
| CK: MACD histogram + lọc EMA200 | 91 | 33% | 1.37% | 1.32 | 49% | 56% | 564% | -15% |
| CK: Supertrend 10/3 | 40 | 45% | 7.48% | 1.96 | 151% | 75% | 564% | 17% |
| CK: Parabolic SAR | 170 | 30% | -1.02% | 0.82 | -96% | 99% | 564% | -89% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 62 | 34% | 5.27% | 2.21 | 555% | 75% | 564% | 234% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 46 | 48% | 2.31% | 1.46 | 64% | 58% | 564% | 0% |
| CK: Bollinger hồi về trung bình + SMA200 | 36 | 69% | 1.39% | 1.32 | 26% | 47% | 564% | -10% |
| CK: Minervini trend template | 37 | 14% | -0.10% | 0.97 | -25% | 58% | 564% | -11% |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 7 | 43% | -1.12% | 0.85 | -14% | 35% | 564% | 11% |
| CK: Elder Triple Screen (khung cao + Force Index) | 33 | 36% | 0.41% | 1.05 | -51% | 89% | 564% | 59% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 21 | 38% | 1.21% | 1.18 | -16% | 58% | 564% | -15% |
| CK: Turtle Donchian 55/20 | 25 | 52% | 15.45% | 4.30 | 636% | 67% | 564% | 127% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 0 | | | | | | | |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 0 | | | | | | | |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 17 | 29% | 11.30% | 2.15 | 113% | 76% | 564% | 94% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 34 | 62% | 0.62% | 1.11 | -11% | 50% | 564% | -44% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 65 | 29% | 2.30% | 1.60 | 75% | 83% | 564% | 41% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 41 | 44% | 2.82% | 1.52 | 75% | 72% | 564% | -5% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 28 | 50% | 2.17% | 1.42 | 27% | 64% | 564% | -20% |

## SOL · 2093 nến 1D · 2021-01-23 đến 2026-10-16

| Chiến lược | Số tín hiệu | Đúng hướng 1 tuần | 2 tuần | 4 tuần | Nền 4 tuần | LN TB 4 tuần |
|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 31 | 48% | 45% | 39% | 51% | -4.73% |
| Cắt EMA20/50 | 41 | 44% | 49% | 49% | 51% | 8.02% |
| Phá đỉnh/đáy 20 nến | 59 | 54% | 51% | 61% | 51% | 10.97% |
| Nén Bollinger rồi bung | 16 | 81% | 62% | 75% | 51% | 11.78% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 34 | 41% | 47% | 47% | 51% | 0.06% |
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
| SMC: hồi về order block sau BOS | 34 | 53% | 53% | 59% | 51% | 6.80% |
| SMC: hồi về fair value gap | 46 | 50% | 43% | 54% | 51% | 13.39% |
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
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 31 | 32% | 1.70% | 1.44 | 21% | 57% | 2876% | -13% |
| Cắt EMA20/50 | 37 | 27% | 22.06% | 3.09 | 333% | 83% | 2876% | -18% |
| Phá đỉnh/đáy 20 nến | 58 | 41% | 9.29% | 2.33 | 553% | 75% | 2876% | -37% |
| Nén Bollinger rồi bung | 16 | 69% | 9.94% | 2.76 | 196% | 62% | 2876% | 5% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 34 | 32% | -0.47% | 0.91 | -41% | 64% | 2876% | -12% |
| Volume profile: thoát vùng giá trị | 39 | 28% | 17.66% | 2.69 | 144% | 78% | 2876% | 8% |
| Volume profile: hồi về POC | 87 | 44% | -0.02% | 1.00 | -44% | 67% | 2876% | -21% |
| Volume profile: cắt EMA lọc theo POC | 96 | 21% | 7.87% | 2.48 | 194% | 77% | 2876% | -10% |
| RSI14 qua 50 (chuẩn so sánh) | 220 | 28% | 4.31% | 2.38 | 4932% | 74% | 2876% | 78% |
| VP thoát vùng + RSI xác nhận | 55 | 35% | 7.86% | 2.24 | 220% | 71% | 2876% | 33% |
| VP thoát vùng + RSI + khối lượng 1,5x | 31 | 35% | 20.77% | 3.01 | 290% | 72% | 2876% | 21% |
| VP thoát vùng + RSI + ADX20 | 37 | 30% | 17.98% | 2.65 | 94% | 81% | 2876% | -15% |
| VP hồi trong vùng + RSI 30/70 | 10 | 50% | 5.58% | 2.25 | 47% | 35% | 2876% | - |
| Đồng thuận POC + EMA + RSI | 73 | 25% | 10.17% | 2.59 | 178% | 79% | 2876% | -4% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 30 | 37% | 22.56% | 3.16 | 401% | 70% | 2876% | 21% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 30 | 37% | 22.53% | 3.14 | 387% | 70% | 2876% | 17% |
| SMC: cấu trúc BOS/CHoCH | 70 | 37% | 4.94% | 1.53 | -44% | 92% | 2876% | -64% |
| SMC: hồi về order block sau BOS | 34 | 41% | 5.82% | 1.85 | 63% | 65% | 2876% | 8% |
| SMC: hồi về fair value gap | 47 | 34% | 4.35% | 1.47 | -24% | 89% | 2876% | -18% |
| SMC: quét thanh khoản đảo chiều | 111 | 35% | -2.23% | 0.68 | -97% | 98% | 2876% | -22% |
| SMC: quét thanh khoản + displacement | 74 | 43% | -0.49% | 0.84 | -52% | 69% | 2876% | 15% |
| PA: nến nhấn chìm theo EMA50 | 117 | 38% | 4.47% | 2.21 | 2359% | 62% | 2876% | 38% |
| PA: pin bar tại đỉnh/đáy swing | 33 | 30% | -2.40% | 0.65 | -67% | 75% | 2876% | -12% |
| PA: phá đỉnh/đáy rồi retest | 59 | 19% | 2.55% | 1.56 | 10% | 70% | 2876% | -18% |
| PA: inside bar theo xu hướng EMA | 22 | 27% | 17.83% | 2.27 | -54% | 97% | 2876% | 1% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 86 | 59% | 0.17% | 1.07 | -12% | 47% | 2876% | 30% |
| CK: cắt SMA50/200 (golden/death cross) | 13 | 38% | 32.48% | 3.25 | 196% | 86% | 2876% | -53% |
| CK: MACD histogram + lọc EMA200 | 89 | 37% | 5.74% | 2.40 | 1132% | 64% | 2876% | 11% |
| CK: Supertrend 10/3 | 40 | 50% | 32.36% | 6.41 | 21527% | 64% | 2876% | 36% |
| CK: Parabolic SAR | 158 | 45% | 3.91% | 1.69 | 1261% | 85% | 2876% | -59% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 73 | 27% | 9.60% | 2.97 | 1312% | 75% | 2876% | 31% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 40 | 50% | 16.68% | 3.62 | 1934% | 78% | 2876% | -30% |
| CK: Bollinger hồi về trung bình + SMA200 | 30 | 57% | 0.41% | 1.07 | -19% | 68% | 2876% | 29% |
| CK: Minervini trend template | 33 | 27% | 7.46% | 2.88 | 310% | 66% | 2876% | -49% |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 11 | 27% | -7.20% | 0.45 | -67% | 72% | 2876% | 7% |
| CK: Elder Triple Screen (khung cao + Force Index) | 33 | 33% | 11.54% | 2.08 | -10% | 88% | 2876% | -58% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 21 | 19% | 17.67% | 2.88 | 30% | 91% | 2876% | -67% |
| CK: Turtle Donchian 55/20 | 25 | 48% | 30.27% | 4.94 | 1703% | 67% | 2876% | -42% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 0 | | | | | | | |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 0 | | | | | | | |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 18 | 50% | 10.31% | 1.92 | 87% | 83% | 2876% | -31% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 25 | 48% | -4.31% | 0.59 | -80% | 89% | 2876% | -55% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 90 | 28% | 0.07% | 1.01 | -89% | 95% | 2876% | -23% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 38 | 42% | 21.05% | 4.13 | 2022% | 83% | 2876% | -38% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 27 | 37% | 13.13% | 3.19 | 418% | 78% | 2876% | -47% |
