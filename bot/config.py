"""Cấu hình bộ chỉ báo. Ngưỡng chỉnh cho phong cách swing (khung 4h và 1D)."""

SYMBOLS = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
SHORT = {"BTCUSDT": "BTC", "ETHUSDT": "ETH", "SOLUSDT": "SOL"}
DVOL_CURRENCIES = {"BTCUSDT": "BTC", "ETHUSDT": "ETH"}  # Deribit chỉ có BTC, ETH

MAIN_TF = "4h"        # khung chính cho swing
HIGHER_TF = "1d"      # khung xác nhận xu hướng
KLINE_LIMIT = 200     # đủ cho EMA50, ADX14, BBW 30 ngày (180 nến 4h)
DAILY_LIMIT = 200     # nến ngày: EMA50, nén 120 ngày

# Ngưỡng cảnh báo theo từng đồng (% thay đổi giá 4h)
PRICE_MOVE_4H = {"BTCUSDT": 3.0, "ETHUSDT": 4.0, "SOLUSDT": 6.0}

ATR_SPIKE_RATIO = 2.0       # ATR(14) hiện tại / trung bình ATR 7 ngày (42 nến 4h)
RV_ZSCORE = 2.0             # z-score biến động thực 24h so với 30 ngày
BBW_SQUEEZE_LOOKBACK = 180  # 30 ngày nến 4h
VOLUME_RATIO = 3.0          # khối lượng nến / trung bình 20 nến
OI_CHANGE_4H = 5.0          # % thay đổi OI trong 4h
OI_CHANGE_24H = 10.0        # % thay đổi OI trong 24h
FUNDING_HOT = 0.0005        # 0,05% mỗi 8h: long quá nóng
FUNDING_COLD = -0.0003      # -0,03% mỗi 8h: short quá đông
LS_RATIO_HIGH = 2.5
LS_RATIO_LOW = 0.6
TAKER_HIGH = 1.4
TAKER_LOW = 0.7
DVOL_RV_GAP = 15.0          # điểm chênh DVOL so với realized vol quy năm

# Xu hướng rõ: EMA20 > EMA50 (hoặc ngược), ADX14 trên ngưỡng, giá cùng phía EMA20
ADX_TREND = 25.0
ADX_STRONG = 35.0

SCORE_WEIGHTS = {"price": 0.40, "deriv": 0.35, "expect": 0.25}
SCORE_HIGH = 70
SCORE_LOW = 30

ALERT_COOLDOWN_MIN = 240    # cùng một cảnh báo không lặp lại trong 4 giờ

# Tín hiệu khung ngày (theo backtest 6 năm: cắt EMA20/50 ngày có lãi ổn định cả 3 đồng)
DAILY_ATR_STOP = 3.5            # dừng lỗ gợi ý = giá vào -/+ 3,5 ATR(14) ngày
DAILY_SQUEEZE_LOOKBACK = 120    # nén: BBW hẹp nhất 120 ngày trong 5 nến gần
DAILY_SQUEEZE_SYMBOLS = ["ETHUSDT", "SOLUSDT"]  # backtest thất bại ở BTC nên bỏ

# Volume profile (backtest: thoát vùng giá trị là cách duy nhất có lãi cả 3 đồng trên 4h)
VP_WINDOW_4H = 180   # 30 ngày nến 4h
VP_WINDOW_1D = 90    # 90 ngày nến ngày
VP_BIN_PCT = 0.002
VP_VALUE_AREA = 0.70
