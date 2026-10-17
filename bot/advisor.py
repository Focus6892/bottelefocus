"""Agent đề xuất: gom tín hiệu nhiều biểu đồ (ngày, 4h, volume profile, dominance) thành một khuyến nghị cho mỗi đồng.

Mỗi nguồn cho một hướng (+1 lên, -1 xuống, 0 trung lập) và một trọng số lấy theo độ tin cậy trong backtest
(profit factor càng cao, trọng số càng lớn). Điểm = tổng(trọng số × hướng) / tổng(trọng số), từ -1 đến 1.
"""
from . import config as C

# Trọng số mặc định theo backtest (bot/README). Reviewer có thể hạ trọng số nếu backtest của đồng đó yếu.
WEIGHTS = {
    "daily_regime": 3.0,   # cắt EMA20/50 ngày: PF 2,4-3,2 cả 3 đồng
    "vp_1d": 2.0,          # thoát vùng giá trị 90 ngày: PF 1,7-2,9; có xác nhận RSI+KL: 2,0-3,9 (x1,5)
    "vp_4h": 1.5,          # thoát vùng 30 ngày trên 4h: PF 1,2-1,7
    "inside_4h": 1.5,      # inside bar 4h theo EMA: PF 1,4-1,7
    "ichimoku_1d": 2.0,    # Ichimoku ngày: PF 2,2-3,0 cả 3 đồng, 24 tháng gần nhất dương
    "weinstein_1d": 1.5,   # SMA30 ngày dốc + giá cùng phía, áp lên 4h: PF 1,6-1,9
    "trend_4h": 1.0,       # pha 4h EMA+ADX: không có lợi thế, chỉ bối cảnh
    "dominance": 1.0,      # dòng tiền chung: quy tắc kinh điển, chưa backtest
    "vp_lean": 1.0,        # thiên hướng 24h từ thống kê volume profile (chỉ khi lệch nền có ý nghĩa)
}
LONG_AT, SHORT_AT = 0.35, -0.35

DOM_BIAS = {  # regime -> {BTC, ETH, SOL}
    "risk_off_alt": {"BTC": -0.5, "ETH": -1, "SOL": -1},
    "risk_off": {"BTC": -1, "ETH": -1, "SOL": -1},
    "alt_season": {"BTC": 0, "ETH": 1, "SOL": 1},
    "risk_on_large": {"BTC": 0, "ETH": 1, "SOL": 0.5},
    "btc_season": {"BTC": 1, "ETH": -0.5, "SOL": -0.5},
    "alt_rotation": {"BTC": -0.5, "ETH": 0.5, "SOL": 1},
    "btc_strength": {"BTC": 0.5, "ETH": -0.5, "SOL": -0.5},
    "neutral": {"BTC": 0, "ETH": 0, "SOL": 0},
}


def sources(r, ana):
    """Danh sách nguồn: (mã, hướng, trọng số, mô tả ngắn)."""
    out = []
    d = r.get("daily") or {}
    if d.get("regime"):
        out.append(("daily_regime", 1 if d["regime"] == "up" else -1, WEIGHTS["daily_regime"], f"EMA20/50 ngày {'tăng' if d['regime'] == 'up' else 'giảm'} {d.get('bars_in_regime', 0)} ngày"))
    v1 = r.get("vp_1d") or {}
    if v1.get("state") in ("above", "below"):
        w = WEIGHTS["vp_1d"] * (1.5 if v1.get("confirmed") else 1.0)
        out.append(("vp_1d", 1 if v1["state"] == "above" else -1, w, f"giá {'trên' if v1['state'] == 'above' else 'dưới'} vùng giá trị 90 ngày" + (" (có xác nhận RSI + KL)" if v1.get("confirmed") else "")))
    v4 = r.get("vp_4h") or {}
    if v4.get("state") in ("above", "below"):
        out.append(("vp_4h", 1 if v4["state"] == "above" else -1, WEIGHTS["vp_4h"], f"giá {'trên' if v4['state'] == 'above' else 'dưới'} vùng giá trị 30 ngày (4h)"))
    for code, label in (("ichimoku_1d", "Ichimoku ngày"), ("weinstein_1d", "SMA30 ngày (Weinstein)")):
        st = r.get(code)
        if st in ("up", "down"):
            out.append((code, 1 if st == "up" else -1, WEIGHTS[code], f"{label} {'tăng' if st == 'up' else 'giảm'}"))
    ib = r.get("inside_4h")
    if ib:
        out.append(("inside_4h", ib["dir"], WEIGHTS["inside_4h"], f"inside bar 4h bung {'lên' if ib['dir'] == 1 else 'xuống'}"))
    if r.get("trend") in ("up", "down"):
        out.append(("trend_4h", 1 if r["trend"] == "up" else -1, WEIGHTS["trend_4h"], f"pha 4h {'tăng' if r['trend'] == 'up' else 'giảm'} (ADX {r.get('adx') or 0:.0f})"))
    fc = ((r.get("vp_forecast") or {}).get("forecast") or {}).get("24 giờ tới")
    if fc and fc["lean"] != "không rõ hướng":
        out.append(("vp_lean", 1 if fc["lean"] == "nghiêng tăng" else -1, WEIGHTS["vp_lean"], f"thống kê VP 24h {fc['lean']} ({fc['d_up']*100:+.0f} điểm)"))
    if ana:
        b = DOM_BIAS.get(ana["regime"], DOM_BIAS["neutral"]).get(r["name"], 0)
        if b:
            out.append(("dominance", b, WEIGHTS["dominance"], f"dòng tiền: {ana['text'].lower()}"))
    return out


def score(srcs):
    tw = sum(w for _, _, w, _ in srcs)
    return sum(d * w for _, d, w, _ in srcs) / tw if tw else 0.0


def recommend(r, ana, srcs=None):
    srcs = srcs if srcs is not None else sources(r, ana)
    s = score(srcs)
    side = "LONG" if s >= LONG_AT else "SHORT" if s <= SHORT_AT else "NGOÀI"
    d = r.get("daily") or {}
    price = r["price"]
    if side == "NGOÀI":
        stop = None
    elif d.get("stop") and ((side == "LONG") == (d.get("regime") == "up")):
        stop = d["stop"]  # cùng chiều khung ngày: dừng lỗ 3,5 ATR ngày
    else:
        atr = price * (r.get("atr_pct") or 2.0) / 100
        stop = price - 2 * atr if side == "LONG" else price + 2 * atr  # ngược khung ngày: dừng lỗ chặt 2 ATR 4h
    return {
        "symbol": r["symbol"], "name": r["name"], "side": side, "score": round(s, 3), "confidence": round(abs(s), 2),
        "price": price, "stop": stop, "sources": srcs,
        "for": [x for x in srcs if x[1] * (1 if s >= 0 else -1) > 0], "against": [x for x in srcs if x[1] * (1 if s >= 0 else -1) < 0],
    }
