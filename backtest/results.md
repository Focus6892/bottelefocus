# Kết quả backtest dự đoán xu hướng · khung 4h

## BTC · 6569 nến 4h · 2023-10-18 đến 2026-10-17

| Chiến lược | Số tín hiệu | Đúng hướng 1d | 3d | 7d | Nền 7d | LN TB 7d |
|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 159 | 50% | 43% | 45% | 54% | -0.37% |
| Cắt EMA20/50 | 118 | 46% | 51% | 58% | 54% | 0.50% |
| Phá đỉnh/đáy 20 nến | 179 | 52% | 54% | 50% | 54% | 0.34% |
| Nén Bollinger rồi bung | 27 | 48% | 44% | 56% | 54% | 0.15% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 134 | 51% | 51% | 45% | 54% | 0.40% |
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
| SMC: hồi về order block sau BOS | 100 | 51% | 50% | 54% | 54% | 0.87% |
| SMC: hồi về fair value gap | 72 | 49% | 45% | 54% | 54% | 0.06% |
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
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 167 | 26% | -0.03% | 0.97 | -14% | 38% | 187% | -9% |
| Cắt EMA20/50 | 174 | 31% | 0.48% | 1.33 | 63% | 39% | 187% | 21% |
| Phá đỉnh/đáy 20 nến | 227 | 30% | 0.03% | 1.02 | -14% | 58% | 187% | -28% |
| Nén Bollinger rồi bung | 68 | 34% | 0.00% | 1.00 | -5% | 36% | 187% | 39% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 140 | 31% | 0.22% | 1.20 | 22% | 21% | 187% | -4% |
| Volume profile: thoát vùng giá trị | 112 | 28% | 0.32% | 1.18 | 18% | 39% | 187% | 24% |
| Volume profile: hồi về POC | 219 | 30% | -0.12% | 0.85 | -27% | 32% | 187% | -7% |
| Volume profile: cắt EMA lọc theo POC | 258 | 22% | 0.04% | 1.03 | -12% | 45% | 187% | -5% |
| RSI14 qua 50 (chuẩn so sánh) | 672 | 23% | -0.00% | 1.00 | -28% | 66% | 187% | -23% |
| VP thoát vùng + RSI xác nhận | 175 | 23% | -0.01% | 0.99 | -16% | 52% | 187% | 11% |
| VP thoát vùng + RSI + khối lượng 1,5x | 109 | 28% | 0.36% | 1.21 | 23% | 38% | 187% | 20% |
| VP thoát vùng + RSI + ADX20 | 113 | 27% | 0.12% | 1.07 | -4% | 41% | 187% | 20% |
| VP hồi trong vùng + RSI 30/70 | 40 | 48% | 0.72% | 1.76 | 30% | 8% | 187% | 19% |
| Đồng thuận POC + EMA + RSI | 197 | 27% | 0.13% | 1.10 | 5% | 36% | 187% | 2% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 110 | 28% | 0.33% | 1.19 | 19% | 38% | 187% | 19% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 111 | 27% | 0.19% | 1.11 | 6% | 39% | 187% | 27% |
| SMC: cấu trúc BOS/CHoCH | 203 | 32% | 0.63% | 1.42 | 157% | 40% | 187% | -24% |
| SMC: hồi về order block sau BOS | 120 | 27% | 0.72% | 1.49 | 88% | 41% | 187% | -28% |
| SMC: hồi về fair value gap | 97 | 32% | 0.66% | 1.44 | 63% | 23% | 187% | 6% |
| SMC: quét thanh khoản đảo chiều | 261 | 33% | -0.33% | 0.75 | -62% | 66% | 187% | -22% |
| SMC: quét thanh khoản + displacement | 191 | 32% | -0.18% | 0.74 | -33% | 48% | 187% | 4% |
| PA: nến nhấn chìm theo EMA50 | 500 | 30% | -0.11% | 0.87 | -49% | 60% | 187% | -23% |
| PA: pin bar tại đỉnh/đáy swing | 117 | 38% | -0.08% | 0.94 | -13% | 30% | 187% | -4% |
| PA: phá đỉnh/đáy rồi retest | 123 | 21% | 0.37% | 1.38 | 41% | 31% | 187% | -15% |
| PA: inside bar theo xu hướng EMA | 94 | 27% | 1.08% | 1.69 | 108% | 27% | 187% | 34% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 340 | 62% | -0.10% | 0.85 | -32% | 36% | 187% | -6% |
| CK: cắt SMA50/200 (golden/death cross) | 112 | 24% | 0.69% | 1.37 | 42% | 48% | 187% | 33% |
| CK: MACD histogram + lọc EMA200 | 362 | 29% | 0.01% | 1.01 | -14% | 50% | 187% | 27% |
| CK: Supertrend 10/3 | 207 | 31% | 0.05% | 1.03 | -19% | 45% | 187% | -29% |
| CK: Parabolic SAR | 576 | 34% | -0.20% | 0.84 | -77% | 79% | 187% | -39% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 268 | 23% | 0.05% | 1.05 | -9% | 51% | 187% | -15% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 149 | 32% | 0.15% | 1.11 | 9% | 33% | 187% | 10% |
| CK: Bollinger hồi về trung bình + SMA200 | 181 | 55% | -0.03% | 0.98 | -11% | 39% | 187% | 1% |
| CK: Minervini trend template | 65 | 20% | -0.13% | 0.91 | -14% | 36% | 187% | -18% |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 55 | 25% | -0.28% | 0.81 | -18% | 34% | 187% | -28% |
| CK: Elder Triple Screen (khung cao + Force Index) | 167 | 35% | 0.43% | 1.30 | 49% | 41% | 187% | 28% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 162 | 30% | 0.33% | 1.23 | 20% | 34% | 187% | 7% |
| CK: Turtle Donchian 55/20 | 116 | 31% | 0.67% | 1.41 | 66% | 32% | 187% | 20% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 0 | | | | | | | |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 0 | | | | | | | |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 116 | 27% | 1.38% | 1.70 | 255% | 34% | 187% | 48% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 187 | 47% | -0.13% | 0.91 | -29% | 47% | 187% | 9% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 361 | 29% | 0.19% | 1.21 | 41% | 30% | 187% | 22% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 159 | 33% | 0.35% | 1.24 | 39% | 31% | 187% | 7% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 150 | 31% | 0.28% | 1.19 | 26% | 34% | 187% | 4% |

## ETH · 6569 nến 4h · 2023-10-18 đến 2026-10-17

| Chiến lược | Số tín hiệu | Đúng hướng 1d | 3d | 7d | Nền 7d | LN TB 7d |
|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 142 | 45% | 45% | 56% | 52% | 1.27% |
| Cắt EMA20/50 | 134 | 47% | 46% | 52% | 52% | 0.27% |
| Phá đỉnh/đáy 20 nến | 170 | 47% | 45% | 48% | 52% | -0.03% |
| Nén Bollinger rồi bung | 30 | 47% | 60% | 67% | 52% | 0.38% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 141 | 52% | 49% | 60% | 52% | 2.61% |
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
| SMC: hồi về order block sau BOS | 100 | 55% | 47% | 46% | 52% | -1.06% |
| SMC: hồi về fair value gap | 77 | 52% | 44% | 53% | 52% | -0.07% |
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
| CK: bung kênh Keltner EMA20 ± 2 ATR | 120 | 53% | 53% | 57% | 52% | 2.05% |
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
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 146 | 26% | 0.00% | 1.00 | -15% | 44% | 54% | -14% |
| Cắt EMA20/50 | 206 | 24% | 0.17% | 1.07 | -27% | 53% | 54% | -34% |
| Phá đỉnh/đáy 20 nến | 214 | 28% | 0.30% | 1.14 | 15% | 63% | 54% | 2% |
| Nén Bollinger rồi bung | 69 | 35% | -0.08% | 0.97 | -16% | 50% | 54% | 33% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 147 | 29% | 0.34% | 1.23 | 35% | 46% | 54% | 22% |
| Volume profile: thoát vùng giá trị | 106 | 27% | 1.22% | 1.55 | 136% | 34% | 54% | 19% |
| Volume profile: hồi về POC | 204 | 30% | -0.11% | 0.91 | -29% | 43% | 54% | -9% |
| Volume profile: cắt EMA lọc theo POC | 283 | 19% | 0.14% | 1.09 | -16% | 46% | 54% | -22% |
| RSI14 qua 50 (chuẩn so sánh) | 725 | 22% | 0.02% | 1.02 | -35% | 69% | 54% | -26% |
| VP thoát vùng + RSI xác nhận | 159 | 33% | 0.39% | 1.22 | 37% | 25% | 54% | -4% |
| VP thoát vùng + RSI + khối lượng 1,5x | 99 | 27% | 1.20% | 1.53 | 124% | 29% | 54% | 25% |
| VP thoát vùng + RSI + ADX20 | 101 | 29% | 1.22% | 1.55 | 128% | 33% | 54% | 13% |
| VP hồi trong vùng + RSI 30/70 | 47 | 32% | -0.37% | 0.78 | -18% | 21% | 54% | -11% |
| Đồng thuận POC + EMA + RSI | 218 | 22% | 0.19% | 1.10 | -15% | 47% | 54% | -10% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 99 | 27% | 1.12% | 1.49 | 107% | 33% | 54% | 21% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 106 | 31% | 1.06% | 1.50 | 109% | 32% | 54% | 12% |
| SMC: cấu trúc BOS/CHoCH | 204 | 27% | 0.66% | 1.28 | 93% | 48% | 54% | -21% |
| SMC: hồi về order block sau BOS | 114 | 20% | -0.55% | 0.77 | -56% | 72% | 54% | -36% |
| SMC: hồi về fair value gap | 100 | 32% | 1.08% | 1.55 | 99% | 45% | 54% | -2% |
| SMC: quét thanh khoản đảo chiều | 239 | 36% | 0.02% | 1.01 | -19% | 51% | 54% | -11% |
| SMC: quét thanh khoản + displacement | 171 | 36% | 0.33% | 1.37 | 49% | 32% | 54% | 12% |
| PA: nến nhấn chìm theo EMA50 | 491 | 29% | -0.20% | 0.83 | -71% | 77% | 54% | -43% |
| PA: pin bar tại đỉnh/đáy swing | 111 | 32% | -0.25% | 0.86 | -31% | 43% | 54% | -4% |
| PA: phá đỉnh/đáy rồi retest | 104 | 12% | -0.22% | 0.85 | -29% | 48% | 54% | -28% |
| PA: inside bar theo xu hướng EMA | 95 | 29% | 1.53% | 1.72 | 186% | 46% | 54% | 47% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 387 | 64% | -0.02% | 0.98 | -17% | 49% | 54% | 15% |
| CK: cắt SMA50/200 (golden/death cross) | 84 | 27% | 2.32% | 1.99 | 284% | 49% | 54% | 61% |
| CK: MACD histogram + lọc EMA200 | 333 | 30% | 0.51% | 1.40 | 262% | 45% | 54% | -5% |
| CK: Supertrend 10/3 | 222 | 26% | 0.30% | 1.12 | -2% | 48% | 54% | -19% |
| CK: Parabolic SAR | 559 | 36% | -0.08% | 0.95 | -66% | 82% | 54% | -51% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 268 | 20% | 0.21% | 1.12 | -2% | 57% | 54% | 16% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 137 | 37% | 0.69% | 1.41 | 104% | 30% | 54% | -4% |
| CK: Bollinger hồi về trung bình + SMA200 | 160 | 61% | 0.45% | 1.33 | 85% | 41% | 54% | 24% |
| CK: Minervini trend template | 121 | 21% | 0.27% | 1.17 | 16% | 32% | 54% | -4% |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 48 | 21% | -0.45% | 0.80 | -25% | 46% | 54% | 10% |
| CK: Elder Triple Screen (khung cao + Force Index) | 187 | 33% | 0.33% | 1.17 | 14% | 43% | 54% | -8% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 129 | 28% | 1.20% | 1.59 | 154% | 47% | 54% | 32% |
| CK: Turtle Donchian 55/20 | 113 | 32% | 0.75% | 1.32 | 56% | 31% | 54% | 3% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 0 | | | | | | | |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 0 | | | | | | | |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 136 | 18% | -0.20% | 0.94 | -58% | 80% | 54% | -23% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 175 | 51% | 0.38% | 1.22 | 66% | 44% | 54% | 46% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 319 | 30% | 0.40% | 1.28 | 85% | 56% | 54% | 2% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 160 | 31% | 0.76% | 1.38 | 123% | 39% | 54% | 18% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 148 | 29% | 0.68% | 1.33 | 83% | 42% | 54% | 17% |

## SOL · 6569 nến 4h · 2023-10-18 đến 2026-10-17

| Chiến lược | Số tín hiệu | Đúng hướng 1d | 3d | 7d | Nền 7d | LN TB 7d |
|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 146 | 56% | 54% | 51% | 51% | 1.44% |
| Cắt EMA20/50 | 126 | 56% | 51% | 53% | 51% | 0.74% |
| Phá đỉnh/đáy 20 nến | 180 | 50% | 49% | 48% | 51% | 0.42% |
| Nén Bollinger rồi bung | 33 | 48% | 39% | 45% | 51% | -0.12% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 141 | 56% | 53% | 49% | 51% | 1.52% |
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
| SMC: hồi về order block sau BOS | 118 | 44% | 50% | 53% | 51% | 0.29% |
| SMC: hồi về fair value gap | 78 | 45% | 53% | 50% | 51% | -0.15% |
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
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 150 | 41% | 0.31% | 1.21 | 30% | 42% | 342% | 4% |
| Cắt EMA20/50 | 176 | 34% | 1.14% | 1.47 | 208% | 46% | 342% | 9% |
| Phá đỉnh/đáy 20 nến | 223 | 35% | 0.21% | 1.08 | -15% | 66% | 342% | 17% |
| Nén Bollinger rồi bung | 84 | 32% | -0.03% | 0.99 | -21% | 53% | 342% | -31% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 144 | 35% | 0.30% | 1.18 | 23% | 55% | 342% | 17% |
| Volume profile: thoát vùng giá trị | 93 | 35% | 1.81% | 1.63 | 185% | 38% | 342% | 58% |
| Volume profile: hồi về POC | 187 | 34% | -0.18% | 0.88 | -37% | 51% | 342% | -14% |
| Volume profile: cắt EMA lọc theo POC | 244 | 27% | 0.64% | 1.36 | 139% | 46% | 342% | 1% |
| RSI14 qua 50 (chuẩn so sánh) | 764 | 21% | -0.00% | 1.00 | -58% | 79% | 342% | -14% |
| VP thoát vùng + RSI xác nhận | 160 | 34% | 0.39% | 1.18 | 27% | 36% | 342% | 40% |
| VP thoát vùng + RSI + khối lượng 1,5x | 90 | 33% | 1.61% | 1.59 | 140% | 40% | 342% | 17% |
| VP thoát vùng + RSI + ADX20 | 92 | 35% | 1.49% | 1.51 | 114% | 44% | 342% | 51% |
| VP hồi trong vùng + RSI 30/70 | 45 | 47% | 0.86% | 1.52 | 37% | 19% | 342% | 50% |
| Đồng thuận POC + EMA + RSI | 185 | 26% | 0.89% | 1.42 | 159% | 46% | 342% | 1% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 90 | 33% | 1.44% | 1.52 | 110% | 44% | 342% | 17% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 88 | 36% | 1.37% | 1.54 | 121% | 30% | 342% | 32% |
| SMC: cấu trúc BOS/CHoCH | 224 | 34% | 0.46% | 1.16 | 18% | 79% | 342% | -32% |
| SMC: hồi về order block sau BOS | 134 | 31% | 0.50% | 1.18 | 17% | 57% | 342% | -4% |
| SMC: hồi về fair value gap | 103 | 26% | 0.02% | 1.01 | -28% | 79% | 342% | -16% |
| SMC: quét thanh khoản đảo chiều | 255 | 33% | -0.18% | 0.92 | -59% | 79% | 342% | 47% |
| SMC: quét thanh khoản + displacement | 207 | 50% | 0.51% | 1.64 | 135% | 31% | 342% | 60% |
| PA: nến nhấn chìm theo EMA50 | 487 | 34% | 0.07% | 1.05 | -15% | 52% | 342% | -14% |
| PA: pin bar tại đỉnh/đáy swing | 77 | 39% | 0.70% | 1.29 | 39% | 43% | 342% | 19% |
| PA: phá đỉnh/đáy rồi retest | 149 | 18% | 0.21% | 1.13 | -0% | 57% | 342% | -5% |
| PA: inside bar theo xu hướng EMA | 101 | 29% | 1.02% | 1.38 | 70% | 47% | 342% | 3% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 349 | 64% | 0.03% | 1.02 | -5% | 37% | 342% | -5% |
| CK: cắt SMA50/200 (golden/death cross) | 85 | 32% | 2.59% | 1.80 | 269% | 58% | 342% | 81% |
| CK: MACD histogram + lọc EMA200 | 373 | 30% | 0.19% | 1.12 | 28% | 55% | 342% | -16% |
| CK: Supertrend 10/3 | 211 | 29% | 0.47% | 1.16 | -5% | 68% | 342% | -46% |
| CK: Parabolic SAR | 577 | 40% | 0.04% | 1.02 | -48% | 79% | 342% | -34% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 256 | 22% | 0.24% | 1.12 | -0% | 58% | 342% | -26% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 141 | 38% | 0.38% | 1.16 | 22% | 45% | 342% | -10% |
| CK: Bollinger hồi về trung bình + SMA200 | 162 | 56% | 0.13% | 1.06 | -1% | 61% | 342% | 10% |
| CK: Minervini trend template | 155 | 23% | -0.21% | 0.90 | -45% | 63% | 342% | -6% |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 26 | 31% | 0.86% | 1.40 | 18% | 33% | 342% | -1% |
| CK: Elder Triple Screen (khung cao + Force Index) | 181 | 33% | 0.85% | 1.36 | 91% | 61% | 342% | -1% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 135 | 33% | 1.43% | 1.57 | 61% | 65% | 342% | 16% |
| CK: Turtle Donchian 55/20 | 112 | 36% | 1.20% | 1.44 | 148% | 47% | 342% | 23% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 0 | | | | | | | |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 0 | | | | | | | |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 112 | 25% | 0.93% | 1.23 | 35% | 67% | 342% | 63% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 171 | 56% | 0.65% | 1.30 | 130% | 49% | 342% | 32% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 293 | 35% | 0.51% | 1.29 | 98% | 65% | 342% | 58% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 153 | 32% | 0.96% | 1.39 | 99% | 51% | 342% | -12% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 131 | 32% | 1.05% | 1.40 | 88% | 56% | 342% | -4% |
