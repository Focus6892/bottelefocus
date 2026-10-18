# Scalp · khung 1h · tối ưu trong mẫu 70% đầu, kiểm tra ngoài mẫu 30% cuối

Cột: số lệnh | thắng | profit factor | lãi/lệnh | tổng lãi | sụt giảm | lệnh/ngày. Phí: taker 0,05% mỗi chiều; lệnh chờ 0,02% vào + 0,05% ra. 'Mặc định' = TP 1,5 / SL 1 / giữ 16 nến không tối ưu. 'Tốt nhất trong mẫu' chọn theo PF với >= 40 lệnh; nếu không tổ hợp nào đạt PF > 1,1 thì bỏ trống.

## BTC · 26279 nến · 2023-10-19 đến 2026-10-17 · ngoài mẫu từ nến thứ 18395

| Chiến lược | Tín hiệu | Tham số tốt nhất (TP/SL/giữ) | Trong mẫu | Ngoài mẫu (cùng tham số) | Ngoài mẫu, mặc định |
|---|---|---|---|---|---|
| VP: từ chối tại VAL/VAH, TP/SL theo ATR | 1042 | không có | 0 lệnh | 0 lệnh | 189 lệnh · thắng 42% · PF 0.88 · -0.049%/lệnh · tổng -9% · sụt 17% · 0.6/ngày |
| VP: từ chối tại VAL/VAH, TP/SL theo ATR · lọc xu hướng ngày | 551 | không có | 0 lệnh | 0 lệnh | 102 lệnh · thắng 40% · PF 0.87 · -0.049%/lệnh · tổng -5% · sụt 8% · 0.3/ngày |
| VP: từ chối tại VAL/VAH, chốt tại POC, dừng dưới nến | 1042 | không có | 0 lệnh | 0 lệnh | 207 lệnh · thắng 29% · PF 1.05 · 0.014%/lệnh · tổng 2% · sụt 16% · 0.6/ngày |
| VP: từ chối tại VAL/VAH, chốt tại POC, dừng dưới nến · lọc xu hướng ngày | 551 | không có | 0 lệnh | 0 lệnh | 108 lệnh · thắng 30% · PF 0.94 · -0.019%/lệnh · tổng -2% · sụt 11% · 0.3/ngày |
| VP: lệnh chờ tại VAL/VAH (phí maker) | 1633 | 1.0/1.5/8 | 549 lệnh · thắng 65% · PF 1.17 · 0.059%/lệnh · tổng 36% · sụt 15% · 0.7/ngày | 250 lệnh · thắng 62% · PF 1.05 · 0.016%/lệnh · tổng 3% · sụt 10% · 0.8/ngày | 232 lệnh · thắng 43% · PF 0.96 · -0.015%/lệnh · tổng -4% · sụt 17% · 0.7/ngày |
| VP: lệnh chờ tại VAL/VAH (phí maker) · lọc xu hướng ngày | 821 | 1.5/1.5/8 | 266 lệnh · thắng 56% · PF 1.12 · 0.053%/lệnh · tổng 14% · sụt 10% · 0.3/ngày | 113 lệnh · thắng 45% · PF 0.87 · -0.052%/lệnh · tổng -6% · sụt 15% · 0.3/ngày | 113 lệnh · thắng 43% · PF 1.08 · 0.026%/lệnh · tổng 3% · sụt 9% · 0.3/ngày |
| Hồi theo xu hướng 4h: RSI<40/EMA20 rồi vượt đỉnh nến trước | 1194 | không có | 0 lệnh | 0 lệnh | 260 lệnh · thắng 35% · PF 0.57 · -0.199%/lệnh · tổng -41% · sụt 42% · 0.8/ngày |
| Hồi theo xu hướng 4h: RSI<40/EMA20 rồi vượt đỉnh nến trước · lọc xu hướng ngày | 755 | không có | 0 lệnh | 0 lệnh | 151 lệnh · thắng 35% · PF 0.58 · -0.204%/lệnh · tổng -27% · sụt 27% · 0.5/ngày |
| VWAP phiên: xuyên -1 sd rồi đóng lại | 4997 | không có | 0 lệnh | 0 lệnh | 738 lệnh · thắng 37% · PF 0.65 · -0.157%/lệnh · tổng -69% · sụt 69% · 2.2/ngày |
| VWAP phiên: xuyên -1 sd rồi đóng lại · lọc xu hướng ngày | 2468 | không có | 0 lệnh | 0 lệnh | 452 lệnh · thắng 37% · PF 0.65 · -0.151%/lệnh · tổng -50% · sụt 50% · 1.4/ngày |
| Nén Bollinger 48 nến rồi bung + khối lượng 1,5x | 721 | 3.0/1.5/8 | 269 lệnh · thắng 43% · PF 1.22 · 0.099%/lệnh · tổng 28% · sụt 12% · 0.4/ngày | 126 lệnh · thắng 42% · PF 0.89 · -0.044%/lệnh · tổng -6% · sụt 9% · 0.4/ngày | 143 lệnh · thắng 38% · PF 0.71 · -0.115%/lệnh · tổng -16% · sụt 16% · 0.4/ngày |
| Nén Bollinger 48 nến rồi bung + khối lượng 1,5x · lọc xu hướng ngày | 354 | 3.0/1.5/8 | 121 lệnh · thắng 45% · PF 1.15 · 0.072%/lệnh · tổng 8% · sụt 11% · 0.2/ngày | 68 lệnh · thắng 47% · PF 1.18 · 0.071%/lệnh · tổng 5% · sụt 7% · 0.2/ngày | 78 lệnh · thắng 45% · PF 0.97 · -0.010%/lệnh · tổng -1% · sụt 5% · 0.2/ngày |
| VP: thoát vùng qua node khối lượng thấp + khối lượng 1,2x | 328 | không có | 0 lệnh | 0 lệnh | 80 lệnh · thắng 44% · PF 0.92 · -0.036%/lệnh · tổng -3% · sụt 7% · 0.2/ngày |
| VP: thoát vùng qua node khối lượng thấp + khối lượng 1,2x · lọc xu hướng ngày | 167 | không có | 0 lệnh | 0 lệnh | 39 lệnh · thắng 51% · PF 1.12 · 0.050%/lệnh · tổng 2% · sụt 5% · 0.1/ngày |
| Bung biên độ 60 phút đầu ngày | 1671 | không có | 0 lệnh | 0 lệnh | 420 lệnh · thắng 38% · PF 0.74 · -0.114%/lệnh · tổng -39% · sụt 40% · 1.3/ngày |
| Bung biên độ 60 phút đầu ngày · lọc xu hướng ngày | 827 | không có | 0 lệnh | 0 lệnh | 249 lệnh · thắng 39% · PF 0.77 · -0.096%/lệnh · tổng -22% · sụt 23% · 0.8/ngày |

## ETH · 26279 nến · 2023-10-19 đến 2026-10-17 · ngoài mẫu từ nến thứ 18395

| Chiến lược | Tín hiệu | Tham số tốt nhất (TP/SL/giữ) | Trong mẫu | Ngoài mẫu (cùng tham số) | Ngoài mẫu, mặc định |
|---|---|---|---|---|---|
| VP: từ chối tại VAL/VAH, TP/SL theo ATR | 1023 | không có | 0 lệnh | 0 lệnh | 178 lệnh · thắng 48% · PF 1.16 · 0.072%/lệnh · tổng 12% · sụt 12% · 0.5/ngày |
| VP: từ chối tại VAL/VAH, TP/SL theo ATR · lọc xu hướng ngày | 494 | 3.0/1.5/16 | 171 lệnh · thắng 44% · PF 1.17 · 0.136%/lệnh · tổng 22% · sụt 15% · 0.2/ngày | 89 lệnh · thắng 39% · PF 0.93 · -0.047%/lệnh · tổng -5% · sụt 12% · 0.3/ngày | 97 lệnh · thắng 46% · PF 1.05 · 0.024%/lệnh · tổng 2% · sụt 8% · 0.3/ngày |
| VP: từ chối tại VAL/VAH, chốt tại POC, dừng dưới nến | 1023 | không có | 0 lệnh | 0 lệnh | 193 lệnh · thắng 28% · PF 0.87 · -0.051%/lệnh · tổng -10% · sụt 13% · 0.6/ngày |
| VP: từ chối tại VAL/VAH, chốt tại POC, dừng dưới nến · lọc xu hướng ngày | 494 | không có | 0 lệnh | 0 lệnh | 105 lệnh · thắng 22% · PF 0.81 · -0.077%/lệnh · tổng -8% · sụt 15% · 0.3/ngày |
| VP: lệnh chờ tại VAL/VAH (phí maker) | 1585 | không có | 0 lệnh | 0 lệnh | 203 lệnh · thắng 44% · PF 1.09 · 0.044%/lệnh · tổng 8% · sụt 10% · 0.6/ngày |
| VP: lệnh chờ tại VAL/VAH (phí maker) · lọc xu hướng ngày | 818 | 3.0/1.5/16 | 197 lệnh · thắng 47% · PF 1.20 · 0.153%/lệnh · tổng 30% · sụt 19% · 0.3/ngày | 98 lệnh · thắng 40% · PF 0.86 · -0.095%/lệnh · tổng -10% · sụt 12% · 0.3/ngày | 125 lệnh · thắng 39% · PF 0.82 · -0.089%/lệnh · tổng -11% · sụt 13% · 0.4/ngày |
| Hồi theo xu hướng 4h: RSI<40/EMA20 rồi vượt đỉnh nến trước | 1127 | không có | 0 lệnh | 0 lệnh | 253 lệnh · thắng 39% · PF 0.82 · -0.095%/lệnh · tổng -22% · sụt 25% · 0.8/ngày |
| Hồi theo xu hướng 4h: RSI<40/EMA20 rồi vượt đỉnh nến trước · lọc xu hướng ngày | 704 | không có | 0 lệnh | 0 lệnh | 151 lệnh · thắng 38% · PF 0.81 · -0.102%/lệnh · tổng -15% · sụt 16% · 0.5/ngày |
| VWAP phiên: xuyên -1 sd rồi đóng lại | 4883 | không có | 0 lệnh | 0 lệnh | 720 lệnh · thắng 36% · PF 0.68 · -0.187%/lệnh · tổng -75% · sụt 75% · 2.2/ngày |
| VWAP phiên: xuyên -1 sd rồi đóng lại · lọc xu hướng ngày | 2450 | không có | 0 lệnh | 0 lệnh | 440 lệnh · thắng 38% · PF 0.74 · -0.143%/lệnh · tổng -48% · sụt 48% · 1.3/ngày |
| Nén Bollinger 48 nến rồi bung + khối lượng 1,5x | 642 | không có | 0 lệnh | 0 lệnh | 133 lệnh · thắng 42% · PF 0.94 · -0.030%/lệnh · tổng -5% · sụt 11% · 0.4/ngày |
| Nén Bollinger 48 nến rồi bung + khối lượng 1,5x · lọc xu hướng ngày | 331 | 3.0/1.5/48 | 120 lệnh · thắng 39% · PF 1.24 · 0.209%/lệnh · tổng 25% · sụt 18% · 0.2/ngày | 62 lệnh · thắng 45% · PF 1.70 · 0.470%/lệnh · tổng 32% · sụt 8% · 0.2/ngày | 73 lệnh · thắng 49% · PF 1.32 · 0.130%/lệnh · tổng 9% · sụt 7% · 0.2/ngày |
| VP: thoát vùng qua node khối lượng thấp + khối lượng 1,2x | 292 | 2.0/1.5/8 | 187 lệnh · thắng 49% · PF 1.19 · 0.130%/lệnh · tổng 24% · sụt 23% · 0.2/ngày | 84 lệnh · thắng 46% · PF 1.05 · 0.030%/lệnh · tổng 2% · sụt 11% · 0.3/ngày | 85 lệnh · thắng 53% · PF 1.35 · 0.152%/lệnh · tổng 13% · sụt 6% · 0.3/ngày |
| VP: thoát vùng qua node khối lượng thấp + khối lượng 1,2x · lọc xu hướng ngày | 151 | 3.0/1.0/48 | 101 lệnh · thắng 36% · PF 1.49 · 0.338%/lệnh · tổng 38% · sụt 11% · 0.1/ngày | 42 lệnh · thắng 36% · PF 1.35 · 0.221%/lệnh · tổng 9% · sụt 7% · 0.1/ngày | 42 lệnh · thắng 52% · PF 1.34 · 0.155%/lệnh · tổng 6% · sụt 5% · 0.1/ngày |
| Bung biên độ 60 phút đầu ngày | 1643 | không có | 0 lệnh | 0 lệnh | 404 lệnh · thắng 42% · PF 0.92 · -0.044%/lệnh · tổng -18% · sụt 28% · 1.2/ngày |
| Bung biên độ 60 phút đầu ngày · lọc xu hướng ngày | 816 | 2.0/1.0/48 | 539 lệnh · thắng 38% · PF 1.12 · 0.082%/lệnh · tổng 45% · sụt 28% · 0.7/ngày | 235 lệnh · thắng 38% · PF 1.04 · 0.023%/lệnh · tổng 3% · sụt 17% · 0.7/ngày | 244 lệnh · thắng 47% · PF 1.10 · 0.047%/lệnh · tổng 10% · sụt 15% · 0.7/ngày |

## SOL · 26279 nến · 2023-10-19 đến 2026-10-17 · ngoài mẫu từ nến thứ 18395

| Chiến lược | Tín hiệu | Tham số tốt nhất (TP/SL/giữ) | Trong mẫu | Ngoài mẫu (cùng tham số) | Ngoài mẫu, mặc định |
|---|---|---|---|---|---|
| VP: từ chối tại VAL/VAH, TP/SL theo ATR | 1021 | 3.0/0.5/48 | 441 lệnh · thắng 18% · PF 1.23 · 0.150%/lệnh · tổng 74% · sụt 34% · 0.6/ngày | 219 lệnh · thắng 14% · PF 0.89 · -0.051%/lệnh · tổng -12% · sụt 25% · 0.7/ngày | 198 lệnh · thắng 40% · PF 0.95 · -0.027%/lệnh · tổng -7% · sụt 19% · 0.6/ngày |
| VP: từ chối tại VAL/VAH, TP/SL theo ATR · lọc xu hướng ngày | 466 | 3.0/0.5/48 | 217 lệnh · thắng 18% · PF 1.43 · 0.273%/lệnh · tổng 70% · sụt 27% · 0.3/ngày | 99 lệnh · thắng 11% · PF 0.68 · -0.158%/lệnh · tổng -15% · sụt 19% · 0.3/ngày | 89 lệnh · thắng 42% · PF 0.89 · -0.065%/lệnh · tổng -6% · sụt 15% · 0.3/ngày |
| VP: từ chối tại VAL/VAH, chốt tại POC, dừng dưới nến | 1021 | không có | 0 lệnh | 0 lệnh | 228 lệnh · thắng 29% · PF 1.14 · 0.060%/lệnh · tổng 12% · sụt 15% · 0.7/ngày |
| VP: từ chối tại VAL/VAH, chốt tại POC, dừng dưới nến · lọc xu hướng ngày | 466 | không có | 0 lệnh | 0 lệnh | 103 lệnh · thắng 28% · PF 0.85 · -0.061%/lệnh · tổng -7% · sụt 11% · 0.3/ngày |
| VP: lệnh chờ tại VAL/VAH (phí maker) | 1660 | 1.0/1.5/16 | 520 lệnh · thắng 68% · PF 1.38 · 0.248%/lệnh · tổng 235% · sụt 30% · 0.7/ngày | 242 lệnh · thắng 70% · PF 1.43 · 0.181%/lệnh · tổng 53% · sụt 9% · 0.7/ngày | 230 lệnh · thắng 46% · PF 1.23 · 0.116%/lệnh · tổng 28% · sụt 17% · 0.7/ngày |
| VP: lệnh chờ tại VAL/VAH (phí maker) · lọc xu hướng ngày | 789 | 3.0/1.0/48 | 209 lệnh · thắng 27% · PF 1.20 · 0.198%/lệnh · tổng 39% · sụt 27% · 0.3/ngày | 90 lệnh · thắng 21% · PF 0.73 · -0.212%/lệnh · tổng -18% · sụt 21% · 0.3/ngày | 107 lệnh · thắng 46% · PF 1.07 · 0.039%/lệnh · tổng 4% · sụt 16% · 0.3/ngày |
| Hồi theo xu hướng 4h: RSI<40/EMA20 rồi vượt đỉnh nến trước | 1045 | không có | 0 lệnh | 0 lệnh | 238 lệnh · thắng 38% · PF 0.77 · -0.144%/lệnh · tổng -30% · sụt 34% · 0.7/ngày |
| Hồi theo xu hướng 4h: RSI<40/EMA20 rồi vượt đỉnh nến trước · lọc xu hướng ngày | 648 | không có | 0 lệnh | 0 lệnh | 137 lệnh · thắng 35% · PF 0.70 · -0.200%/lệnh · tổng -25% · sụt 31% · 0.4/ngày |
| VWAP phiên: xuyên -1 sd rồi đóng lại | 4689 | không có | 0 lệnh | 0 lệnh | 705 lệnh · thắng 43% · PF 0.95 · -0.028%/lệnh · tổng -22% · sụt 40% · 2.1/ngày |
| VWAP phiên: xuyên -1 sd rồi đóng lại · lọc xu hướng ngày | 2353 | không có | 0 lệnh | 0 lệnh | 440 lệnh · thắng 41% · PF 0.92 · -0.048%/lệnh · tổng -21% · sụt 27% · 1.3/ngày |
| Nén Bollinger 48 nến rồi bung + khối lượng 1,5x | 618 | 3.0/1.0/48 | 235 lệnh · thắng 32% · PF 1.22 · 0.212%/lệnh · tổng 52% · sụt 14% · 0.3/ngày | 115 lệnh · thắng 26% · PF 1.10 · 0.072%/lệnh · tổng 7% · sụt 12% · 0.4/ngày | 126 lệnh · thắng 40% · PF 0.84 · -0.092%/lệnh · tổng -12% · sụt 13% · 0.4/ngày |
| Nén Bollinger 48 nến rồi bung + khối lượng 1,5x · lọc xu hướng ngày | 294 | không có | 0 lệnh | 0 lệnh | 62 lệnh · thắng 42% · PF 0.98 · -0.011%/lệnh · tổng -1% · sụt 8% · 0.2/ngày |
| VP: thoát vùng qua node khối lượng thấp + khối lượng 1,2x | 284 | 3.0/1.5/8 | 183 lệnh · thắng 44% · PF 1.25 · 0.246%/lệnh · tổng 48% · sụt 22% · 0.2/ngày | 78 lệnh · thắng 51% · PF 1.93 · 0.466%/lệnh · tổng 42% · sụt 6% · 0.2/ngày | 80 lệnh · thắng 52% · PF 1.42 · 0.208%/lệnh · tổng 17% · sụt 10% · 0.2/ngày |
| VP: thoát vùng qua node khối lượng thấp + khối lượng 1,2x · lọc xu hướng ngày | 149 | 3.0/0.5/48 | 104 lệnh · thắng 22% · PF 1.40 · 0.255%/lệnh · tổng 27% · sụt 15% · 0.1/ngày | 40 lệnh · thắng 35% · PF 2.35 · 0.530%/lệnh · tổng 23% · sụt 4% · 0.1/ngày | 40 lệnh · thắng 57% · PF 1.81 · 0.360%/lệnh · tổng 15% · sụt 3% · 0.1/ngày |
| Bung biên độ 60 phút đầu ngày | 1695 | không có | 0 lệnh | 0 lệnh | 428 lệnh · thắng 37% · PF 0.72 · -0.182%/lệnh · tổng -56% · sụt 59% · 1.3/ngày |
| Bung biên độ 60 phút đầu ngày · lọc xu hướng ngày | 849 | không có | 0 lệnh | 0 lệnh | 248 lệnh · thắng 40% · PF 0.89 · -0.069%/lệnh · tổng -17% · sụt 29% · 0.8/ngày |

## Tham số chung cho cả 3 đồng (chọn trong mẫu theo PF trung bình, kiểm tra ngoài mẫu từng đồng)

| Chiến lược | TP/SL/giữ | PF TB trong mẫu | BTC ngoài mẫu | ETH ngoài mẫu | SOL ngoài mẫu |
|---|---|---|---|---|---|
| VP: từ chối tại VAL/VAH, TP/SL theo ATR | 3.0/1.5/48 | 1.02 | 151 lệnh · thắng 43% · PF 1.22 · 0.135%/lệnh · tổng 21% · sụt 14% · 0.5/ngày | 143 lệnh · thắng 39% · PF 1.08 · 0.059%/lệnh · tổng 6% · sụt 13% · 0.4/ngày | 151 lệnh · thắng 38% · PF 1.10 · 0.095%/lệnh · tổng 11% · sụt 16% · 0.5/ngày |
| VP: từ chối tại VAL/VAH, TP/SL theo ATR · lọc xu hướng ngày | 3.0/1.0/48 | 1.03 | 93 lệnh · thắng 32% · PF 1.29 · 0.130%/lệnh · tổng 12% · sụt 6% · 0.3/ngày | 86 lệnh · thắng 30% · PF 1.09 · 0.057%/lệnh · tổng 4% · sụt 8% · 0.3/ngày | 81 lệnh · thắng 27% · PF 1.01 · 0.010%/lệnh · tổng -0% · sụt 15% · 0.2/ngày |
| VP: từ chối tại VAL/VAH, chốt tại POC, dừng dưới nến | 1.0/0.5/48 | 0.89 | 200 lệnh · thắng 28% · PF 1.19 · 0.065%/lệnh · tổng 12% · sụt 15% · 0.6/ngày | 187 lệnh · thắng 22% · PF 0.73 · -0.122%/lệnh · tổng -21% · sụt 21% · 0.6/ngày | 225 lệnh · thắng 27% · PF 1.08 · 0.035%/lệnh · tổng 6% · sụt 16% · 0.7/ngày |
| VP: từ chối tại VAL/VAH, chốt tại POC, dừng dưới nến · lọc xu hướng ngày | 1.0/0.5/48 | 0.98 | 105 lệnh · thắng 30% · PF 1.07 · 0.023%/lệnh · tổng 2% · sụt 10% · 0.3/ngày | 103 lệnh · thắng 17% · PF 0.61 · -0.180%/lệnh · tổng -17% · sụt 18% · 0.3/ngày | 102 lệnh · thắng 27% · PF 0.89 · -0.047%/lệnh · tổng -5% · sụt 9% · 0.3/ngày |
| VP: lệnh chờ tại VAL/VAH (phí maker) | 1.0/1.5/8 | 1.19 | 250 lệnh · thắng 62% · PF 1.05 · 0.016%/lệnh · tổng 3% · sụt 10% · 0.8/ngày | 214 lệnh · thắng 64% · PF 1.30 · 0.111%/lệnh · tổng 25% · sụt 12% · 0.7/ngày | 250 lệnh · thắng 68% · PF 1.34 · 0.139%/lệnh · tổng 40% · sụt 9% · 0.8/ngày |
| VP: lệnh chờ tại VAL/VAH (phí maker) · lọc xu hướng ngày | 3.0/1.5/16 | 1.10 | 96 lệnh · thắng 42% · PF 1.11 · 0.050%/lệnh · tổng 4% · sụt 11% · 0.3/ngày | 98 lệnh · thắng 40% · PF 0.86 · -0.095%/lệnh · tổng -10% · sụt 12% · 0.3/ngày | 94 lệnh · thắng 39% · PF 0.92 · -0.058%/lệnh · tổng -7% · sụt 17% · 0.3/ngày |
| Hồi theo xu hướng 4h: RSI<40/EMA20 rồi vượt đỉnh nến trước | 3.0/1.0/16 | 0.96 | 252 lệnh · thắng 25% · PF 0.55 · -0.239%/lệnh · tổng -46% · sụt 47% · 0.8/ngày | 245 lệnh · thắng 27% · PF 0.79 · -0.134%/lệnh · tổng -30% · sụt 31% · 0.7/ngày | 231 lệnh · thắng 29% · PF 0.82 · -0.128%/lệnh · tổng -28% · sụt 34% · 0.7/ngày |
| Hồi theo xu hướng 4h: RSI<40/EMA20 rồi vượt đỉnh nến trước · lọc xu hướng ngày | 3.0/1.0/16 | 1.00 | 146 lệnh · thắng 24% · PF 0.53 · -0.260%/lệnh · tổng -32% · sụt 33% · 0.4/ngày | 146 lệnh · thắng 27% · PF 0.77 · -0.146%/lệnh · tổng -20% · sụt 21% · 0.4/ngày | 136 lệnh · thắng 29% · PF 0.84 · -0.121%/lệnh · tổng -17% · sụt 27% · 0.4/ngày |
| VWAP phiên: xuyên -1 sd rồi đóng lại | 3.0/1.0/48 | 0.85 | 528 lệnh · thắng 27% · PF 0.82 · -0.101%/lệnh · tổng -43% · sụt 44% · 1.6/ngày | 515 lệnh · thắng 29% · PF 0.95 · -0.039%/lệnh · tổng -24% · sụt 38% · 1.6/ngày | 493 lệnh · thắng 26% · PF 0.88 · -0.093%/lệnh · tổng -41% · sụt 47% · 1.5/ngày |
| VWAP phiên: xuyên -1 sd rồi đóng lại · lọc xu hướng ngày | 3.0/1.5/48 | 0.88 | 313 lệnh · thắng 34% · PF 0.85 · -0.099%/lệnh · tổng -29% · sụt 31% · 1.0/ngày | 297 lệnh · thắng 36% · PF 0.99 · -0.008%/lệnh · tổng -8% · sụt 24% · 0.9/ngày | 307 lệnh · thắng 34% · PF 0.95 · -0.043%/lệnh · tổng -18% · sụt 40% · 0.9/ngày |
| Nén Bollinger 48 nến rồi bung + khối lượng 1,5x | 3.0/1.5/48 | 1.09 | 113 lệnh · thắng 37% · PF 0.98 · -0.014%/lệnh · tổng -2% · sụt 11% · 0.3/ngày | 111 lệnh · thắng 35% · PF 1.08 · 0.064%/lệnh · tổng 5% · sụt 13% · 0.3/ngày | 105 lệnh · thắng 39% · PF 1.34 · 0.283%/lệnh · tổng 31% · sụt 9% · 0.3/ngày |
| Nén Bollinger 48 nến rồi bung + khối lượng 1,5x · lọc xu hướng ngày | 3.0/1.5/8 | 1.04 | 68 lệnh · thắng 47% · PF 1.18 · 0.071%/lệnh · tổng 5% · sụt 7% · 0.2/ngày | 65 lệnh · thắng 40% · PF 1.45 · 0.244%/lệnh · tổng 16% · sụt 8% · 0.2/ngày | 56 lệnh · thắng 46% · PF 1.35 · 0.230%/lệnh · tổng 13% · sụt 5% · 0.2/ngày |
| VP: thoát vùng qua node khối lượng thấp + khối lượng 1,2x | 3.0/1.5/48 | 1.07 | 78 lệnh · thắng 36% · PF 0.89 · -0.078%/lệnh · tổng -7% · sụt 16% · 0.2/ngày | 82 lệnh · thắng 43% · PF 1.21 · 0.166%/lệnh · tổng 13% · sụt 13% · 0.2/ngày | 74 lệnh · thắng 45% · PF 1.29 · 0.254%/lệnh · tổng 19% · sụt 15% · 0.2/ngày |
| VP: thoát vùng qua node khối lượng thấp + khối lượng 1,2x · lọc xu hướng ngày | 3.0/1.5/48 | 1.17 | 38 lệnh · thắng 34% · PF 0.77 · -0.189%/lệnh · tổng -7% · sụt 15% · 0.1/ngày | 41 lệnh · thắng 41% · PF 1.15 · 0.125%/lệnh · tổng 4% · sụt 10% · 0.1/ngày | 36 lệnh · thắng 44% · PF 1.42 · 0.364%/lệnh · tổng 13% · sụt 10% · 0.1/ngày |
| Bung biên độ 60 phút đầu ngày | 2.0/1.5/16 | 0.83 | 363 lệnh · thắng 44% · PF 0.84 · -0.083%/lệnh · tổng -28% · sụt 33% · 1.1/ngày | 363 lệnh · thắng 43% · PF 0.90 · -0.072%/lệnh · tổng -26% · sụt 36% · 1.1/ngày | 365 lệnh · thắng 40% · PF 0.75 · -0.220%/lệnh · tổng -58% · sụt 62% · 1.1/ngày |
| Bung biên độ 60 phút đầu ngày · lọc xu hướng ngày | 2.0/1.5/48 | 0.98 | 227 lệnh · thắng 43% · PF 0.83 · -0.102%/lệnh · tổng -22% · sụt 27% · 0.7/ngày | 223 lệnh · thắng 48% · PF 1.04 · 0.028%/lệnh · tổng 3% · sụt 16% · 0.7/ngày | 230 lệnh · thắng 39% · PF 0.80 · -0.192%/lệnh · tổng -38% · sụt 46% · 0.7/ngày |
