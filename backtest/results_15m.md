# Kết quả backtest dự đoán xu hướng · khung 15m

## BTC · 35039 nến 15m · 2025-10-17 đến 2026-10-17

| Chiến lược | Số tín hiệu | Đúng hướng 1 giờ | 4 giờ | 1 ngày | Nền 1 ngày | LN TB 1 ngày |
|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 609 | 48% | 49% | 50% | 51% | 0.20% |
| Cắt EMA20/50 | 670 | 47% | 51% | 51% | 51% | 0.02% |
| Phá đỉnh/đáy 20 nến | 1082 | 44% | 45% | 48% | 51% | -0.05% |
| Nén Bollinger rồi bung | 133 | 42% | 38% | 47% | 51% | -0.10% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 563 | 46% | 45% | 48% | 51% | 0.15% |
| Volume profile: thoát vùng giá trị | 372 | 42% | 47% | 52% | 51% | 0.11% |
| Volume profile: hồi về POC | 1142 | 47% | 52% | 49% | 51% | -0.18% |
| Volume profile: cắt EMA lọc theo POC | 1331 | 46% | 47% | 50% | 51% | 0.01% |
| RSI14 qua 50 (chuẩn so sánh) | 4210 | 48% | 49% | 49% | 51% | -0.01% |
| VP thoát vùng + RSI xác nhận | 777 | 45% | 47% | 50% | 51% | 0.09% |
| VP thoát vùng + RSI + khối lượng 1,5x | 340 | 44% | 47% | 53% | 51% | 0.15% |
| VP thoát vùng + RSI + ADX20 | 340 | 45% | 47% | 51% | 51% | 0.12% |
| VP hồi trong vùng + RSI 30/70 | 178 | 59% | 59% | 53% | 51% | -0.12% |
| Đồng thuận POC + EMA + RSI | 1011 | 45% | 47% | 48% | 51% | -0.05% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 325 | 44% | 49% | 53% | 51% | 0.12% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 345 | 44% | 49% | 52% | 51% | 0.12% |
| SMC: cấu trúc BOS/CHoCH | 862 | 46% | 45% | 49% | 51% | -0.02% |
| SMC: hồi về order block sau BOS | 638 | 48% | 46% | 50% | 51% | 0.05% |
| SMC: hồi về fair value gap | 417 | 52% | 49% | 49% | 51% | 0.07% |
| SMC: quét thanh khoản đảo chiều | 1286 | 52% | 54% | 52% | 51% | 0.05% |
| SMC: quét thanh khoản + displacement | 1034 | 53% | 50% | 51% | 51% | 0.01% |
| PA: nến nhấn chìm theo EMA50 | 2564 | 47% | 47% | 51% | 51% | 0.04% |
| PA: pin bar tại đỉnh/đáy swing | 1080 | 50% | 50% | 51% | 51% | 0.03% |
| PA: phá đỉnh/đáy rồi retest | 840 | 46% | 45% | 50% | 51% | 0.06% |
| PA: inside bar theo xu hướng EMA | 471 | 46% | 44% | 48% | 51% | -0.06% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 1467 | 53% | 52% | 48% | 51% | -0.01% |
| CK: cắt SMA50/200 (golden/death cross) | 225 | 42% | 43% | 49% | 51% | 0.02% |
| CK: MACD histogram + lọc EMA200 | 2059 | 47% | 47% | 47% | 51% | 0.02% |
| CK: Supertrend 10/3 | 810 | 45% | 47% | 50% | 51% | -0.01% |
| CK: Parabolic SAR | 2836 | 50% | 49% | 49% | 51% | -0.02% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 1373 | 49% | 49% | 51% | 51% | 0.09% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 710 | 45% | 48% | 48% | 51% | 0.07% |
| CK: Bollinger hồi về trung bình + SMA200 | 471 | 52% | 56% | 51% | 51% | 0.03% |
| CK: Minervini trend template | 0 | - | - | - | 51% | - |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 195 | 40% | 41% | 44% | 51% | -0.05% |
| CK: Elder Triple Screen (khung cao + Force Index) | 335 | 46% | 47% | 49% | 51% | 0.00% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 190 | 40% | 39% | 45% | 51% | -0.13% |
| CK: Turtle Donchian 55/20 | 479 | 47% | 47% | 49% | 51% | -0.00% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 871 | 46% | 45% | 49% | 51% | -0.03% |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 1069 | 54% | 54% | 53% | 51% | 0.14% |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 432 | 46% | 49% | 48% | 51% | -0.12% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 470 | 55% | 54% | 50% | 51% | 0.05% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 1722 | 49% | 50% | 50% | 51% | -0.01% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 550 | 44% | 45% | 46% | 51% | -0.08% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 424 | 42% | 40% | 45% | 51% | -0.09% |

| Chiến lược | Số lệnh | Thắng | LN/lệnh | Profit factor | Tổng LN cả kỳ | Sụt giảm tối đa | Mua và giữ | Tổng LN 3 tháng |
|---|---|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 667 | 20% | -0.10% | 0.66 | -50% | 50% | -24% | -7% |
| Cắt EMA20/50 | 1250 | 18% | -0.08% | 0.79 | -65% | 66% | -24% | -19% |
| Phá đỉnh/đáy 20 nến | 1662 | 21% | -0.14% | 0.61 | -92% | 92% | -24% | -45% |
| Nén Bollinger rồi bung | 562 | 21% | -0.13% | 0.66 | -52% | 55% | -24% | -23% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 655 | 22% | -0.10% | 0.69 | -48% | 49% | -24% | -9% |
| Volume profile: thoát vùng giá trị | 696 | 20% | -0.02% | 0.94 | -20% | 31% | -24% | -14% |
| Volume profile: hồi về POC | 1242 | 26% | -0.12% | 0.57 | -79% | 79% | -24% | -27% |
| Volume profile: cắt EMA lọc theo POC | 1557 | 15% | -0.08% | 0.72 | -75% | 76% | -24% | -34% |
| RSI14 qua 50 (chuẩn so sánh) | 4295 | 15% | -0.11% | 0.54 | -99% | 99% | -24% | -70% |
| VP thoát vùng + RSI xác nhận | 958 | 24% | -0.08% | 0.77 | -54% | 57% | -24% | -19% |
| VP thoát vùng + RSI + khối lượng 1,5x | 664 | 20% | -0.02% | 0.95 | -18% | 28% | -24% | -13% |
| VP thoát vùng + RSI + ADX20 | 674 | 20% | -0.04% | 0.90 | -29% | 40% | -24% | -13% |
| VP hồi trong vùng + RSI 30/70 | 247 | 31% | -0.11% | 0.67 | -23% | 25% | -24% | -6% |
| Đồng thuận POC + EMA + RSI | 1283 | 16% | -0.08% | 0.76 | -69% | 69% | -24% | -29% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 655 | 19% | -0.02% | 0.95 | -18% | 27% | -24% | -11% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 669 | 21% | -0.02% | 0.95 | -18% | 29% | -24% | -10% |
| SMC: cấu trúc BOS/CHoCH | 1576 | 19% | -0.12% | 0.69 | -86% | 86% | -24% | -46% |
| SMC: hồi về order block sau BOS | 855 | 19% | -0.10% | 0.73 | -60% | 62% | -24% | -24% |
| SMC: hồi về fair value gap | 653 | 17% | -0.10% | 0.73 | -51% | 53% | -24% | -19% |
| SMC: quét thanh khoản đảo chiều | 1495 | 29% | -0.12% | 0.65 | -83% | 84% | -24% | -29% |
| SMC: quét thanh khoản + displacement | 1130 | 22% | -0.09% | 0.56 | -65% | 66% | -24% | -27% |
| PA: nến nhấn chìm theo EMA50 | 2793 | 22% | -0.11% | 0.57 | -95% | 95% | -24% | -45% |
| PA: pin bar tại đỉnh/đáy swing | 1167 | 26% | -0.14% | 0.51 | -82% | 82% | -24% | -35% |
| PA: phá đỉnh/đáy rồi retest | 873 | 11% | -0.11% | 0.63 | -62% | 64% | -24% | -23% |
| PA: inside bar theo xu hướng EMA | 647 | 18% | -0.07% | 0.81 | -41% | 46% | -24% | -4% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 1980 | 46% | -0.07% | 0.56 | -77% | 77% | -24% | -33% |
| CK: cắt SMA50/200 (golden/death cross) | 796 | 20% | -0.09% | 0.80 | -55% | 55% | -24% | -23% |
| CK: MACD histogram + lọc EMA200 | 2246 | 21% | -0.09% | 0.65 | -89% | 89% | -24% | -50% |
| CK: Supertrend 10/3 | 1420 | 21% | -0.07% | 0.81 | -67% | 70% | -24% | -18% |
| CK: Parabolic SAR | 3438 | 27% | -0.11% | 0.65 | -98% | 98% | -24% | -63% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 1599 | 17% | -0.09% | 0.70 | -79% | 80% | -24% | -24% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 981 | 23% | -0.11% | 0.69 | -66% | 67% | -24% | -19% |
| CK: Bollinger hồi về trung bình + SMA200 | 938 | 47% | -0.07% | 0.74 | -49% | 50% | -24% | -17% |
| CK: Minervini trend template | 0 | | | | | | | |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 290 | 20% | -0.09% | 0.72 | -23% | 24% | -24% | -7% |
| CK: Elder Triple Screen (khung cao + Force Index) | 880 | 20% | -0.14% | 0.64 | -74% | 74% | -24% | -22% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 588 | 17% | -0.16% | 0.64 | -64% | 66% | -24% | -5% |
| CK: Turtle Donchian 55/20 | 897 | 19% | -0.11% | 0.74 | -64% | 67% | -24% | -8% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 1529 | 19% | -0.11% | 0.72 | -83% | 83% | -24% | -32% |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 2220 | 41% | -0.10% | 0.69 | -89% | 89% | -24% | -45% |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 973 | 17% | -0.15% | 0.70 | -79% | 79% | -24% | -27% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 1084 | 42% | -0.07% | 0.79 | -53% | 55% | -24% | -19% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 2080 | 18% | -0.08% | 0.69 | -83% | 83% | -24% | -35% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 884 | 20% | -0.09% | 0.77 | -56% | 60% | -24% | -9% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 737 | 19% | -0.11% | 0.73 | -57% | 60% | -24% | -9% |

## ETH · 35039 nến 15m · 2025-10-17 đến 2026-10-17

| Chiến lược | Số tín hiệu | Đúng hướng 1 giờ | 4 giờ | 1 ngày | Nền 1 ngày | LN TB 1 ngày |
|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 612 | 49% | 47% | 48% | 51% | 0.19% |
| Cắt EMA20/50 | 730 | 43% | 47% | 48% | 51% | 0.01% |
| Phá đỉnh/đáy 20 nến | 1004 | 42% | 45% | 49% | 51% | 0.03% |
| Nén Bollinger rồi bung | 125 | 42% | 41% | 45% | 51% | -0.14% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 609 | 45% | 48% | 46% | 51% | 0.05% |
| Volume profile: thoát vùng giá trị | 354 | 45% | 49% | 51% | 51% | 0.24% |
| Volume profile: hồi về POC | 980 | 51% | 54% | 52% | 51% | -0.11% |
| Volume profile: cắt EMA lọc theo POC | 1359 | 47% | 47% | 47% | 51% | 0.09% |
| RSI14 qua 50 (chuẩn so sánh) | 4304 | 49% | 49% | 49% | 51% | -0.01% |
| VP thoát vùng + RSI xác nhận | 751 | 46% | 47% | 47% | 51% | 0.15% |
| VP thoát vùng + RSI + khối lượng 1,5x | 334 | 42% | 47% | 52% | 51% | 0.23% |
| VP thoát vùng + RSI + ADX20 | 329 | 46% | 48% | 50% | 51% | 0.25% |
| VP hồi trong vùng + RSI 30/70 | 157 | 61% | 58% | 50% | 51% | 0.07% |
| Đồng thuận POC + EMA + RSI | 1044 | 45% | 46% | 48% | 51% | 0.06% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 327 | 43% | 47% | 51% | 51% | 0.19% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 357 | 44% | 47% | 50% | 51% | 0.13% |
| SMC: cấu trúc BOS/CHoCH | 869 | 44% | 45% | 48% | 51% | -0.09% |
| SMC: hồi về order block sau BOS | 650 | 45% | 45% | 48% | 51% | -0.08% |
| SMC: hồi về fair value gap | 394 | 52% | 49% | 49% | 51% | 0.11% |
| SMC: quét thanh khoản đảo chiều | 1152 | 53% | 52% | 49% | 51% | -0.11% |
| SMC: quét thanh khoản + displacement | 1021 | 53% | 51% | 49% | 51% | -0.06% |
| PA: nến nhấn chìm theo EMA50 | 2573 | 47% | 46% | 47% | 51% | -0.00% |
| PA: pin bar tại đỉnh/đáy swing | 898 | 52% | 52% | 51% | 51% | -0.09% |
| PA: phá đỉnh/đáy rồi retest | 828 | 45% | 45% | 47% | 51% | -0.09% |
| PA: inside bar theo xu hướng EMA | 492 | 46% | 46% | 48% | 51% | -0.11% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 1429 | 53% | 51% | 47% | 51% | -0.08% |
| CK: cắt SMA50/200 (golden/death cross) | 223 | 48% | 46% | 47% | 51% | -0.09% |
| CK: MACD histogram + lọc EMA200 | 2101 | 47% | 47% | 49% | 51% | 0.03% |
| CK: Supertrend 10/3 | 772 | 44% | 47% | 48% | 51% | -0.01% |
| CK: Parabolic SAR | 2672 | 47% | 49% | 50% | 51% | 0.01% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 1476 | 46% | 47% | 48% | 51% | -0.03% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 645 | 43% | 47% | 49% | 51% | 0.04% |
| CK: Bollinger hồi về trung bình + SMA200 | 464 | 58% | 57% | 51% | 51% | 0.07% |
| CK: Minervini trend template | 1 | 0% | 100% | 100% | 51% | 2.00% |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 182 | 46% | 51% | 52% | 51% | 0.00% |
| CK: Elder Triple Screen (khung cao + Force Index) | 345 | 42% | 45% | 47% | 51% | -0.07% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 222 | 44% | 40% | 45% | 51% | -0.31% |
| CK: Turtle Donchian 55/20 | 422 | 41% | 46% | 48% | 51% | 0.00% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 853 | 43% | 47% | 48% | 51% | -0.10% |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 993 | 55% | 52% | 50% | 51% | -0.02% |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 378 | 45% | 48% | 52% | 51% | -0.04% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 467 | 52% | 55% | 48% | 51% | 0.09% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 1802 | 47% | 48% | 49% | 51% | -0.01% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 550 | 42% | 45% | 45% | 51% | -0.17% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 422 | 42% | 43% | 43% | 51% | -0.29% |

| Chiến lược | Số lệnh | Thắng | LN/lệnh | Profit factor | Tổng LN cả kỳ | Sụt giảm tối đa | Mua và giữ | Tổng LN 3 tháng |
|---|---|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 669 | 22% | -0.08% | 0.79 | -43% | 45% | -37% | -11% |
| Cắt EMA20/50 | 1359 | 19% | -0.09% | 0.81 | -75% | 76% | -37% | -41% |
| Phá đỉnh/đáy 20 nến | 1591 | 22% | -0.17% | 0.66 | -94% | 94% | -37% | -44% |
| Nén Bollinger rồi bung | 536 | 20% | -0.14% | 0.71 | -55% | 59% | -37% | -15% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 684 | 22% | -0.08% | 0.79 | -45% | 49% | -37% | -20% |
| Volume profile: thoát vùng giá trị | 706 | 20% | -0.01% | 0.98 | -17% | 29% | -37% | -12% |
| Volume profile: hồi về POC | 1061 | 31% | -0.09% | 0.73 | -64% | 67% | -37% | -13% |
| Volume profile: cắt EMA lọc theo POC | 1591 | 15% | -0.09% | 0.76 | -80% | 81% | -37% | -43% |
| RSI14 qua 50 (chuẩn so sánh) | 4386 | 15% | -0.11% | 0.61 | -99% | 99% | -37% | -70% |
| VP thoát vùng + RSI xác nhận | 920 | 22% | -0.08% | 0.82 | -56% | 60% | -37% | -22% |
| VP thoát vùng + RSI + khối lượng 1,5x | 703 | 20% | -0.02% | 0.96 | -22% | 28% | -37% | -13% |
| VP thoát vùng + RSI + ADX20 | 684 | 20% | -0.02% | 0.95 | -25% | 28% | -37% | -14% |
| VP hồi trong vùng + RSI 30/70 | 208 | 33% | -0.08% | 0.80 | -17% | 18% | -37% | -4% |
| Đồng thuận POC + EMA + RSI | 1316 | 16% | -0.10% | 0.78 | -75% | 76% | -37% | -36% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 700 | 19% | -0.02% | 0.96 | -24% | 30% | -37% | -12% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 723 | 20% | -0.04% | 0.92 | -34% | 41% | -37% | -17% |
| SMC: cấu trúc BOS/CHoCH | 1607 | 19% | -0.17% | 0.68 | -94% | 95% | -37% | -47% |
| SMC: hồi về order block sau BOS | 899 | 18% | -0.19% | 0.62 | -84% | 84% | -37% | -38% |
| SMC: hồi về fair value gap | 578 | 21% | -0.04% | 0.91 | -27% | 28% | -37% | -12% |
| SMC: quét thanh khoản đảo chiều | 1357 | 31% | -0.07% | 0.84 | -65% | 66% | -37% | -40% |
| SMC: quét thanh khoản + displacement | 1133 | 24% | -0.09% | 0.64 | -67% | 67% | -37% | -29% |
| PA: nến nhấn chìm theo EMA50 | 2773 | 24% | -0.10% | 0.67 | -94% | 94% | -37% | -53% |
| PA: pin bar tại đỉnh/đáy swing | 1001 | 29% | -0.14% | 0.63 | -76% | 76% | -37% | -34% |
| PA: phá đỉnh/đáy rồi retest | 857 | 11% | -0.14% | 0.63 | -71% | 71% | -37% | -33% |
| PA: inside bar theo xu hướng EMA | 698 | 17% | -0.04% | 0.91 | -36% | 41% | -37% | -14% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 1941 | 50% | -0.09% | 0.62 | -82% | 82% | -37% | -32% |
| CK: cắt SMA50/200 (golden/death cross) | 775 | 21% | -0.11% | 0.80 | -63% | 73% | -37% | -24% |
| CK: MACD histogram + lọc EMA200 | 2292 | 22% | -0.09% | 0.72 | -89% | 91% | -37% | -53% |
| CK: Supertrend 10/3 | 1370 | 21% | -0.10% | 0.82 | -78% | 80% | -37% | -32% |
| CK: Parabolic SAR | 3250 | 30% | -0.08% | 0.79 | -94% | 95% | -37% | -45% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 1692 | 16% | -0.11% | 0.73 | -86% | 87% | -37% | -43% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 906 | 24% | -0.12% | 0.73 | -69% | 72% | -37% | -21% |
| CK: Bollinger hồi về trung bình + SMA200 | 891 | 49% | -0.08% | 0.78 | -51% | 53% | -37% | -21% |
| CK: Minervini trend template | 2 | 50% | 0.95% | 2.98 | 2% | 1% | -37% | 2% |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 261 | 24% | -0.12% | 0.70 | -27% | 30% | -37% | -17% |
| CK: Elder Triple Screen (khung cao + Force Index) | 908 | 22% | -0.15% | 0.70 | -78% | 79% | -37% | -30% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 664 | 19% | -0.17% | 0.68 | -71% | 73% | -37% | -41% |
| CK: Turtle Donchian 55/20 | 814 | 21% | -0.10% | 0.81 | -61% | 62% | -37% | -19% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 1488 | 20% | -0.12% | 0.77 | -85% | 86% | -37% | -36% |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 2035 | 42% | -0.12% | 0.72 | -92% | 92% | -37% | -51% |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 865 | 18% | -0.13% | 0.81 | -72% | 76% | -37% | -17% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 1076 | 42% | -0.07% | 0.83 | -54% | 58% | -37% | -32% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 2180 | 19% | -0.10% | 0.71 | -90% | 91% | -37% | -51% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 912 | 20% | -0.12% | 0.75 | -71% | 73% | -37% | -37% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 734 | 20% | -0.11% | 0.79 | -59% | 61% | -37% | -29% |

## SOL · 35039 nến 15m · 2025-10-17 đến 2026-10-17

| Chiến lược | Số tín hiệu | Đúng hướng 1 giờ | 4 giờ | 1 ngày | Nền 1 ngày | LN TB 1 ngày |
|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 630 | 49% | 48% | 49% | 51% | 0.23% |
| Cắt EMA20/50 | 702 | 46% | 46% | 50% | 51% | -0.06% |
| Phá đỉnh/đáy 20 nến | 1011 | 45% | 48% | 48% | 51% | -0.02% |
| Nén Bollinger rồi bung | 130 | 46% | 42% | 47% | 51% | -0.08% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 599 | 47% | 48% | 49% | 51% | 0.00% |
| Volume profile: thoát vùng giá trị | 375 | 47% | 52% | 50% | 51% | 0.10% |
| Volume profile: hồi về POC | 1096 | 49% | 47% | 51% | 51% | -0.09% |
| Volume profile: cắt EMA lọc theo POC | 1386 | 47% | 49% | 48% | 51% | -0.10% |
| RSI14 qua 50 (chuẩn so sánh) | 4222 | 49% | 50% | 50% | 51% | -0.00% |
| VP thoát vùng + RSI xác nhận | 802 | 50% | 51% | 48% | 51% | 0.16% |
| VP thoát vùng + RSI + khối lượng 1,5x | 346 | 44% | 52% | 50% | 51% | 0.06% |
| VP thoát vùng + RSI + ADX20 | 345 | 46% | 51% | 50% | 51% | 0.05% |
| VP hồi trong vùng + RSI 30/70 | 170 | 58% | 57% | 52% | 51% | 0.25% |
| Đồng thuận POC + EMA + RSI | 1041 | 45% | 47% | 48% | 51% | -0.09% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 331 | 45% | 52% | 50% | 51% | 0.03% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 349 | 44% | 51% | 49% | 51% | 0.00% |
| SMC: cấu trúc BOS/CHoCH | 855 | 48% | 46% | 48% | 51% | 0.03% |
| SMC: hồi về order block sau BOS | 603 | 49% | 46% | 50% | 51% | -0.02% |
| SMC: hồi về fair value gap | 415 | 46% | 48% | 46% | 51% | -0.22% |
| SMC: quét thanh khoản đảo chiều | 1273 | 51% | 51% | 49% | 51% | -0.20% |
| SMC: quét thanh khoản + displacement | 1048 | 50% | 51% | 49% | 51% | -0.19% |
| PA: nến nhấn chìm theo EMA50 | 2512 | 47% | 49% | 49% | 51% | -0.07% |
| PA: pin bar tại đỉnh/đáy swing | 881 | 48% | 49% | 48% | 51% | -0.19% |
| PA: phá đỉnh/đáy rồi retest | 774 | 50% | 48% | 51% | 51% | 0.10% |
| PA: inside bar theo xu hướng EMA | 466 | 46% | 51% | 49% | 51% | 0.04% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 1491 | 52% | 50% | 48% | 51% | -0.11% |
| CK: cắt SMA50/200 (golden/death cross) | 221 | 52% | 51% | 46% | 51% | -0.13% |
| CK: MACD histogram + lọc EMA200 | 2053 | 48% | 48% | 48% | 51% | 0.03% |
| CK: Supertrend 10/3 | 796 | 47% | 49% | 49% | 51% | -0.00% |
| CK: Parabolic SAR | 2874 | 47% | 49% | 50% | 51% | -0.01% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 1351 | 50% | 49% | 49% | 51% | -0.02% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 689 | 44% | 46% | 48% | 51% | -0.00% |
| CK: Bollinger hồi về trung bình + SMA200 | 469 | 48% | 51% | 48% | 51% | -0.01% |
| CK: Minervini trend template | 2 | 0% | 0% | 0% | 51% | -12.37% |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 144 | 40% | 38% | 53% | 51% | 0.02% |
| CK: Elder Triple Screen (khung cao + Force Index) | 320 | 46% | 45% | 47% | 51% | -0.14% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 208 | 48% | 48% | 49% | 51% | -0.07% |
| CK: Turtle Donchian 55/20 | 472 | 47% | 49% | 47% | 51% | -0.19% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 881 | 48% | 47% | 48% | 51% | -0.08% |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 1123 | 53% | 56% | 52% | 51% | 0.16% |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 436 | 49% | 50% | 49% | 51% | -0.08% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 487 | 53% | 52% | 47% | 51% | -0.04% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 1704 | 48% | 49% | 51% | 51% | 0.01% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 553 | 44% | 46% | 47% | 51% | -0.07% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 425 | 43% | 47% | 46% | 51% | -0.01% |

| Chiến lược | Số lệnh | Thắng | LN/lệnh | Profit factor | Tổng LN cả kỳ | Sụt giảm tối đa | Mua và giữ | Tổng LN 3 tháng |
|---|---|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 694 | 24% | -0.10% | 0.75 | -51% | 59% | -44% | 6% |
| Cắt EMA20/50 | 1342 | 19% | -0.11% | 0.80 | -81% | 81% | -44% | -26% |
| Phá đỉnh/đáy 20 nến | 1527 | 24% | -0.09% | 0.82 | -79% | 82% | -44% | -37% |
| Nén Bollinger rồi bung | 563 | 20% | -0.13% | 0.77 | -55% | 59% | -44% | -29% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 699 | 22% | -0.14% | 0.68 | -64% | 68% | -44% | 7% |
| Volume profile: thoát vùng giá trị | 725 | 20% | -0.04% | 0.94 | -32% | 48% | -44% | 1% |
| Volume profile: hồi về POC | 1179 | 30% | -0.11% | 0.71 | -74% | 75% | -44% | -26% |
| Volume profile: cắt EMA lọc theo POC | 1618 | 17% | -0.10% | 0.75 | -84% | 84% | -44% | -34% |
| RSI14 qua 50 (chuẩn so sánh) | 4290 | 18% | -0.11% | 0.66 | -99% | 99% | -44% | -77% |
| VP thoát vùng + RSI xác nhận | 969 | 25% | -0.10% | 0.79 | -65% | 66% | -44% | -21% |
| VP thoát vùng + RSI + khối lượng 1,5x | 701 | 21% | -0.04% | 0.93 | -33% | 52% | -44% | 3% |
| VP thoát vùng + RSI + ADX20 | 686 | 21% | -0.05% | 0.92 | -35% | 51% | -44% | -2% |
| VP hồi trong vùng + RSI 30/70 | 207 | 39% | -0.01% | 0.98 | -3% | 11% | -44% | -8% |
| Đồng thuận POC + EMA + RSI | 1337 | 18% | -0.10% | 0.79 | -79% | 79% | -44% | -27% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 673 | 21% | -0.04% | 0.93 | -31% | 46% | -44% | 3% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 666 | 23% | -0.01% | 0.98 | -17% | 35% | -44% | 0% |
| SMC: cấu trúc BOS/CHoCH | 1506 | 21% | -0.07% | 0.87 | -71% | 73% | -44% | -46% |
| SMC: hồi về order block sau BOS | 818 | 21% | -0.07% | 0.85 | -51% | 60% | -44% | -19% |
| SMC: hồi về fair value gap | 639 | 20% | -0.10% | 0.81 | -50% | 58% | -44% | -9% |
| SMC: quét thanh khoản đảo chiều | 1450 | 30% | -0.16% | 0.67 | -91% | 91% | -44% | -18% |
| SMC: quét thanh khoản + displacement | 1162 | 28% | -0.09% | 0.71 | -65% | 69% | -44% | -16% |
| PA: nến nhấn chìm theo EMA50 | 2723 | 26% | -0.09% | 0.73 | -92% | 92% | -44% | -53% |
| PA: pin bar tại đỉnh/đáy swing | 971 | 27% | -0.20% | 0.55 | -86% | 87% | -44% | -29% |
| PA: phá đỉnh/đáy rồi retest | 797 | 13% | -0.11% | 0.73 | -60% | 62% | -44% | -14% |
| PA: inside bar theo xu hướng EMA | 639 | 18% | -0.05% | 0.92 | -35% | 58% | -44% | 29% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 2053 | 53% | -0.08% | 0.67 | -81% | 81% | -44% | -32% |
| CK: cắt SMA50/200 (golden/death cross) | 790 | 23% | -0.13% | 0.79 | -69% | 75% | -44% | -7% |
| CK: MACD histogram + lọc EMA200 | 2239 | 23% | -0.10% | 0.74 | -91% | 93% | -44% | -47% |
| CK: Supertrend 10/3 | 1379 | 22% | -0.05% | 0.90 | -62% | 68% | -44% | -24% |
| CK: Parabolic SAR | 3499 | 29% | -0.12% | 0.73 | -99% | 99% | -44% | -65% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 1561 | 18% | -0.08% | 0.82 | -76% | 77% | -44% | -29% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 958 | 24% | -0.14% | 0.72 | -75% | 76% | -44% | -28% |
| CK: Bollinger hồi về trung bình + SMA200 | 940 | 48% | -0.11% | 0.74 | -64% | 65% | -44% | -16% |
| CK: Minervini trend template | 4 | 0% | -2.95% | 0.00 | -11% | 11% | -44% | -1% |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 199 | 22% | -0.18% | 0.63 | -31% | 32% | -44% | -12% |
| CK: Elder Triple Screen (khung cao + Force Index) | 860 | 23% | -0.14% | 0.75 | -75% | 75% | -44% | -16% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 573 | 22% | -0.09% | 0.84 | -51% | 66% | -44% | 23% |
| CK: Turtle Donchian 55/20 | 863 | 20% | -0.08% | 0.86 | -57% | 61% | -44% | -12% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 1528 | 20% | -0.13% | 0.78 | -88% | 89% | -44% | -11% |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 2230 | 45% | -0.08% | 0.82 | -85% | 86% | -44% | -45% |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 907 | 17% | -0.11% | 0.84 | -70% | 79% | -44% | 20% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 1114 | 43% | -0.08% | 0.83 | -61% | 61% | -44% | -21% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 2060 | 20% | -0.11% | 0.73 | -91% | 91% | -44% | -21% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 870 | 22% | -0.07% | 0.86 | -53% | 62% | -44% | -3% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 717 | 23% | -0.06% | 0.89 | -42% | 54% | -44% | 10% |
