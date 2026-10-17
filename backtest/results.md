# Kết quả backtest dự đoán xu hướng · khung 4h

## BTC · 6569 nến 4h · 2023-10-18 đến 2026-10-17

| Chiến lược | Số tín hiệu | Đúng hướng 1d | 3d | 7d | Nền 7d | LN TB 7d |
|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 159 | 50% | 45% | 46% | 54% | -0.40% |
| Cắt EMA20/50 | 118 | 46% | 51% | 58% | 54% | 0.50% |
| Phá đỉnh/đáy 20 nến | 179 | 52% | 54% | 50% | 54% | 0.34% |
| Nén Bollinger rồi bung | 27 | 48% | 44% | 56% | 54% | 0.15% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 133 | 50% | 53% | 45% | 54% | 0.34% |
| Volume profile: thoát vùng giá trị | 72 | 63% | 59% | 50% | 54% | 0.77% |
| Volume profile: hồi về POC | 213 | 47% | 48% | 51% | 54% | -0.22% |
| Volume profile: cắt EMA lọc theo POC | 239 | 56% | 59% | 56% | 54% | 1.01% |
| RSI14 qua 50 (chuẩn so sánh) | 658 | 49% | 49% | 50% | 54% | 0.07% |
| VP thoát vùng + RSI xác nhận | 154 | 53% | 48% | 48% | 54% | 0.35% |
| VP thoát vùng + RSI + khối lượng 1,5x | 67 | 65% | 59% | 48% | 54% | 0.67% |
| VP thoát vùng + RSI + ADX20 | 71 | 53% | 57% | 52% | 54% | 0.73% |
| VP hồi trong vùng + RSI 30/70 | 35 | 60% | 63% | 46% | 54% | -1.70% |
| Đồng thuận POC + EMA + RSI | 173 | 54% | 59% | 54% | 54% | 1.06% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 67 | 63% | 57% | 48% | 54% | 0.65% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 71 | 62% | 58% | 49% | 54% | 0.79% |
| SMC: cấu trúc BOS/CHoCH | 142 | 53% | 52% | 58% | 54% | 0.96% |
| SMC: hồi về order block sau BOS | 67 | 56% | 54% | 52% | 54% | 1.24% |
| SMC: hồi về fair value gap | 96 | 55% | 54% | 58% | 54% | 0.53% |
| SMC: quét thanh khoản đảo chiều | 251 | 51% | 49% | 49% | 54% | -0.51% |
| SMC: quét thanh khoản + displacement | 179 | 45% | 49% | 46% | 54% | -0.71% |
| PA: nến nhấn chìm theo EMA50 | 477 | 50% | 50% | 50% | 54% | -0.04% |
| PA: pin bar tại đỉnh/đáy swing | 116 | 43% | 50% | 55% | 54% | 0.36% |
| PA: phá đỉnh/đáy rồi retest | 118 | 51% | 53% | 57% | 54% | 1.28% |
| PA: inside bar theo xu hướng EMA | 78 | 55% | 55% | 59% | 54% | 1.03% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 267 | 51% | 56% | 52% | 54% | 0.63% |
| CK: cắt SMA50/200 (golden/death cross) | 41 | 41% | 41% | 51% | 54% | 0.13% |
| CK: MACD histogram + lọc EMA200 | 343 | 45% | 52% | 46% | 54% | -0.05% |
| CK: Supertrend 10/3 | 154 | 50% | 51% | 53% | 54% | 0.28% |
| CK: Parabolic SAR | 536 | 49% | 48% | 48% | 54% | -0.03% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 247 | 47% | 53% | 53% | 54% | 0.19% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 132 | 54% | 47% | 52% | 54% | 0.22% |
| CK: Bollinger hồi về trung bình + SMA200 | 102 | 56% | 55% | 53% | 54% | 0.74% |
| CK: Minervini trend template | 55 | 45% | 47% | 62% | 54% | 2.52% |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 39 | 54% | 49% | 56% | 54% | 0.48% |
| CK: Elder Triple Screen (khung cao + Force Index) | 107 | 52% | 57% | 45% | 54% | -0.34% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 97 | 43% | 45% | 53% | 54% | 0.53% |
| CK: Turtle Donchian 55/20 | 77 | 53% | 45% | 51% | 54% | 0.49% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 0 | - | - | - | 54% | - |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 0 | - | - | - | 54% | - |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 71 | 49% | 54% | 49% | 54% | 0.37% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 88 | 58% | 55% | 53% | 54% | 0.63% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 332 | 49% | 49% | 51% | 54% | 0.12% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 127 | 48% | 51% | 53% | 54% | 0.74% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 115 | 43% | 48% | 52% | 54% | 1.04% |

| Chiến lược | Số lệnh | Thắng | LN/lệnh | Profit factor | Tổng LN cả kỳ | Sụt giảm tối đa | Mua và giữ | Tổng LN 12 tháng |
|---|---|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 159 | 27% | 0.01% | 1.01 | -8% | 38% | 187% | -6% |
| Cắt EMA20/50 | 108 | 31% | 0.98% | 1.59 | 112% | 38% | 187% | 26% |
| Phá đỉnh/đáy 20 nến | 175 | 31% | 0.06% | 1.04 | -7% | 59% | 187% | -25% |
| Nén Bollinger rồi bung | 27 | 33% | 0.27% | 1.19 | 4% | 23% | 187% | 22% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 133 | 33% | 0.30% | 1.27 | 34% | 27% | 187% | -4% |
| Volume profile: thoát vùng giá trị | 73 | 27% | 0.25% | 1.13 | 8% | 46% | 187% | 32% |
| Volume profile: hồi về POC | 215 | 30% | -0.13% | 0.84 | -28% | 33% | 187% | -7% |
| Volume profile: cắt EMA lọc theo POC | 236 | 23% | 0.08% | 1.07 | -2% | 49% | 187% | -12% |
| RSI14 qua 50 (chuẩn so sánh) | 634 | 22% | -0.01% | 0.99 | -28% | 63% | 187% | -21% |
| VP thoát vùng + RSI xác nhận | 156 | 24% | 0.06% | 1.04 | -5% | 47% | 187% | 15% |
| VP thoát vùng + RSI + khối lượng 1,5x | 68 | 29% | 0.39% | 1.20 | 17% | 45% | 187% | 32% |
| VP thoát vùng + RSI + ADX20 | 72 | 28% | 0.17% | 1.09 | 2% | 46% | 187% | 28% |
| VP hồi trong vùng + RSI 30/70 | 35 | 43% | 0.12% | 1.13 | 3% | 11% | 187% | 1% |
| Đồng thuận POC + EMA + RSI | 174 | 28% | 0.18% | 1.14 | 12% | 43% | 187% | -6% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 68 | 29% | 0.38% | 1.19 | 16% | 45% | 187% | 31% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 72 | 28% | 0.51% | 1.26 | 26% | 40% | 187% | 35% |
| SMC: cấu trúc BOS/CHoCH | 124 | 35% | 0.87% | 1.55 | 127% | 41% | 187% | 3% |
| SMC: hồi về order block sau BOS | 68 | 32% | 0.87% | 1.65 | 61% | 38% | 187% | -28% |
| SMC: hồi về fair value gap | 97 | 37% | 0.76% | 1.53 | 80% | 24% | 187% | -11% |
| SMC: quét thanh khoản đảo chiều | 253 | 34% | -0.37% | 0.72 | -65% | 67% | 187% | -19% |
| SMC: quét thanh khoản + displacement | 181 | 33% | -0.16% | 0.76 | -29% | 47% | 187% | 6% |
| PA: nến nhấn chìm theo EMA50 | 475 | 30% | -0.11% | 0.86 | -49% | 61% | 187% | -28% |
| PA: pin bar tại đỉnh/đáy swing | 116 | 37% | -0.12% | 0.90 | -17% | 30% | 187% | -1% |
| PA: phá đỉnh/đáy rồi retest | 121 | 21% | 0.43% | 1.47 | 52% | 33% | 187% | -12% |
| PA: inside bar theo xu hướng EMA | 79 | 28% | 1.26% | 1.78 | 107% | 36% | 187% | 22% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 267 | 62% | -0.09% | 0.87 | -24% | 26% | 187% | -3% |
| CK: cắt SMA50/200 (golden/death cross) | 42 | 17% | 0.85% | 1.38 | 17% | 41% | 187% | 9% |
| CK: MACD histogram + lọc EMA200 | 339 | 29% | 0.04% | 1.04 | -3% | 50% | 187% | 34% |
| CK: Supertrend 10/3 | 130 | 32% | -0.05% | 0.98 | -24% | 65% | 187% | -16% |
| CK: Parabolic SAR | 445 | 32% | -0.36% | 0.72 | -84% | 84% | 187% | -44% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 243 | 22% | 0.11% | 1.09 | 4% | 47% | 187% | -11% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 132 | 33% | 0.32% | 1.23 | 33% | 27% | 187% | 14% |
| CK: Bollinger hồi về trung bình + SMA200 | 102 | 54% | -0.16% | 0.88 | -18% | 41% | 187% | 11% |
| CK: Minervini trend template | 55 | 20% | 0.14% | 1.10 | 1% | 33% | 187% | -16% |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 39 | 26% | -0.12% | 0.92 | -8% | 25% | 187% | -16% |
| CK: Elder Triple Screen (khung cao + Force Index) | 108 | 29% | 0.14% | 1.08 | -2% | 50% | 187% | 33% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 98 | 28% | 0.98% | 1.60 | 90% | 36% | 187% | 6% |
| CK: Turtle Donchian 55/20 | 75 | 28% | 0.81% | 1.45 | 45% | 35% | 187% | 17% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 0 | | | | | | | |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 0 | | | | | | | |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 66 | 33% | 2.02% | 2.08 | 209% | 37% | 187% | -5% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 88 | 44% | -0.14% | 0.91 | -16% | 33% | 187% | 13% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 317 | 29% | 0.30% | 1.35 | 86% | 34% | 187% | 44% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 127 | 34% | 0.64% | 1.44 | 82% | 29% | 187% | 21% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 115 | 32% | 0.67% | 1.45 | 79% | 32% | 187% | 20% |

## ETH · 6569 nến 4h · 2023-10-18 đến 2026-10-17

| Chiến lược | Số tín hiệu | Đúng hướng 1d | 3d | 7d | Nền 7d | LN TB 7d |
|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 141 | 45% | 44% | 56% | 52% | 1.35% |
| Cắt EMA20/50 | 134 | 47% | 46% | 52% | 52% | 0.27% |
| Phá đỉnh/đáy 20 nến | 170 | 47% | 45% | 48% | 52% | -0.03% |
| Nén Bollinger rồi bung | 30 | 47% | 60% | 67% | 52% | 0.38% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 141 | 52% | 48% | 61% | 52% | 2.71% |
| Volume profile: thoát vùng giá trị | 68 | 44% | 43% | 56% | 52% | 2.57% |
| Volume profile: hồi về POC | 196 | 42% | 47% | 45% | 52% | -1.07% |
| Volume profile: cắt EMA lọc theo POC | 254 | 41% | 43% | 46% | 52% | -0.74% |
| RSI14 qua 50 (chuẩn so sánh) | 718 | 49% | 48% | 49% | 52% | -0.06% |
| VP thoát vùng + RSI xác nhận | 143 | 45% | 48% | 55% | 52% | 1.71% |
| VP thoát vùng + RSI + khối lượng 1,5x | 61 | 48% | 43% | 57% | 52% | 3.03% |
| VP thoát vùng + RSI + ADX20 | 64 | 45% | 48% | 58% | 52% | 2.36% |
| VP hồi trong vùng + RSI 30/70 | 43 | 53% | 53% | 49% | 52% | -1.16% |
| Đồng thuận POC + EMA + RSI | 190 | 44% | 42% | 47% | 52% | -0.51% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 61 | 49% | 43% | 54% | 52% | 2.95% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 67 | 48% | 43% | 52% | 52% | 2.36% |
| SMC: cấu trúc BOS/CHoCH | 142 | 55% | 50% | 50% | 52% | 0.22% |
| SMC: hồi về order block sau BOS | 67 | 40% | 45% | 42% | 52% | -2.57% |
| SMC: hồi về fair value gap | 98 | 58% | 42% | 53% | 52% | 0.46% |
| SMC: quét thanh khoản đảo chiều | 228 | 55% | 52% | 52% | 52% | 0.37% |
| SMC: quét thanh khoản + displacement | 162 | 47% | 48% | 49% | 52% | -0.13% |
| PA: nến nhấn chìm theo EMA50 | 469 | 46% | 46% | 48% | 52% | 0.28% |
| PA: pin bar tại đỉnh/đáy swing | 109 | 50% | 54% | 49% | 52% | -0.23% |
| PA: phá đỉnh/đáy rồi retest | 102 | 44% | 42% | 48% | 52% | -0.69% |
| PA: inside bar theo xu hướng EMA | 78 | 44% | 42% | 54% | 52% | 1.15% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 308 | 53% | 54% | 54% | 52% | 1.30% |
| CK: cắt SMA50/200 (golden/death cross) | 31 | 50% | 44% | 48% | 52% | 0.36% |
| CK: MACD histogram + lọc EMA200 | 325 | 47% | 47% | 48% | 52% | 0.25% |
| CK: Supertrend 10/3 | 152 | 47% | 43% | 48% | 52% | 0.06% |
| CK: Parabolic SAR | 518 | 47% | 51% | 48% | 52% | -0.10% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 247 | 44% | 42% | 45% | 52% | -0.77% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 120 | 53% | 53% | 57% | 52% | 2.08% |
| CK: Bollinger hồi về trung bình + SMA200 | 99 | 58% | 64% | 60% | 52% | 2.07% |
| CK: Minervini trend template | 111 | 45% | 47% | 50% | 52% | 0.91% |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 33 | 27% | 39% | 39% | 52% | -2.28% |
| CK: Elder Triple Screen (khung cao + Force Index) | 114 | 50% | 46% | 47% | 52% | -0.33% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 76 | 47% | 47% | 53% | 52% | 1.46% |
| CK: Turtle Donchian 55/20 | 80 | 56% | 52% | 59% | 52% | 1.40% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 0 | - | - | - | 52% | - |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 0 | - | - | - | 52% | - |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 79 | 48% | 54% | 53% | 52% | 0.38% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 91 | 52% | 59% | 55% | 52% | 1.31% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 274 | 49% | 51% | 49% | 52% | 0.14% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 121 | 53% | 48% | 53% | 52% | 1.47% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 107 | 48% | 43% | 53% | 52% | 1.96% |

| Chiến lược | Số lệnh | Thắng | LN/lệnh | Profit factor | Tổng LN cả kỳ | Sụt giảm tối đa | Mua và giữ | Tổng LN 12 tháng |
|---|---|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 141 | 25% | 0.09% | 1.06 | -4% | 43% | 54% | -8% |
| Cắt EMA20/50 | 120 | 24% | 1.01% | 1.40 | 87% | 47% | 54% | 12% |
| Phá đỉnh/đáy 20 nến | 160 | 26% | 0.10% | 1.05 | -20% | 60% | 54% | -17% |
| Nén Bollinger rồi bung | 30 | 40% | 1.17% | 1.62 | 33% | 29% | 54% | 38% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 141 | 27% | 0.41% | 1.28 | 47% | 44% | 54% | 29% |
| Volume profile: thoát vùng giá trị | 68 | 28% | 2.04% | 1.81 | 169% | 38% | 54% | 8% |
| Volume profile: hồi về POC | 199 | 30% | -0.12% | 0.90 | -29% | 46% | 54% | -5% |
| Volume profile: cắt EMA lọc theo POC | 248 | 19% | 0.28% | 1.18 | 15% | 51% | 54% | -20% |
| RSI14 qua 50 (chuẩn so sánh) | 696 | 21% | -0.01% | 0.99 | -42% | 77% | 54% | -36% |
| VP thoát vùng + RSI xác nhận | 146 | 33% | 0.48% | 1.26 | 48% | 30% | 54% | 2% |
| VP thoát vùng + RSI + khối lượng 1,5x | 61 | 28% | 2.14% | 1.84 | 162% | 35% | 54% | 12% |
| VP thoát vùng + RSI + ADX20 | 64 | 33% | 2.60% | 2.10 | 258% | 37% | 54% | 31% |
| VP hồi trong vùng + RSI 30/70 | 43 | 35% | -0.19% | 0.88 | -10% | 21% | 54% | -6% |
| Đồng thuận POC + EMA + RSI | 190 | 21% | 0.21% | 1.10 | -13% | 56% | 54% | -15% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 61 | 28% | 1.99% | 1.76 | 139% | 39% | 54% | 9% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 67 | 30% | 1.81% | 1.73 | 136% | 32% | 54% | 1% |
| SMC: cấu trúc BOS/CHoCH | 122 | 28% | 0.42% | 1.17 | 10% | 69% | 54% | -46% |
| SMC: hồi về order block sau BOS | 67 | 12% | -1.53% | 0.36 | -66% | 70% | 54% | -39% |
| SMC: hồi về fair value gap | 98 | 34% | 0.46% | 1.22 | 25% | 37% | 54% | -16% |
| SMC: quét thanh khoản đảo chiều | 230 | 36% | -0.05% | 0.97 | -30% | 48% | 54% | -11% |
| SMC: quét thanh khoản + displacement | 163 | 36% | 0.08% | 1.09 | 2% | 36% | 54% | -10% |
| PA: nến nhấn chìm theo EMA50 | 460 | 29% | -0.19% | 0.84 | -67% | 77% | 54% | -40% |
| PA: pin bar tại đỉnh/đáy swing | 109 | 30% | -0.37% | 0.80 | -39% | 50% | 54% | -3% |
| PA: phá đỉnh/đáy rồi retest | 102 | 13% | -0.21% | 0.86 | -28% | 51% | 54% | -27% |
| PA: inside bar theo xu hướng EMA | 78 | 28% | 1.96% | 1.88 | 212% | 45% | 54% | 58% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 310 | 65% | 0.04% | 1.05 | 3% | 35% | 54% | 17% |
| CK: cắt SMA50/200 (golden/death cross) | 32 | 28% | 3.91% | 2.44 | 147% | 40% | 54% | 21% |
| CK: MACD histogram + lọc EMA200 | 323 | 30% | 0.53% | 1.41 | 270% | 50% | 54% | -4% |
| CK: Supertrend 10/3 | 132 | 27% | 0.03% | 1.01 | -31% | 71% | 54% | -7% |
| CK: Parabolic SAR | 439 | 36% | -0.19% | 0.89 | -73% | 82% | 54% | -58% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 238 | 19% | 0.03% | 1.02 | -31% | 71% | 54% | -7% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 121 | 38% | 0.74% | 1.41 | 95% | 36% | 54% | -7% |
| CK: Bollinger hồi về trung bình + SMA200 | 100 | 67% | 0.79% | 1.69 | 107% | 24% | 54% | 13% |
| CK: Minervini trend template | 111 | 22% | 0.38% | 1.25 | 29% | 38% | 54% | 2% |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 33 | 21% | -0.59% | 0.75 | -22% | 47% | 54% | 6% |
| CK: Elder Triple Screen (khung cao + Force Index) | 114 | 24% | 0.34% | 1.14 | -3% | 56% | 54% | -24% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 78 | 23% | 1.88% | 1.86 | 167% | 35% | 54% | 12% |
| CK: Turtle Donchian 55/20 | 79 | 32% | 0.46% | 1.19 | 10% | 53% | 54% | -15% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 0 | | | | | | | |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 0 | | | | | | | |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 70 | 17% | -1.43% | 0.61 | -70% | 74% | 54% | -40% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 92 | 58% | 0.56% | 1.37 | 55% | 31% | 54% | 19% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 252 | 33% | 0.72% | 1.57 | 245% | 41% | 54% | 41% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 122 | 32% | 0.97% | 1.44 | 120% | 35% | 54% | 12% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 109 | 29% | 0.93% | 1.41 | 91% | 34% | 54% | 9% |

## SOL · 6569 nến 4h · 2023-10-18 đến 2026-10-17

| Chiến lược | Số tín hiệu | Đúng hướng 1d | 3d | 7d | Nền 7d | LN TB 7d |
|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 144 | 57% | 55% | 52% | 51% | 1.53% |
| Cắt EMA20/50 | 126 | 56% | 51% | 53% | 51% | 0.74% |
| Phá đỉnh/đáy 20 nến | 180 | 50% | 49% | 48% | 51% | 0.42% |
| Nén Bollinger rồi bung | 33 | 48% | 39% | 45% | 51% | -0.12% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 140 | 56% | 54% | 50% | 51% | 1.70% |
| Volume profile: thoát vùng giá trị | 65 | 56% | 52% | 57% | 51% | 1.84% |
| Volume profile: hồi về POC | 182 | 51% | 51% | 50% | 51% | -1.26% |
| Volume profile: cắt EMA lọc theo POC | 228 | 54% | 49% | 51% | 51% | 0.01% |
| RSI14 qua 50 (chuẩn so sánh) | 762 | 49% | 49% | 50% | 51% | 0.09% |
| VP thoát vùng + RSI xác nhận | 148 | 50% | 51% | 51% | 51% | 1.72% |
| VP thoát vùng + RSI + khối lượng 1,5x | 57 | 55% | 53% | 60% | 51% | 1.99% |
| VP thoát vùng + RSI + ADX20 | 61 | 48% | 52% | 57% | 51% | 1.08% |
| VP hồi trong vùng + RSI 30/70 | 40 | 52% | 70% | 65% | 51% | 3.21% |
| Đồng thuận POC + EMA + RSI | 168 | 55% | 49% | 51% | 51% | 0.18% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 57 | 53% | 53% | 60% | 51% | 1.81% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 60 | 52% | 52% | 58% | 51% | 1.86% |
| SMC: cấu trúc BOS/CHoCH | 156 | 46% | 48% | 52% | 51% | 0.64% |
| SMC: hồi về order block sau BOS | 81 | 48% | 46% | 51% | 51% | -0.15% |
| SMC: hồi về fair value gap | 102 | 51% | 52% | 56% | 51% | 1.30% |
| SMC: quét thanh khoản đảo chiều | 240 | 54% | 55% | 54% | 51% | 0.35% |
| SMC: quét thanh khoản + displacement | 205 | 56% | 53% | 50% | 51% | 0.53% |
| PA: nến nhấn chìm theo EMA50 | 464 | 49% | 49% | 48% | 51% | -0.18% |
| PA: pin bar tại đỉnh/đáy swing | 72 | 60% | 57% | 60% | 51% | 1.75% |
| PA: phá đỉnh/đáy rồi retest | 146 | 51% | 53% | 56% | 51% | 2.00% |
| PA: inside bar theo xu hướng EMA | 90 | 49% | 54% | 58% | 51% | 0.18% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 285 | 49% | 49% | 48% | 51% | 0.77% |
| CK: cắt SMA50/200 (golden/death cross) | 35 | 47% | 61% | 60% | 51% | 1.50% |
| CK: MACD histogram + lọc EMA200 | 359 | 50% | 49% | 47% | 51% | 0.04% |
| CK: Supertrend 10/3 | 148 | 47% | 42% | 54% | 51% | 1.12% |
| CK: Parabolic SAR | 547 | 52% | 51% | 49% | 51% | 0.07% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 237 | 51% | 49% | 49% | 51% | 0.41% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 128 | 59% | 51% | 54% | 51% | 0.99% |
| CK: Bollinger hồi về trung bình + SMA200 | 92 | 53% | 52% | 51% | 51% | 2.62% |
| CK: Minervini trend template | 145 | 41% | 38% | 48% | 51% | 0.66% |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 21 | 43% | 38% | 48% | 51% | 0.42% |
| CK: Elder Triple Screen (khung cao + Force Index) | 119 | 53% | 46% | 48% | 51% | -0.63% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 82 | 45% | 52% | 55% | 51% | 1.47% |
| CK: Turtle Donchian 55/20 | 77 | 62% | 55% | 58% | 51% | 2.60% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 0 | - | - | - | 51% | - |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 0 | - | - | - | 51% | - |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 78 | 47% | 44% | 50% | 51% | -1.46% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 96 | 53% | 56% | 51% | 51% | 1.04% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 256 | 53% | 50% | 52% | 51% | -0.06% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 124 | 50% | 42% | 50% | 51% | -0.12% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 101 | 49% | 45% | 54% | 51% | 0.97% |

| Chiến lược | Số lệnh | Thắng | LN/lệnh | Profit factor | Tổng LN cả kỳ | Sụt giảm tối đa | Mua và giữ | Tổng LN 12 tháng |
|---|---|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 144 | 41% | 0.36% | 1.23 | 35% | 49% | 342% | 10% |
| Cắt EMA20/50 | 122 | 32% | 1.21% | 1.44 | 127% | 57% | 342% | -3% |
| Phá đỉnh/đáy 20 nến | 176 | 36% | 0.25% | 1.09 | -8% | 63% | 342% | -14% |
| Nén Bollinger rồi bung | 33 | 21% | -0.57% | 0.83 | -25% | 49% | 342% | -19% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 140 | 34% | 0.05% | 1.03 | -12% | 65% | 342% | 22% |
| Volume profile: thoát vùng giá trị | 66 | 32% | 0.09% | 1.03 | -18% | 57% | 342% | 70% |
| Volume profile: hồi về POC | 182 | 33% | -0.20% | 0.87 | -38% | 53% | 342% | -13% |
| Volume profile: cắt EMA lọc theo POC | 227 | 26% | 0.46% | 1.26 | 63% | 60% | 342% | 20% |
| RSI14 qua 50 (chuẩn so sánh) | 745 | 20% | -0.03% | 0.98 | -64% | 85% | 342% | -1% |
| VP thoát vùng + RSI xác nhận | 149 | 36% | 0.60% | 1.28 | 68% | 38% | 342% | 42% |
| VP thoát vùng + RSI + khối lượng 1,5x | 58 | 34% | 1.25% | 1.40 | 50% | 51% | 342% | 45% |
| VP thoát vùng + RSI + ADX20 | 62 | 31% | -0.18% | 0.95 | -29% | 59% | 342% | 62% |
| VP hồi trong vùng + RSI 30/70 | 40 | 50% | 0.97% | 1.62 | 39% | 25% | 342% | 50% |
| Đồng thuận POC + EMA + RSI | 168 | 26% | 0.56% | 1.26 | 50% | 59% | 342% | -4% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 58 | 34% | 0.98% | 1.31 | 31% | 56% | 342% | 45% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 61 | 38% | 1.30% | 1.47 | 65% | 49% | 342% | 51% |
| SMC: cấu trúc BOS/CHoCH | 145 | 37% | 0.93% | 1.32 | 97% | 64% | 342% | -29% |
| SMC: hồi về order block sau BOS | 82 | 30% | 0.91% | 1.41 | 48% | 55% | 342% | 14% |
| SMC: hồi về fair value gap | 103 | 33% | 0.85% | 1.30 | 52% | 69% | 342% | 6% |
| SMC: quét thanh khoản đảo chiều | 242 | 33% | -0.30% | 0.87 | -65% | 83% | 342% | 52% |
| SMC: quét thanh khoản + displacement | 206 | 50% | 0.53% | 1.66 | 140% | 37% | 342% | 64% |
| PA: nến nhấn chìm theo EMA50 | 459 | 34% | 0.01% | 1.01 | -32% | 52% | 342% | -16% |
| PA: pin bar tại đỉnh/đáy swing | 72 | 40% | 0.44% | 1.20 | 23% | 32% | 342% | 19% |
| PA: phá đỉnh/đáy rồi retest | 148 | 18% | 0.21% | 1.14 | 0% | 63% | 342% | -4% |
| PA: inside bar theo xu hướng EMA | 91 | 29% | 1.07% | 1.38 | 63% | 57% | 342% | 12% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 286 | 63% | -0.01% | 0.99 | -15% | 40% | 342% | -7% |
| CK: cắt SMA50/200 (golden/death cross) | 35 | 31% | 4.73% | 2.51 | 223% | 44% | 342% | 16% |
| CK: MACD histogram + lọc EMA200 | 359 | 30% | 0.18% | 1.11 | 20% | 63% | 342% | -9% |
| CK: Supertrend 10/3 | 134 | 30% | 0.27% | 1.09 | -29% | 79% | 342% | -32% |
| CK: Parabolic SAR | 472 | 39% | -0.05% | 0.98 | -61% | 78% | 342% | -40% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 230 | 20% | 0.05% | 1.02 | -33% | 65% | 342% | -28% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 129 | 40% | 0.37% | 1.15 | 19% | 49% | 342% | -6% |
| CK: Bollinger hồi về trung bình + SMA200 | 92 | 59% | 0.26% | 1.13 | 14% | 44% | 342% | -3% |
| CK: Minervini trend template | 145 | 20% | -0.28% | 0.86 | -49% | 72% | 342% | -7% |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 21 | 29% | 0.42% | 1.17 | 4% | 43% | 342% | -1% |
| CK: Elder Triple Screen (khung cao + Force Index) | 120 | 29% | 1.11% | 1.41 | 79% | 65% | 342% | 11% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 83 | 24% | 1.81% | 1.60 | 21% | 81% | 342% | 16% |
| CK: Turtle Donchian 55/20 | 77 | 39% | 2.09% | 1.80 | 247% | 46% | 342% | 21% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 0 | | | | | | | |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 0 | | | | | | | |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 68 | 24% | -0.20% | 0.95 | -41% | 77% | 342% | 23% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 97 | 57% | 0.75% | 1.38 | 81% | 34% | 342% | -2% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 240 | 34% | 0.20% | 1.12 | -6% | 77% | 342% | -3% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 125 | 33% | 0.85% | 1.33 | 50% | 58% | 342% | -2% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 101 | 34% | 1.14% | 1.40 | 69% | 59% | 342% | 7% |
