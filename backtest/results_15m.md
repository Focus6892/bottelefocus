# Kết quả backtest dự đoán xu hướng · khung 15m

## BTC · 35039 nến 15m · 2025-10-17 đến 2026-10-17

| Chiến lược | Số tín hiệu | Đúng hướng 1 giờ | 4 giờ | 1 ngày | Nền 1 ngày | LN TB 1 ngày |
|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 605 | 46% | 48% | 49% | 51% | 0.20% |
| Cắt EMA20/50 | 670 | 47% | 51% | 51% | 51% | 0.02% |
| Phá đỉnh/đáy 20 nến | 1082 | 44% | 45% | 48% | 51% | -0.05% |
| Nén Bollinger rồi bung | 133 | 42% | 38% | 47% | 51% | -0.10% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 560 | 44% | 45% | 48% | 51% | 0.14% |
| Volume profile: thoát vùng giá trị | 372 | 42% | 47% | 52% | 51% | 0.11% |
| Volume profile: hồi về POC | 1142 | 47% | 52% | 49% | 51% | -0.18% |
| Volume profile: cắt EMA lọc theo POC | 1331 | 46% | 47% | 50% | 51% | 0.01% |
| RSI14 qua 50 (chuẩn so sánh) | 4210 | 48% | 49% | 49% | 51% | -0.01% |
| VP thoát vùng + RSI xác nhận | 777 | 45% | 47% | 50% | 51% | 0.09% |
| VP thoát vùng + RSI + khối lượng 1,5x | 340 | 44% | 47% | 53% | 51% | 0.15% |
| VP thoát vùng + RSI + ADX20 | 340 | 45% | 47% | 51% | 51% | 0.12% |
| VP hồi trong vùng + RSI 30/70 | 179 | 59% | 59% | 53% | 51% | -0.12% |
| Đồng thuận POC + EMA + RSI | 1011 | 45% | 47% | 48% | 51% | -0.05% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 325 | 44% | 49% | 53% | 51% | 0.12% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 345 | 44% | 49% | 52% | 51% | 0.12% |
| SMC: cấu trúc BOS/CHoCH | 862 | 46% | 45% | 49% | 51% | -0.02% |
| SMC: hồi về order block sau BOS | 449 | 48% | 47% | 52% | 51% | 0.12% |
| SMC: hồi về fair value gap | 584 | 50% | 47% | 50% | 51% | 0.05% |
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
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 869 | 46% | 45% | 49% | 51% | -0.03% |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 1069 | 54% | 54% | 53% | 51% | 0.14% |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 432 | 46% | 49% | 48% | 51% | -0.12% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 470 | 55% | 54% | 50% | 51% | 0.05% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 1722 | 50% | 50% | 50% | 51% | -0.01% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 550 | 44% | 45% | 46% | 51% | -0.08% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 424 | 42% | 40% | 45% | 51% | -0.09% |

| Chiến lược | Số lệnh | Thắng | LN/lệnh | Profit factor | Tổng LN cả kỳ | Sụt giảm tối đa | Mua và giữ | Tổng LN 3 tháng |
|---|---|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 606 | 20% | -0.10% | 0.67 | -46% | 46% | -24% | -7% |
| Cắt EMA20/50 | 621 | 19% | -0.05% | 0.88 | -30% | 40% | -24% | -4% |
| Phá đỉnh/đáy 20 nến | 1034 | 23% | -0.13% | 0.65 | -75% | 76% | -24% | -17% |
| Nén Bollinger rồi bung | 134 | 10% | -0.17% | 0.55 | -21% | 30% | -24% | -6% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 561 | 22% | -0.08% | 0.74 | -38% | 40% | -24% | -2% |
| Volume profile: thoát vùng giá trị | 371 | 17% | -0.11% | 0.76 | -36% | 41% | -24% | -14% |
| Volume profile: hồi về POC | 1143 | 26% | -0.12% | 0.57 | -75% | 75% | -24% | -26% |
| Volume profile: cắt EMA lọc theo POC | 1309 | 15% | -0.08% | 0.73 | -68% | 70% | -24% | -23% |
| RSI14 qua 50 (chuẩn so sánh) | 3849 | 15% | -0.11% | 0.52 | -99% | 99% | -24% | -68% |
| VP thoát vùng + RSI xác nhận | 778 | 24% | -0.09% | 0.74 | -52% | 56% | -24% | -15% |
| VP thoát vùng + RSI + khối lượng 1,5x | 339 | 17% | -0.11% | 0.75 | -34% | 41% | -24% | -13% |
| VP thoát vùng + RSI + ADX20 | 339 | 17% | -0.12% | 0.75 | -35% | 46% | -24% | -8% |
| VP hồi trong vùng + RSI 30/70 | 179 | 33% | -0.10% | 0.70 | -16% | 17% | -24% | -4% |
| Đồng thuận POC + EMA + RSI | 1012 | 17% | -0.07% | 0.79 | -56% | 59% | -24% | -18% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 326 | 17% | -0.12% | 0.74 | -34% | 38% | -24% | -12% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 346 | 17% | -0.15% | 0.67 | -41% | 48% | -24% | -7% |
| SMC: cấu trúc BOS/CHoCH | 785 | 20% | -0.12% | 0.70 | -63% | 63% | -24% | -19% |
| SMC: hồi về order block sau BOS | 449 | 19% | -0.08% | 0.77 | -33% | 44% | -24% | -21% |
| SMC: hồi về fair value gap | 586 | 20% | -0.10% | 0.75 | -45% | 45% | -24% | -21% |
| SMC: quét thanh khoản đảo chiều | 1280 | 29% | -0.12% | 0.64 | -80% | 81% | -24% | -27% |
| SMC: quét thanh khoản + displacement | 1036 | 23% | -0.08% | 0.58 | -57% | 60% | -24% | -22% |
| PA: nến nhấn chìm theo EMA50 | 2493 | 21% | -0.11% | 0.56 | -93% | 93% | -24% | -41% |
| PA: pin bar tại đỉnh/đáy swing | 1080 | 26% | -0.15% | 0.49 | -80% | 80% | -24% | -31% |
| PA: phá đỉnh/đáy rồi retest | 841 | 11% | -0.11% | 0.62 | -62% | 64% | -24% | -20% |
| PA: inside bar theo xu hướng EMA | 472 | 19% | -0.09% | 0.78 | -37% | 39% | -24% | -15% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 1470 | 44% | -0.08% | 0.52 | -71% | 71% | -24% | -26% |
| CK: cắt SMA50/200 (golden/death cross) | 222 | 13% | -0.13% | 0.73 | -26% | 34% | -24% | -18% |
| CK: MACD histogram + lọc EMA200 | 2003 | 22% | -0.09% | 0.66 | -85% | 86% | -24% | -46% |
| CK: Supertrend 10/3 | 729 | 22% | -0.09% | 0.76 | -52% | 60% | -24% | 7% |
| CK: Parabolic SAR | 2304 | 27% | -0.12% | 0.62 | -94% | 94% | -24% | -48% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 1347 | 17% | -0.09% | 0.70 | -73% | 76% | -24% | -29% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 709 | 25% | -0.09% | 0.74 | -50% | 55% | -24% | -11% |
| CK: Bollinger hồi về trung bình + SMA200 | 472 | 48% | -0.07% | 0.72 | -29% | 29% | -24% | -9% |
| CK: Minervini trend template | 0 | | | | | | | |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 195 | 21% | -0.12% | 0.63 | -22% | 24% | -24% | -5% |
| CK: Elder Triple Screen (khung cao + Force Index) | 335 | 11% | -0.21% | 0.54 | -52% | 53% | -24% | -18% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 191 | 13% | -0.04% | 0.91 | -13% | 39% | -24% | 11% |
| CK: Turtle Donchian 55/20 | 478 | 20% | -0.15% | 0.63 | -52% | 56% | -24% | -12% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 766 | 21% | -0.08% | 0.81 | -47% | 52% | -24% | -11% |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 1073 | 44% | -0.11% | 0.58 | -69% | 69% | -24% | -20% |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 413 | 21% | -0.15% | 0.69 | -48% | 50% | -24% | -15% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 472 | 43% | -0.06% | 0.79 | -26% | 29% | -24% | -10% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 1540 | 17% | -0.09% | 0.64 | -76% | 77% | -24% | -25% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 550 | 22% | -0.10% | 0.75 | -44% | 53% | -24% | 10% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 424 | 19% | -0.14% | 0.67 | -47% | 54% | -24% | 7% |

## ETH · 35039 nến 15m · 2025-10-17 đến 2026-10-17

| Chiến lược | Số tín hiệu | Đúng hướng 1 giờ | 4 giờ | 1 ngày | Nền 1 ngày | LN TB 1 ngày |
|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 607 | 49% | 48% | 48% | 51% | 0.20% |
| Cắt EMA20/50 | 730 | 43% | 47% | 48% | 51% | 0.01% |
| Phá đỉnh/đáy 20 nến | 1004 | 42% | 45% | 49% | 51% | 0.03% |
| Nén Bollinger rồi bung | 125 | 42% | 41% | 45% | 51% | -0.14% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 603 | 45% | 48% | 46% | 51% | 0.06% |
| Volume profile: thoát vùng giá trị | 354 | 45% | 49% | 51% | 51% | 0.24% |
| Volume profile: hồi về POC | 980 | 51% | 54% | 52% | 51% | -0.11% |
| Volume profile: cắt EMA lọc theo POC | 1359 | 47% | 47% | 47% | 51% | 0.09% |
| RSI14 qua 50 (chuẩn so sánh) | 4306 | 49% | 49% | 49% | 51% | -0.01% |
| VP thoát vùng + RSI xác nhận | 751 | 46% | 47% | 47% | 51% | 0.15% |
| VP thoát vùng + RSI + khối lượng 1,5x | 334 | 42% | 47% | 52% | 51% | 0.23% |
| VP thoát vùng + RSI + ADX20 | 329 | 46% | 48% | 50% | 51% | 0.25% |
| VP hồi trong vùng + RSI 30/70 | 158 | 61% | 58% | 50% | 51% | 0.07% |
| Đồng thuận POC + EMA + RSI | 1044 | 45% | 46% | 48% | 51% | 0.06% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 327 | 43% | 47% | 51% | 51% | 0.19% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 357 | 44% | 47% | 50% | 51% | 0.13% |
| SMC: cấu trúc BOS/CHoCH | 869 | 44% | 45% | 48% | 51% | -0.09% |
| SMC: hồi về order block sau BOS | 447 | 48% | 48% | 53% | 51% | 0.18% |
| SMC: hồi về fair value gap | 568 | 51% | 48% | 49% | 51% | -0.05% |
| SMC: quét thanh khoản đảo chiều | 1152 | 53% | 52% | 49% | 51% | -0.11% |
| SMC: quét thanh khoản + displacement | 1021 | 53% | 51% | 49% | 51% | -0.06% |
| PA: nến nhấn chìm theo EMA50 | 2573 | 47% | 46% | 47% | 51% | -0.00% |
| PA: pin bar tại đỉnh/đáy swing | 898 | 52% | 52% | 51% | 51% | -0.09% |
| PA: phá đỉnh/đáy rồi retest | 828 | 45% | 45% | 47% | 51% | -0.09% |
| PA: inside bar theo xu hướng EMA | 492 | 46% | 46% | 48% | 51% | -0.11% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 1429 | 53% | 51% | 47% | 51% | -0.08% |
| CK: cắt SMA50/200 (golden/death cross) | 223 | 48% | 46% | 47% | 51% | -0.08% |
| CK: MACD histogram + lọc EMA200 | 2102 | 47% | 47% | 49% | 51% | 0.03% |
| CK: Supertrend 10/3 | 770 | 44% | 47% | 48% | 51% | -0.01% |
| CK: Parabolic SAR | 2672 | 47% | 49% | 49% | 51% | 0.01% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 1476 | 46% | 47% | 48% | 51% | -0.03% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 645 | 43% | 47% | 49% | 51% | 0.04% |
| CK: Bollinger hồi về trung bình + SMA200 | 464 | 58% | 57% | 51% | 51% | 0.07% |
| CK: Minervini trend template | 1 | 0% | 100% | 100% | 51% | 2.00% |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 182 | 46% | 51% | 52% | 51% | 0.00% |
| CK: Elder Triple Screen (khung cao + Force Index) | 345 | 42% | 45% | 47% | 51% | -0.07% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 222 | 44% | 40% | 45% | 51% | -0.31% |
| CK: Turtle Donchian 55/20 | 422 | 41% | 46% | 48% | 51% | 0.00% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 848 | 43% | 47% | 48% | 51% | -0.11% |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 994 | 55% | 52% | 50% | 51% | -0.02% |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 378 | 45% | 48% | 52% | 51% | -0.04% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 467 | 52% | 55% | 48% | 51% | 0.09% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 1802 | 47% | 48% | 49% | 51% | -0.01% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 549 | 42% | 45% | 45% | 51% | -0.17% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 421 | 42% | 43% | 43% | 51% | -0.29% |

| Chiến lược | Số lệnh | Thắng | LN/lệnh | Profit factor | Tổng LN cả kỳ | Sụt giảm tối đa | Mua và giữ | Tổng LN 3 tháng |
|---|---|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 608 | 22% | -0.07% | 0.81 | -37% | 40% | -37% | -10% |
| Cắt EMA20/50 | 673 | 17% | -0.05% | 0.90 | -39% | 49% | -37% | -18% |
| Phá đỉnh/đáy 20 nến | 960 | 23% | -0.16% | 0.68 | -80% | 82% | -37% | -33% |
| Nén Bollinger rồi bung | 125 | 9% | -0.21% | 0.58 | -24% | 27% | -37% | -7% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 604 | 21% | -0.07% | 0.83 | -36% | 40% | -37% | -17% |
| Volume profile: thoát vùng giá trị | 354 | 20% | -0.01% | 0.98 | -11% | 32% | -37% | 16% |
| Volume profile: hồi về POC | 980 | 31% | -0.08% | 0.75 | -57% | 62% | -37% | -11% |
| Volume profile: cắt EMA lọc theo POC | 1336 | 15% | -0.08% | 0.78 | -71% | 74% | -37% | -31% |
| RSI14 qua 50 (chuẩn so sánh) | 3946 | 15% | -0.12% | 0.58 | -99% | 99% | -37% | -61% |
| VP thoát vùng + RSI xác nhận | 752 | 23% | -0.07% | 0.84 | -46% | 52% | -37% | -11% |
| VP thoát vùng + RSI + khối lượng 1,5x | 334 | 20% | -0.04% | 0.93 | -19% | 32% | -37% | 8% |
| VP thoát vùng + RSI + ADX20 | 329 | 21% | 0.01% | 1.01 | -5% | 24% | -37% | 4% |
| VP hồi trong vùng + RSI 30/70 | 158 | 32% | -0.11% | 0.73 | -17% | 19% | -37% | -1% |
| Đồng thuận POC + EMA + RSI | 1046 | 16% | -0.09% | 0.80 | -66% | 70% | -37% | -26% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 328 | 19% | -0.06% | 0.89 | -24% | 32% | -37% | 9% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 358 | 20% | -0.05% | 0.91 | -22% | 36% | -37% | 11% |
| SMC: cấu trúc BOS/CHoCH | 776 | 18% | -0.21% | 0.62 | -82% | 82% | -37% | -37% |
| SMC: hồi về order block sau BOS | 448 | 20% | -0.17% | 0.65 | -55% | 58% | -37% | -27% |
| SMC: hồi về fair value gap | 571 | 20% | -0.09% | 0.81 | -45% | 50% | -37% | -15% |
| SMC: quét thanh khoản đảo chiều | 1151 | 30% | -0.08% | 0.82 | -62% | 63% | -37% | -41% |
| SMC: quét thanh khoản + displacement | 1024 | 25% | -0.09% | 0.62 | -62% | 62% | -37% | -21% |
| PA: nến nhấn chìm theo EMA50 | 2509 | 23% | -0.10% | 0.67 | -92% | 92% | -37% | -49% |
| PA: pin bar tại đỉnh/đáy swing | 899 | 30% | -0.14% | 0.64 | -72% | 72% | -37% | -33% |
| PA: phá đỉnh/đáy rồi retest | 829 | 11% | -0.15% | 0.60 | -72% | 72% | -37% | -41% |
| PA: inside bar theo xu hướng EMA | 493 | 17% | 0.03% | 1.05 | -0% | 33% | -37% | -7% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 1432 | 50% | -0.08% | 0.62 | -68% | 68% | -37% | -18% |
| CK: cắt SMA50/200 (golden/death cross) | 223 | 13% | -0.25% | 0.59 | -44% | 45% | -37% | -23% |
| CK: MACD histogram + lọc EMA200 | 2050 | 22% | -0.10% | 0.72 | -87% | 89% | -37% | -50% |
| CK: Supertrend 10/3 | 692 | 23% | -0.13% | 0.77 | -61% | 66% | -37% | -23% |
| CK: Parabolic SAR | 2168 | 31% | -0.10% | 0.76 | -89% | 90% | -37% | -39% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 1434 | 16% | -0.11% | 0.73 | -81% | 81% | -37% | -38% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 641 | 24% | -0.13% | 0.73 | -58% | 63% | -37% | -21% |
| CK: Bollinger hồi về trung bình + SMA200 | 464 | 52% | -0.05% | 0.84 | -21% | 24% | -37% | -12% |
| CK: Minervini trend template | 1 | 0% | -0.96% | 0.00 | -1% | 3% | -37% | -1% |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 182 | 25% | -0.10% | 0.76 | -17% | 21% | -37% | -12% |
| CK: Elder Triple Screen (khung cao + Force Index) | 346 | 14% | -0.15% | 0.75 | -45% | 54% | -37% | -26% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 223 | 12% | -0.16% | 0.74 | -35% | 54% | -37% | -20% |
| CK: Turtle Donchian 55/20 | 420 | 19% | -0.13% | 0.78 | -44% | 46% | -37% | -16% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 751 | 21% | -0.12% | 0.77 | -63% | 67% | -37% | -31% |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 999 | 47% | -0.11% | 0.67 | -67% | 67% | -37% | -22% |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 351 | 19% | -0.29% | 0.59 | -65% | 69% | -37% | -13% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 467 | 46% | -0.05% | 0.88 | -21% | 26% | -37% | -17% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 1626 | 18% | -0.10% | 0.68 | -83% | 84% | -37% | -44% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 550 | 21% | -0.12% | 0.77 | -52% | 60% | -37% | -34% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 422 | 20% | -0.14% | 0.74 | -48% | 52% | -37% | -26% |

## SOL · 35039 nến 15m · 2025-10-17 đến 2026-10-17

| Chiến lược | Số tín hiệu | Đúng hướng 1 giờ | 4 giờ | 1 ngày | Nền 1 ngày | LN TB 1 ngày |
|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 626 | 49% | 48% | 49% | 51% | 0.23% |
| Cắt EMA20/50 | 702 | 46% | 46% | 50% | 51% | -0.06% |
| Phá đỉnh/đáy 20 nến | 1011 | 45% | 48% | 48% | 51% | -0.02% |
| Nén Bollinger rồi bung | 130 | 46% | 42% | 47% | 51% | -0.08% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 593 | 48% | 49% | 48% | 51% | -0.00% |
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
| SMC: hồi về order block sau BOS | 435 | 45% | 47% | 50% | 51% | -0.03% |
| SMC: hồi về fair value gap | 573 | 43% | 45% | 45% | 51% | -0.25% |
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
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 877 | 47% | 46% | 48% | 51% | -0.09% |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 1123 | 53% | 56% | 52% | 51% | 0.16% |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 436 | 49% | 50% | 49% | 51% | -0.08% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 487 | 53% | 52% | 47% | 51% | -0.04% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 1704 | 48% | 49% | 51% | 51% | 0.01% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 553 | 44% | 46% | 47% | 51% | -0.07% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 425 | 43% | 47% | 46% | 51% | -0.01% |

| Chiến lược | Số lệnh | Thắng | LN/lệnh | Profit factor | Tổng LN cả kỳ | Sụt giảm tối đa | Mua và giữ | Tổng LN 3 tháng |
|---|---|---|---|---|---|---|---|---|
| Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng) | 628 | 25% | -0.08% | 0.80 | -41% | 53% | -44% | 13% |
| Cắt EMA20/50 | 658 | 17% | -0.08% | 0.87 | -49% | 52% | -44% | -13% |
| Phá đỉnh/đáy 20 nến | 972 | 26% | -0.09% | 0.83 | -60% | 67% | -44% | -12% |
| Nén Bollinger rồi bung | 131 | 8% | -0.29% | 0.51 | -32% | 37% | -44% | -4% |
| Xu hướng + phá đỉnh/đáy cùng chiều | 594 | 22% | -0.14% | 0.69 | -58% | 63% | -44% | 8% |
| Volume profile: thoát vùng giá trị | 376 | 20% | -0.05% | 0.92 | -22% | 42% | -44% | -6% |
| Volume profile: hồi về POC | 1098 | 30% | -0.12% | 0.69 | -74% | 75% | -44% | -24% |
| Volume profile: cắt EMA lọc theo POC | 1358 | 16% | -0.10% | 0.76 | -78% | 78% | -44% | -32% |
| RSI14 qua 50 (chuẩn so sánh) | 3897 | 17% | -0.10% | 0.66 | -99% | 99% | -44% | -66% |
| VP thoát vùng + RSI xác nhận | 803 | 25% | -0.10% | 0.79 | -58% | 62% | -44% | -14% |
| VP thoát vùng + RSI + khối lượng 1,5x | 347 | 19% | -0.08% | 0.88 | -29% | 46% | -44% | -4% |
| VP thoát vùng + RSI + ADX20 | 346 | 21% | -0.05% | 0.92 | -21% | 38% | -44% | -15% |
| VP hồi trong vùng + RSI 30/70 | 170 | 41% | -0.01% | 0.98 | -2% | 14% | -44% | -6% |
| Đồng thuận POC + EMA + RSI | 1042 | 17% | -0.09% | 0.82 | -66% | 67% | -44% | -31% |
| VP + RSI + KL, chỉ vào cùng hướng EMA | 332 | 19% | -0.10% | 0.85 | -32% | 46% | -44% | -4% |
| VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi | 350 | 20% | -0.10% | 0.84 | -33% | 44% | -44% | -8% |
| SMC: cấu trúc BOS/CHoCH | 785 | 22% | -0.08% | 0.86 | -52% | 53% | -44% | -20% |
| SMC: hồi về order block sau BOS | 437 | 20% | -0.11% | 0.78 | -42% | 48% | -44% | -24% |
| SMC: hồi về fair value gap | 576 | 17% | -0.17% | 0.70 | -65% | 65% | -44% | -23% |
| SMC: quét thanh khoản đảo chiều | 1273 | 30% | -0.17% | 0.65 | -89% | 90% | -44% | -21% |
| SMC: quét thanh khoản + displacement | 1052 | 28% | -0.10% | 0.66 | -65% | 68% | -44% | -19% |
| PA: nến nhấn chìm theo EMA50 | 2455 | 25% | -0.09% | 0.71 | -91% | 91% | -44% | -50% |
| PA: pin bar tại đỉnh/đáy swing | 885 | 28% | -0.20% | 0.55 | -84% | 84% | -44% | -31% |
| PA: phá đỉnh/đáy rồi retest | 776 | 13% | -0.10% | 0.74 | -57% | 59% | -44% | -13% |
| PA: inside bar theo xu hướng EMA | 466 | 18% | 0.03% | 1.06 | 3% | 40% | -44% | 26% |
| CK: Connors RSI(2) hồi về trung bình + SMA200 | 1493 | 53% | -0.09% | 0.63 | -74% | 74% | -44% | -28% |
| CK: cắt SMA50/200 (golden/death cross) | 222 | 13% | -0.22% | 0.69 | -41% | 48% | -44% | -11% |
| CK: MACD histogram + lọc EMA200 | 1983 | 23% | -0.10% | 0.74 | -88% | 90% | -44% | -40% |
| CK: Supertrend 10/3 | 728 | 22% | -0.10% | 0.84 | -55% | 66% | -44% | -1% |
| CK: Parabolic SAR | 2336 | 30% | -0.13% | 0.72 | -95% | 95% | -44% | -54% |
| CK: Ichimoku (mây + Tenkan/Kijun) | 1318 | 17% | -0.07% | 0.83 | -67% | 69% | -44% | -22% |
| CK: bung kênh Keltner EMA20 ± 2 ATR | 689 | 26% | -0.11% | 0.79 | -55% | 58% | -44% | -15% |
| CK: Bollinger hồi về trung bình + SMA200 | 469 | 47% | -0.14% | 0.66 | -49% | 49% | -44% | -15% |
| CK: Minervini trend template | 2 | 0% | -2.96% | 0.00 | -6% | 7% | -44% | -1% |
| CK: nền co biên rồi bung với khối lượng (O'Neil/VCP) | 146 | 20% | -0.20% | 0.62 | -26% | 29% | -44% | -9% |
| CK: Elder Triple Screen (khung cao + Force Index) | 322 | 17% | -0.10% | 0.84 | -34% | 51% | -44% | 11% |
| CK: Weinstein giai đoạn 2/4 (SMA30 khung cao) | 209 | 12% | -0.20% | 0.70 | -37% | 54% | -44% | -2% |
| CK: Turtle Donchian 55/20 | 472 | 24% | -0.00% | 0.99 | -9% | 23% | -44% | -5% |
| CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h) | 778 | 21% | -0.08% | 0.87 | -52% | 67% | -44% | 27% |
| CK: VWAP ngày hồi về trung bình (chỉ khung < 4h) | 1123 | 49% | -0.10% | 0.73 | -69% | 70% | -44% | -16% |
| CK: hộp Darvas (đỉnh mới + khối lượng) | 410 | 20% | -0.09% | 0.86 | -37% | 61% | -44% | 7% |
| CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors) | 488 | 44% | -0.09% | 0.80 | -37% | 41% | -44% | -9% |
| CK: động lượng tuyệt đối 90 nến (Antonacci) | 1540 | 20% | -0.09% | 0.75 | -78% | 80% | -44% | -6% |
| Đồng thuận 2/3: Supertrend + Keltner + Weinstein | 554 | 23% | -0.05% | 0.91 | -29% | 49% | -44% | 13% |
| Đồng thuận 2/3 bắt buộc cùng chiều khung cao | 426 | 24% | -0.03% | 0.94 | -19% | 44% | -44% | 21% |
