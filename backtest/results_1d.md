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
