# Scalp · khung 15m · tối ưu trong mẫu 70% đầu, kiểm tra ngoài mẫu 30% cuối

Cột: số lệnh | thắng | profit factor | lãi/lệnh | tổng lãi | sụt giảm | lệnh/ngày. Phí: taker 0,05% mỗi chiều; lệnh chờ 0,02% vào + 0,05% ra. 'Mặc định' = TP 1,5 / SL 1 / giữ 16 nến không tối ưu. 'Tốt nhất trong mẫu' chọn theo PF với >= 40 lệnh; nếu không tổ hợp nào đạt PF > 1,1 thì bỏ trống.

## BTC · 105119 nến · 2023-10-18 đến 2026-10-17 · ngoài mẫu từ nến thứ 73583

| Chiến lược | Tín hiệu | Tham số tốt nhất (TP/SL/giữ) | Trong mẫu | Ngoài mẫu (cùng tham số) | Ngoài mẫu, mặc định |
|---|---|---|---|---|---|
| VP: từ chối tại VAL/VAH, TP/SL theo ATR | 5398 | không có | 0 lệnh | 0 lệnh | 999 lệnh · thắng 38% · PF 0.60 · -0.096%/lệnh · tổng -62% · sụt 62% · 3.0/ngày |
| VP: từ chối tại VAL/VAH, TP/SL theo ATR · lọc xu hướng ngày | 2760 | không có | 0 lệnh | 0 lệnh | 512 lệnh · thắng 36% · PF 0.55 · -0.110%/lệnh · tổng -43% · sụt 43% · 1.6/ngày |
| VP: từ chối tại VAL/VAH, chốt tại POC, dừng dưới nến | 5398 | không có | 0 lệnh | 0 lệnh | 1094 lệnh · thắng 25% · PF 0.45 · -0.110%/lệnh · tổng -70% · sụt 70% · 3.3/ngày |
| VP: từ chối tại VAL/VAH, chốt tại POC, dừng dưới nến · lọc xu hướng ngày | 2760 | không có | 0 lệnh | 0 lệnh | 559 lệnh · thắng 22% · PF 0.39 · -0.127%/lệnh · tổng -51% · sụt 51% · 1.7/ngày |
| VP: lệnh chờ tại VAL/VAH (phí maker) | 9223 | không có | 0 lệnh | 0 lệnh | 1268 lệnh · thắng 38% · PF 0.66 · -0.075%/lệnh · tổng -62% · sụt 62% · 3.9/ngày |
| VP: lệnh chờ tại VAL/VAH (phí maker) · lọc xu hướng ngày | 4683 | không có | 0 lệnh | 0 lệnh | 653 lệnh · thắng 37% · PF 0.64 · -0.079%/lệnh · tổng -41% · sụt 41% · 2.0/ngày |
| Hồi theo xu hướng 4h: RSI<40/EMA20 rồi vượt đỉnh nến trước | 4015 | không có | 0 lệnh | 0 lệnh | 886 lệnh · thắng 38% · PF 0.52 · -0.114%/lệnh · tổng -64% · sụt 64% · 2.7/ngày |
| Hồi theo xu hướng 4h: RSI<40/EMA20 rồi vượt đỉnh nến trước · lọc xu hướng ngày | 2542 | không có | 0 lệnh | 0 lệnh | 534 lệnh · thắng 39% · PF 0.56 · -0.109%/lệnh · tổng -44% · sụt 44% · 1.6/ngày |
| VWAP phiên: xuyên -1 sd rồi đóng lại | 14309 | không có | 0 lệnh | 0 lệnh | 2416 lệnh · thắng 39% · PF 0.57 · -0.101%/lệnh · tổng -92% · sụt 92% · 7.4/ngày |
| VWAP phiên: xuyên -1 sd rồi đóng lại · lọc xu hướng ngày | 7058 | không có | 0 lệnh | 0 lệnh | 1320 lệnh · thắng 39% · PF 0.57 · -0.101%/lệnh · tổng -74% · sụt 74% · 4.0/ngày |
| Nén Bollinger 48 nến rồi bung + khối lượng 1,5x | 2748 | không có | 0 lệnh | 0 lệnh | 508 lệnh · thắng 37% · PF 0.48 · -0.117%/lệnh · tổng -45% · sụt 45% · 1.5/ngày |
| Nén Bollinger 48 nến rồi bung + khối lượng 1,5x · lọc xu hướng ngày | 1376 | không có | 0 lệnh | 0 lệnh | 259 lệnh · thắng 39% · PF 0.55 · -0.101%/lệnh · tổng -23% · sụt 23% · 0.8/ngày |
| VP: thoát vùng qua node khối lượng thấp + khối lượng 1,2x | 1884 | không có | 0 lệnh | 0 lệnh | 569 lệnh · thắng 40% · PF 0.55 · -0.107%/lệnh · tổng -46% · sụt 46% · 1.7/ngày |
| VP: thoát vùng qua node khối lượng thấp + khối lượng 1,2x · lọc xu hướng ngày | 947 | không có | 0 lệnh | 0 lệnh | 299 lệnh · thắng 40% · PF 0.55 · -0.110%/lệnh · tổng -28% · sụt 28% · 0.9/ngày |
| Bung biên độ 60 phút đầu ngày | 1795 | không có | 0 lệnh | 0 lệnh | 532 lệnh · thắng 37% · PF 0.59 · -0.094%/lệnh · tổng -40% · sụt 40% · 1.6/ngày |
| Bung biên độ 60 phút đầu ngày · lọc xu hướng ngày | 890 | không có | 0 lệnh | 0 lệnh | 270 lệnh · thắng 39% · PF 0.66 · -0.073%/lệnh · tổng -18% · sụt 18% · 0.8/ngày |

## ETH · 105119 nến · 2023-10-18 đến 2026-10-17 · ngoài mẫu từ nến thứ 73583

| Chiến lược | Tín hiệu | Tham số tốt nhất (TP/SL/giữ) | Trong mẫu | Ngoài mẫu (cùng tham số) | Ngoài mẫu, mặc định |
|---|---|---|---|---|---|
| VP: từ chối tại VAL/VAH, TP/SL theo ATR | 5822 | không có | 0 lệnh | 0 lệnh | 1055 lệnh · thắng 42% · PF 0.74 · -0.075%/lệnh · tổng -55% · sụt 57% · 3.2/ngày |
| VP: từ chối tại VAL/VAH, TP/SL theo ATR · lọc xu hướng ngày | 3052 | không có | 0 lệnh | 0 lệnh | 523 lệnh · thắng 40% · PF 0.69 · -0.092%/lệnh · tổng -39% · sụt 40% · 1.6/ngày |
| VP: từ chối tại VAL/VAH, chốt tại POC, dừng dưới nến | 5822 | không có | 0 lệnh | 0 lệnh | 1166 lệnh · thắng 32% · PF 0.66 · -0.075%/lệnh · tổng -59% · sụt 61% · 3.5/ngày |
| VP: từ chối tại VAL/VAH, chốt tại POC, dừng dưới nến · lọc xu hướng ngày | 3052 | không có | 0 lệnh | 0 lệnh | 584 lệnh · thắng 32% · PF 0.68 · -0.073%/lệnh · tổng -35% · sụt 35% · 1.8/ngày |
| VP: lệnh chờ tại VAL/VAH (phí maker) | 9443 | không có | 0 lệnh | 0 lệnh | 1253 lệnh · thắng 40% · PF 0.77 · -0.064%/lệnh · tổng -56% · sụt 59% · 3.8/ngày |
| VP: lệnh chờ tại VAL/VAH (phí maker) · lọc xu hướng ngày | 4916 | không có | 0 lệnh | 0 lệnh | 647 lệnh · thắng 40% · PF 0.76 · -0.066%/lệnh · tổng -35% · sụt 37% · 2.0/ngày |
| Hồi theo xu hướng 4h: RSI<40/EMA20 rồi vượt đỉnh nến trước | 3686 | không có | 0 lệnh | 0 lệnh | 894 lệnh · thắng 39% · PF 0.62 · -0.112%/lệnh · tổng -64% · sụt 64% · 2.7/ngày |
| Hồi theo xu hướng 4h: RSI<40/EMA20 rồi vượt đỉnh nến trước · lọc xu hướng ngày | 2410 | không có | 0 lệnh | 0 lệnh | 562 lệnh · thắng 39% · PF 0.66 · -0.103%/lệnh · tổng -44% · sụt 45% · 1.7/ngày |
| VWAP phiên: xuyên -1 sd rồi đóng lại | 14290 | không có | 0 lệnh | 0 lệnh | 2471 lệnh · thắng 39% · PF 0.62 · -0.113%/lệnh · tổng -94% · sụt 94% · 7.5/ngày |
| VWAP phiên: xuyên -1 sd rồi đóng lại · lọc xu hướng ngày | 7204 | không có | 0 lệnh | 0 lệnh | 1279 lệnh · thắng 40% · PF 0.68 · -0.092%/lệnh · tổng -70% · sụt 70% · 3.9/ngày |
| Nén Bollinger 48 nến rồi bung + khối lượng 1,5x | 2768 | không có | 0 lệnh | 0 lệnh | 515 lệnh · thắng 42% · PF 0.71 · -0.076%/lệnh · tổng -33% · sụt 34% · 1.6/ngày |
| Nén Bollinger 48 nến rồi bung + khối lượng 1,5x · lọc xu hướng ngày | 1367 | không có | 0 lệnh | 0 lệnh | 258 lệnh · thắng 41% · PF 0.73 · -0.072%/lệnh · tổng -17% · sụt 18% · 0.8/ngày |
| VP: thoát vùng qua node khối lượng thấp + khối lượng 1,2x | 1902 | không có | 0 lệnh | 0 lệnh | 546 lệnh · thắng 41% · PF 0.65 · -0.111%/lệnh · tổng -46% · sụt 47% · 1.7/ngày |
| VP: thoát vùng qua node khối lượng thấp + khối lượng 1,2x · lọc xu hướng ngày | 969 | không có | 0 lệnh | 0 lệnh | 274 lệnh · thắng 41% · PF 0.69 · -0.101%/lệnh · tổng -24% · sụt 26% · 0.8/ngày |
| Bung biên độ 60 phút đầu ngày | 1759 | không có | 0 lệnh | 0 lệnh | 517 lệnh · thắng 36% · PF 0.61 · -0.117%/lệnh · tổng -46% · sụt 47% · 1.6/ngày |
| Bung biên độ 60 phút đầu ngày · lọc xu hướng ngày | 872 | không có | 0 lệnh | 0 lệnh | 270 lệnh · thắng 37% · PF 0.69 · -0.089%/lệnh · tổng -22% · sụt 22% · 0.8/ngày |

## SOL · 105119 nến · 2023-10-18 đến 2026-10-17 · ngoài mẫu từ nến thứ 73583

| Chiến lược | Tín hiệu | Tham số tốt nhất (TP/SL/giữ) | Trong mẫu | Ngoài mẫu (cùng tham số) | Ngoài mẫu, mặc định |
|---|---|---|---|---|---|
| VP: từ chối tại VAL/VAH, TP/SL theo ATR | 5855 | không có | 0 lệnh | 0 lệnh | 1059 lệnh · thắng 37% · PF 0.63 · -0.130%/lệnh · tổng -75% · sụt 75% · 3.2/ngày |
| VP: từ chối tại VAL/VAH, TP/SL theo ATR · lọc xu hướng ngày | 3017 | không có | 0 lệnh | 0 lệnh | 566 lệnh · thắng 35% · PF 0.56 · -0.157%/lệnh · tổng -59% · sụt 59% · 1.7/ngày |
| VP: từ chối tại VAL/VAH, chốt tại POC, dừng dưới nến | 5855 | không có | 0 lệnh | 0 lệnh | 1220 lệnh · thắng 26% · PF 0.57 · -0.109%/lệnh · tổng -74% · sụt 74% · 3.7/ngày |
| VP: từ chối tại VAL/VAH, chốt tại POC, dừng dưới nến · lọc xu hướng ngày | 3017 | không có | 0 lệnh | 0 lệnh | 653 lệnh · thắng 25% · PF 0.51 · -0.122%/lệnh · tổng -55% · sụt 55% · 2.0/ngày |
| VP: lệnh chờ tại VAL/VAH (phí maker) | 9528 | không có | 0 lệnh | 0 lệnh | 1312 lệnh · thắng 39% · PF 0.73 · -0.088%/lệnh · tổng -69% · sụt 70% · 4.0/ngày |
| VP: lệnh chờ tại VAL/VAH (phí maker) · lọc xu hướng ngày | 4897 | không có | 0 lệnh | 0 lệnh | 709 lệnh · thắng 39% · PF 0.71 · -0.089%/lệnh · tổng -47% · sụt 48% · 2.2/ngày |
| Hồi theo xu hướng 4h: RSI<40/EMA20 rồi vượt đỉnh nến trước | 3690 | không có | 0 lệnh | 0 lệnh | 872 lệnh · thắng 44% · PF 0.80 · -0.061%/lệnh · tổng -42% · sụt 45% · 2.7/ngày |
| Hồi theo xu hướng 4h: RSI<40/EMA20 rồi vượt đỉnh nến trước · lọc xu hướng ngày | 2242 | không có | 0 lệnh | 0 lệnh | 507 lệnh · thắng 42% · PF 0.78 · -0.072%/lệnh · tổng -31% · sụt 33% · 1.5/ngày |
| VWAP phiên: xuyên -1 sd rồi đóng lại | 14001 | không có | 0 lệnh | 0 lệnh | 2385 lệnh · thắng 41% · PF 0.71 · -0.093%/lệnh · tổng -90% · sụt 91% · 7.3/ngày |
| VWAP phiên: xuyên -1 sd rồi đóng lại · lọc xu hướng ngày | 6932 | không có | 0 lệnh | 0 lệnh | 1321 lệnh · thắng 40% · PF 0.71 · -0.093%/lệnh · tổng -71% · sụt 74% · 4.0/ngày |
| Nén Bollinger 48 nến rồi bung + khối lượng 1,5x | 2492 | không có | 0 lệnh | 0 lệnh | 475 lệnh · thắng 38% · PF 0.65 · -0.110%/lệnh · tổng -41% · sụt 43% · 1.4/ngày |
| Nén Bollinger 48 nến rồi bung + khối lượng 1,5x · lọc xu hướng ngày | 1221 | không có | 0 lệnh | 0 lệnh | 249 lệnh · thắng 37% · PF 0.61 · -0.128%/lệnh · tổng -28% · sụt 29% · 0.8/ngày |
| VP: thoát vùng qua node khối lượng thấp + khối lượng 1,2x | 1839 | không có | 0 lệnh | 0 lệnh | 522 lệnh · thắng 40% · PF 0.70 · -0.101%/lệnh · tổng -42% · sụt 45% · 1.6/ngày |
| VP: thoát vùng qua node khối lượng thấp + khối lượng 1,2x · lọc xu hướng ngày | 911 | 3.0/1.5/16 | 558 lệnh · thắng 41% · PF 1.10 · 0.061%/lệnh · tổng 33% · sụt 31% · 0.7/ngày | 252 lệnh · thắng 35% · PF 0.79 · -0.104%/lệnh · tổng -24% · sụt 33% · 0.8/ngày | 266 lệnh · thắng 41% · PF 0.78 · -0.073%/lệnh · tổng -18% · sụt 23% · 0.8/ngày |
| Bung biên độ 60 phút đầu ngày | 1793 | không có | 0 lệnh | 0 lệnh | 530 lệnh · thắng 40% · PF 0.67 · -0.111%/lệnh · tổng -45% · sụt 46% · 1.6/ngày |
| Bung biên độ 60 phút đầu ngày · lọc xu hướng ngày | 902 | không có | 0 lệnh | 0 lệnh | 269 lệnh · thắng 39% · PF 0.70 · -0.097%/lệnh · tổng -23% · sụt 25% · 0.8/ngày |

## Tham số chung cho cả 3 đồng (chọn trong mẫu theo PF trung bình, kiểm tra ngoài mẫu từng đồng)

| Chiến lược | TP/SL/giữ | PF TB trong mẫu | BTC ngoài mẫu | ETH ngoài mẫu | SOL ngoài mẫu |
|---|---|---|---|---|---|
| VP: từ chối tại VAL/VAH, TP/SL theo ATR | 3.0/1.5/48 | 0.79 | 756 lệnh · thắng 33% · PF 0.71 · -0.107%/lệnh · tổng -56% · sụt 57% · 2.3/ngày | 769 lệnh · thắng 36% · PF 0.82 · -0.085%/lệnh · tổng -50% · sụt 54% · 2.3/ngày | 803 lệnh · thắng 33% · PF 0.77 · -0.122%/lệnh · tổng -64% · sụt 65% · 2.4/ngày |
| VP: từ chối tại VAL/VAH, TP/SL theo ATR · lọc xu hướng ngày | 3.0/1.5/48 | 0.75 | 409 lệnh · thắng 34% · PF 0.71 · -0.101%/lệnh · tổng -35% · sụt 35% · 1.2/ngày | 415 lệnh · thắng 35% · PF 0.80 · -0.091%/lệnh · tổng -33% · sụt 39% · 1.3/ngày | 447 lệnh · thắng 31% · PF 0.70 · -0.162%/lệnh · tổng -53% · sụt 53% · 1.4/ngày |
| VP: từ chối tại VAL/VAH, chốt tại POC, dừng dưới nến | 1.0/0.5/48 | 0.57 | 1085 lệnh · thắng 24% · PF 0.50 · -0.103%/lệnh · tổng -68% · sụt 68% · 3.3/ngày | 1136 lệnh · thắng 30% · PF 0.68 · -0.077%/lệnh · tổng -59% · sụt 60% · 3.5/ngày | 1206 lệnh · thắng 25% · PF 0.61 · -0.103%/lệnh · tổng -72% · sụt 72% · 3.7/ngày |
| VP: từ chối tại VAL/VAH, chốt tại POC, dừng dưới nến · lọc xu hướng ngày | 1.0/0.5/48 | 0.54 | 554 lệnh · thắng 22% · PF 0.40 · -0.125%/lệnh · tổng -50% · sụt 50% · 1.7/ngày | 574 lệnh · thắng 30% · PF 0.70 · -0.071%/lệnh · tổng -34% · sụt 35% · 1.7/ngày | 651 lệnh · thắng 24% · PF 0.50 · -0.129%/lệnh · tổng -57% · sụt 57% · 2.0/ngày |
| VP: lệnh chờ tại VAL/VAH (phí maker) | 1.0/1.5/48 | 0.88 | 1284 lệnh · thắng 63% · PF 0.84 · -0.030%/lệnh · tổng -33% · sụt 35% · 3.9/ngày | 1281 lệnh · thắng 63% · PF 0.88 · -0.031%/lệnh · tổng -34% · sụt 40% · 3.9/ngày | 1338 lệnh · thắng 61% · PF 0.83 · -0.049%/lệnh · tổng -49% · sụt 50% · 4.1/ngày |
| VP: lệnh chờ tại VAL/VAH (phí maker) · lọc xu hướng ngày | 1.0/1.5/48 | 0.91 | 656 lệnh · thắng 62% · PF 0.80 · -0.038%/lệnh · tổng -22% · sụt 24% · 2.0/ngày | 663 lệnh · thắng 63% · PF 0.92 · -0.019%/lệnh · tổng -13% · sụt 19% · 2.0/ngày | 725 lệnh · thắng 62% · PF 0.85 · -0.041%/lệnh · tổng -27% · sụt 27% · 2.2/ngày |
| Hồi theo xu hướng 4h: RSI<40/EMA20 rồi vượt đỉnh nến trước | 3.0/1.5/48 | 0.87 | 657 lệnh · thắng 35% · PF 0.75 · -0.090%/lệnh · tổng -46% · sụt 48% · 2.0/ngày | 647 lệnh · thắng 34% · PF 0.78 · -0.101%/lệnh · tổng -50% · sụt 53% · 2.0/ngày | 667 lệnh · thắng 36% · PF 0.93 · -0.036%/lệnh · tổng -24% · sụt 28% · 2.0/ngày |
| Hồi theo xu hướng 4h: RSI<40/EMA20 rồi vượt đỉnh nến trước · lọc xu hướng ngày | 3.0/1.5/48 | 0.86 | 400 lệnh · thắng 36% · PF 0.76 · -0.089%/lệnh · tổng -31% · sụt 31% · 1.2/ngày | 403 lệnh · thắng 35% · PF 0.87 · -0.061%/lệnh · tổng -24% · sụt 32% · 1.2/ngày | 392 lệnh · thắng 35% · PF 0.89 · -0.059%/lệnh · tổng -23% · sụt 29% · 1.2/ngày |
| VWAP phiên: xuyên -1 sd rồi đóng lại | 3.0/1.5/48 | 0.78 | 1457 lệnh · thắng 35% · PF 0.75 · -0.093%/lệnh · tổng -75% · sụt 76% · 4.4/ngày | 1386 lệnh · thắng 35% · PF 0.76 · -0.113%/lệnh · tổng -80% · sụt 83% · 4.2/ngày | 1420 lệnh · thắng 35% · PF 0.80 · -0.104%/lệnh · tổng -79% · sụt 84% · 4.3/ngày |
| VWAP phiên: xuyên -1 sd rồi đóng lại · lọc xu hướng ngày | 3.0/1.5/48 | 0.77 | 932 lệnh · thắng 34% · PF 0.71 · -0.104%/lệnh · tổng -63% · sụt 63% · 2.8/ngày | 859 lệnh · thắng 37% · PF 0.90 · -0.045%/lệnh · tổng -35% · sụt 39% · 2.6/ngày | 898 lệnh · thắng 34% · PF 0.81 · -0.098%/lệnh · tổng -61% · sụt 67% · 2.7/ngày |
| Nén Bollinger 48 nến rồi bung + khối lượng 1,5x | 2.0/1.5/48 | 0.80 | 459 lệnh · thắng 42% · PF 0.62 · -0.112%/lệnh · tổng -40% · sụt 41% · 1.4/ngày | 466 lệnh · thắng 45% · PF 0.76 · -0.086%/lệnh · tổng -34% · sụt 37% · 1.4/ngày | 428 lệnh · thắng 41% · PF 0.76 · -0.103%/lệnh · tổng -36% · sụt 40% · 1.3/ngày |
| Nén Bollinger 48 nến rồi bung + khối lượng 1,5x · lọc xu hướng ngày | 3.0/1.5/48 | 0.76 | 225 lệnh · thắng 36% · PF 0.68 · -0.108%/lệnh · tổng -22% · sụt 25% · 0.7/ngày | 224 lệnh · thắng 37% · PF 0.91 · -0.034%/lệnh · tổng -8% · sụt 15% · 0.7/ngày | 217 lệnh · thắng 30% · PF 0.70 · -0.153%/lệnh · tổng -29% · sụt 29% · 0.7/ngày |
| VP: thoát vùng qua node khối lượng thấp + khối lượng 1,2x | 3.0/1.5/16 | 0.89 | 532 lệnh · thắng 36% · PF 0.72 · -0.088%/lệnh · tổng -38% · sụt 39% · 1.6/ngày | 512 lệnh · thắng 37% · PF 0.77 · -0.101%/lệnh · tổng -42% · sụt 46% · 1.6/ngày | 495 lệnh · thắng 36% · PF 0.78 · -0.103%/lệnh · tổng -41% · sụt 50% · 1.5/ngày |
| VP: thoát vùng qua node khối lượng thấp + khối lượng 1,2x · lọc xu hướng ngày | 3.0/1.5/48 | 0.93 | 275 lệnh · thắng 35% · PF 0.73 · -0.096%/lệnh · tổng -24% · sụt 24% · 0.8/ngày | 250 lệnh · thắng 38% · PF 0.93 · -0.035%/lệnh · tổng -10% · sụt 19% · 0.8/ngày | 241 lệnh · thắng 34% · PF 0.79 · -0.112%/lệnh · tổng -25% · sụt 32% · 0.7/ngày |
| Bung biên độ 60 phút đầu ngày | 3.0/1.5/48 | 0.83 | 503 lệnh · thắng 29% · PF 0.60 · -0.151%/lệnh · tổng -54% · sụt 54% · 1.5/ngày | 484 lệnh · thắng 34% · PF 0.82 · -0.078%/lệnh · tổng -33% · sụt 39% · 1.5/ngày | 499 lệnh · thắng 31% · PF 0.73 · -0.140%/lệnh · tổng -52% · sụt 54% · 1.5/ngày |
| Bung biên độ 60 phút đầu ngày · lọc xu hướng ngày | 3.0/1.5/48 | 0.92 | 270 lệnh · thắng 33% · PF 0.71 · -0.103%/lệnh · tổng -25% · sụt 25% · 0.8/ngày | 269 lệnh · thắng 38% · PF 1.02 · 0.006%/lệnh · tổng 1% · sụt 12% · 0.8/ngày | 268 lệnh · thắng 34% · PF 0.87 · -0.062%/lệnh · tổng -17% · sụt 26% · 0.8/ngày |
