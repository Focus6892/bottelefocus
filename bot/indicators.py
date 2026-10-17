"""Tính toán chỉ báo từ nến và dữ liệu phái sinh. Chỉ dùng thư viện chuẩn."""
import math
from statistics import mean, pstdev

from . import config as C


# ---------- tiện ích ----------
def ema(values, n):
    k = 2 / (n + 1)
    out = []
    e = None
    for v in values:
        e = v if e is None else v * k + e * (1 - k)
        out.append(e)
    return out


def true_ranges(k):
    tr = [k[0]["h"] - k[0]["l"]]
    for i in range(1, len(k)):
        tr.append(max(k[i]["h"] - k[i]["l"], abs(k[i]["h"] - k[i - 1]["c"]), abs(k[i]["l"] - k[i - 1]["c"])))
    return tr


def wilder(values, n):
    """Làm mượt kiểu Wilder (dùng cho ATR, ADX)."""
    out = []
    s = None
    for i, v in enumerate(values):
        if i < n - 1:
            out.append(None)
            continue
        if s is None:
            s = mean(values[: n])
        else:
            s = (s * (n - 1) + v) / n
        out.append(s)
    return out


def atr_pct(k, n=14):
    a = wilder(true_ranges(k), n)
    return [None if x is None else x / k[i]["c"] * 100 for i, x in enumerate(a)]


def adx(k, n=14):
    """Trả về (adx, +di, -di) tại nến cuối."""
    tr = true_ranges(k)
    plus, minus = [0.0], [0.0]
    for i in range(1, len(k)):
        up = k[i]["h"] - k[i - 1]["h"]
        dn = k[i - 1]["l"] - k[i]["l"]
        plus.append(up if up > dn and up > 0 else 0.0)
        minus.append(dn if dn > up and dn > 0 else 0.0)
    tr_s, p_s, m_s = wilder(tr, n), wilder(plus, n), wilder(minus, n)
    dx = []
    for t, p, m in zip(tr_s, p_s, m_s):
        if t is None or t == 0:
            dx.append(None)
            continue
        pdi, mdi = 100 * p / t, 100 * m / t
        dx.append(100 * abs(pdi - mdi) / (pdi + mdi) if pdi + mdi else 0.0)
    valid = [x for x in dx if x is not None]
    a = wilder(valid, n)
    pdi = 100 * p_s[-1] / tr_s[-1] if tr_s[-1] else 0.0
    mdi = 100 * m_s[-1] / tr_s[-1] if tr_s[-1] else 0.0
    return (a[-1] if a and a[-1] is not None else None), pdi, mdi


def bb_width(closes, n=20, mult=2.0):
    out = []
    for i in range(len(closes)):
        if i < n - 1:
            out.append(None)
            continue
        w = closes[i - n + 1 : i + 1]
        m, sd = mean(w), pstdev(w)
        out.append((2 * mult * sd) / m * 100 if m else None)
    return out


def realized_vol(closes, bars, bars_per_year):
    """Biến động thực quy năm (%) của `bars` nến cuối."""
    if len(closes) < bars + 1:
        return None
    rets = [math.log(closes[i] / closes[i - 1]) for i in range(len(closes) - bars, len(closes))]
    return pstdev(rets) * math.sqrt(bars_per_year) * 100


def pct(a, b):
    return (a / b - 1) * 100 if b else 0.0


def volume_profile(k, bin_pct=None, value_area=None):
    """POC, VAH, VAL của các nến k (khối lượng rải đều trên khoảng thấp-cao, bin cố định theo % giá)."""
    bin_pct = bin_pct or C.VP_BIN_PCT
    value_area = value_area or C.VP_VALUE_AREA
    if not k:
        return None
    width = k[-1]["c"] * bin_pct
    hist = {}
    for bar in k:
        lo, hi = int(bar["l"] // width), int(bar["h"] // width)
        v = bar["v"] / (hi - lo + 1)
        for b in range(lo, hi + 1):
            hist[b] = hist.get(b, 0.0) + v
    total = sum(hist.values())
    poc = max(hist, key=hist.get)
    acc, lo, hi = hist[poc], poc, poc
    while acc < total * value_area:
        up, dn = hist.get(hi + 1, 0.0), hist.get(lo - 1, 0.0)
        if up == 0 and dn == 0:
            break
        if up >= dn:
            hi += 1; acc += up
        else:
            lo -= 1; acc += dn
    return {"poc": (poc + 0.5) * width, "vah": (hi + 1) * width, "val": lo * width}


def rsi(closes, n=14):
    """RSI14 kiểu Wilder tại nến cuối."""
    if len(closes) <= n:
        return None
    gains = [max(closes[i] - closes[i - 1], 0.0) for i in range(1, len(closes))]
    losses = [max(closes[i - 1] - closes[i], 0.0) for i in range(1, len(closes))]
    ag, al = mean(gains[:n]), mean(losses[:n])
    for g, l in zip(gains[n:], losses[n:]):
        ag = (ag * (n - 1) + g) / n
        al = (al * (n - 1) + l) / n
    return 100.0 if al == 0 else 100 - 100 / (1 + ag / al)


def vp_state(close, p):
    if p is None:
        return "none"
    return "above" if close > p["vah"] else "below" if close < p["val"] else "inside"


# ---------- bộ chỉ báo cho một đồng ----------
def compute(symbol, d, dvol=None):
    km = d["k_main"][:-1]  # bỏ nến đang chạy để chỉ báo ổn định
    kh = d["k_high"][:-1]
    closes = [x["c"] for x in km]
    last = d["k_main"][-1]["c"]  # giá hiện tại = close của nến đang chạy
    bars_per_year = 6 * 365  # nến 4h

    r = {"symbol": symbol, "name": C.SHORT[symbol], "price": last}

    # Giá
    r["chg_4h"] = pct(last, closes[-1])
    r["chg_24h"] = pct(last, closes[-6]) if len(closes) >= 6 else None
    r["chg_7d"] = pct(last, closes[-42]) if len(closes) >= 42 else None
    atrp = atr_pct(km)
    r["atr_pct"] = atrp[-1]
    atr_hist = [x for x in atrp[-42:] if x is not None]
    r["atr_ratio"] = atrp[-1] / mean(atr_hist) if atr_hist and atrp[-1] else None
    rv24 = realized_vol(closes, 6, bars_per_year)
    rv_hist = [realized_vol(closes[: i + 1], 6, bars_per_year) for i in range(len(closes) - 180, len(closes))]
    rv_hist = [x for x in rv_hist if x is not None]
    r["rv_24h"] = rv24
    r["rv_z"] = (rv24 - mean(rv_hist)) / pstdev(rv_hist) if rv24 and len(rv_hist) > 10 and pstdev(rv_hist) else None
    bbw = bb_width(closes)
    recent = [x for x in bbw[-C.BBW_SQUEEZE_LOOKBACK:] if x is not None]
    r["bbw"] = bbw[-1]
    r["bbw_squeeze"] = bool(recent) and bbw[-1] is not None and bbw[-1] <= min(recent) * 1.05
    vols = [x["v"] for x in km]
    r["vol_ratio"] = vols[-1] / mean(vols[-21:-1]) if len(vols) > 21 and mean(vols[-21:-1]) else None

    # Xu hướng (4h + 1D)
    e20, e50 = ema(closes, 20), ema(closes, 50)
    a, pdi, mdi = adx(km)
    r["ema20"], r["ema50"], r["adx"] = e20[-1], e50[-1], a
    hc = [x["c"] for x in kh]
    he20, he50 = ema(hc, 20), ema(hc, 50)
    r["trend_1d"] = "up" if he20[-1] > he50[-1] and hc[-1] > he20[-1] else "down" if he20[-1] < he50[-1] and hc[-1] < he20[-1] else "flat"
    if a is not None and a >= C.ADX_TREND and e20[-1] > e50[-1] and last > e20[-1] and pdi > mdi:
        r["trend_4h"] = "up"
    elif a is not None and a >= C.ADX_TREND and e20[-1] < e50[-1] and last < e20[-1] and mdi > pdi:
        r["trend_4h"] = "down"
    else:
        r["trend_4h"] = "flat"
    # Xu hướng rõ: 4h và 1D cùng chiều
    r["trend"] = r["trend_4h"] if r["trend_4h"] == r["trend_1d"] and r["trend_4h"] != "flat" else "flat"
    r["trend_strong"] = r["trend"] != "flat" and a is not None and a >= C.ADX_STRONG

    # Phái sinh
    oi = d["oi"]
    r["oi_usd"] = oi[-1]["oi_usd"] if oi else None
    r["oi_chg_4h"] = pct(oi[-1]["oi"], oi[-5]["oi"]) if len(oi) >= 5 else None
    r["oi_chg_24h"] = pct(oi[-1]["oi"], oi[-25]["oi"]) if len(oi) >= 25 else None
    r["funding"] = d["premium"]["funding"]
    r["ls_accounts"] = d["ls_accounts"]
    r["ls_top"] = d["ls_top"]
    r["taker"] = d["taker"]

    # Kỳ vọng
    r["dvol"] = dvol
    r["dvol_gap"] = dvol - rv24 if dvol is not None and rv24 is not None else None

    r["daily"] = daily_signals(symbol, kh)

    # Volume profile: tính trên nến ĐÃ ĐÓNG, trạng thái theo close của nến đóng gần nhất
    p4 = volume_profile(km[-C.VP_WINDOW_4H - 1 : -1]) if len(km) > C.VP_WINDOW_4H else None
    p1 = volume_profile(kh[-C.VP_WINDOW_1D - 1 : -1]) if len(kh) > C.VP_WINDOW_1D else None
    r["vp_4h"] = {"profile": p4, "state": vp_state(km[-1]["c"], p4), "close": km[-1]["c"]}
    r["vp_1d"] = {"profile": p1, "state": vp_state(kh[-1]["c"], p1), "close": kh[-1]["c"]}
    # Xác nhận cho tín hiệu ngày (backtest: VP + RSI + khối lượng 1,5x là tổ hợp tốt nhất trên 1D)
    hc = [x["c"] for x in kh]
    hv = [x["v"] for x in kh]
    r["vp_1d"]["rsi"] = rsi(hc)
    r["vp_1d"]["vol_ratio"] = hv[-1] / mean(hv[-21:-1]) if len(hv) > 21 and mean(hv[-21:-1]) else None
    st = r["vp_1d"]["state"]
    rs, vr = r["vp_1d"]["rsi"], r["vp_1d"]["vol_ratio"]
    r["vp_1d"]["confirmed"] = bool(rs is not None and vr is not None and vr >= 1.5 and ((st == "above" and rs > 55) or (st == "below" and rs < 45)))

    # Ichimoku ngày và Weinstein (SMA30 ngày): hai nguồn thêm cho agent đề xuất (backtest 1D: Ichimoku PF 2,2-3,0; Weinstein áp lên 4h PF 1,6-1,9)
    r["ichimoku_1d"] = ichimoku_state(kh)
    r["weinstein_1d"] = weinstein_state(hc)

    # Inside bar 4h theo hướng EMA20/50 (backtest 3 năm: PF 1,4-1,7 cả 3 đồng). Nến mẹ km[-3], nến trong km[-2], nến bung km[-1].
    r["inside_4h"] = inside_bar(km, e20[-1], e50[-1])

    r["score"] = volatility_score(r)
    r["signals"] = signals(r)
    return r


def ichimoku_state(k):
    """'up' khi giá trên mây và Tenkan > Kijun, 'down' ngược lại, 'flat' khi trong mây hoặc lệch nhau. Mây dịch 26 nến."""
    if len(k) < 52 + 26:
        return "flat"
    h = [x["h"] for x in k]; l = [x["l"] for x in k]
    def mid(n, i):
        return (max(h[i - n + 1 : i + 1]) + min(l[i - n + 1 : i + 1])) / 2
    i = len(k) - 1; j = i - 26
    tenkan, kijun = mid(9, i), mid(26, i)
    sa, sb = (mid(9, j) + mid(26, j)) / 2, mid(52, j)
    c = k[i]["c"]
    if c > max(sa, sb) and tenkan > kijun:
        return "up"
    if c < min(sa, sb) and tenkan < kijun:
        return "down"
    return "flat"


def weinstein_state(closes, n=30):
    """Giai đoạn 2 ('up'): giá trên SMA30 và SMA30 dốc lên; giai đoạn 4 ('down'): dưới và dốc xuống; còn lại 'flat'."""
    if len(closes) < n + 2:
        return "flat"
    s_now = mean(closes[-n:]); s_prev = mean(closes[-n - 1 : -1])
    c = closes[-1]
    if c > s_now and s_now > s_prev:
        return "up"
    if c < s_now and s_now < s_prev:
        return "down"
    return "flat"


def inside_bar(km, e20, e50):
    """{dir: 1/-1, mother_low, mother_high, close, t} khi nến vừa đóng bung khỏi nến mẹ cùng chiều EMA, ngược lại None."""
    if len(km) < 3 or e20 is None or e50 is None:
        return None
    m, ins, b = km[-3], km[-2], km[-1]
    if not (ins["h"] <= m["h"] and ins["l"] >= m["l"]):
        return None
    trend = 1 if e20 > e50 else -1
    if trend == 1 and b["c"] > m["h"]:
        return {"dir": 1, "mother_low": m["l"], "mother_high": m["h"], "close": b["c"], "t": b["t"]}
    if trend == -1 and b["c"] < m["l"]:
        return {"dir": -1, "mother_low": m["l"], "mother_high": m["h"], "close": b["c"], "t": b["t"]}
    return None


def daily_signals(symbol, kh):
    """Khung ngày: cắt EMA20/50 (tín hiệu chính), nén rồi bung, dừng lỗ gợi ý theo ATR."""
    c = [x["c"] for x in kh]
    if len(c) < 60:
        return {"regime": "flat", "crossed": False, "stop": None, "squeeze_break": 0}
    e20, e50 = ema(c, 20), ema(c, 50)
    regime = "up" if e20[-1] > e50[-1] else "down"
    prev = "up" if e20[-2] > e50[-2] else "down"
    atr = wilder(true_ranges(kh), 14)[-1]
    stop = c[-1] - atr * C.DAILY_ATR_STOP if regime == "up" else c[-1] + atr * C.DAILY_ATR_STOP
    # nén rồi bung
    sq = 0
    if symbol in C.DAILY_SQUEEZE_SYMBOLS and len(c) > C.DAILY_SQUEEZE_LOOKBACK + 25:
        n, m = 20, 2.0
        bbw, up, lo = [], [], []
        for i in range(len(c)):
            if i < n - 1:
                bbw.append(None); up.append(None); lo.append(None); continue
            w = c[i - n + 1 : i + 1]
            mu, sd = mean(w), pstdev(w)
            bbw.append(2 * m * sd / mu * 100); up.append(mu + m * sd); lo.append(mu - m * sd)
        recent = [x for x in bbw[-C.DAILY_SQUEEZE_LOOKBACK - 1 : -1] if x is not None]
        squeezed = any(bbw[j] is not None and bbw[j] <= min(recent) * 1.05 for j in range(len(c) - 6, len(c) - 1))
        if squeezed and c[-1] > up[-1]:
            sq = 1
        elif squeezed and c[-1] < lo[-1]:
            sq = -1
    return {
        "regime": regime,
        "crossed": regime != prev,
        "ema20": e20[-1],
        "ema50": e50[-1],
        "atr": atr,
        "stop": stop,
        "close": c[-1],
        "squeeze_break": sq,
        "bars_in_regime": next((k for k in range(1, len(c)) if (e20[-1 - k] > e50[-1 - k]) != (regime == "up")), len(c)),
    }


def _clip(x, lo, hi):
    return max(lo, min(hi, x))


def volatility_score(r):
    """Điểm 0-100: gộp z-score các nhóm. 50 = bình thường."""
    price_parts = []
    if r.get("rv_z") is not None:
        price_parts.append(_clip(r["rv_z"], -3, 3) / 3)
    if r.get("atr_ratio") is not None:
        price_parts.append(_clip((r["atr_ratio"] - 1) / 1.0, -1, 1))
    if r.get("vol_ratio") is not None:
        price_parts.append(_clip((r["vol_ratio"] - 1) / 2.0, -1, 1))
    deriv_parts = []
    if r.get("oi_chg_4h") is not None:
        deriv_parts.append(_clip(abs(r["oi_chg_4h"]) / C.OI_CHANGE_4H, 0, 1))
    if r.get("funding") is not None:
        deriv_parts.append(_clip(abs(r["funding"]) / C.FUNDING_HOT, 0, 1))
    if r.get("ls_accounts") is not None:
        deriv_parts.append(_clip(abs(math.log(r["ls_accounts"])) / math.log(C.LS_RATIO_HIGH), 0, 1))
    expect_parts = []
    if r.get("dvol_gap") is not None:
        expect_parts.append(_clip(r["dvol_gap"] / C.DVOL_RV_GAP, -1, 1))

    def avg(xs):
        return mean(xs) if xs else 0.0

    w = C.SCORE_WEIGHTS
    total_w = (w["price"] if price_parts else 0) + (w["deriv"] if deriv_parts else 0) + (w["expect"] if expect_parts else 0)
    if not total_w:
        return 50
    s = (avg(price_parts) * w["price"] + avg(deriv_parts) * w["deriv"] + avg(expect_parts) * w["expect"]) / total_w
    return int(round(50 + 50 * _clip(s, -1, 1)))


def signals(r):
    """Danh sách tín hiệu kết hợp, mỗi phần tử (mã, mức, mô tả)."""
    s = []
    sym = r["symbol"]
    if abs(r["chg_4h"]) >= C.PRICE_MOVE_4H[sym]:
        s.append(("price_move", "high", f"Giá {'tăng' if r['chg_4h'] > 0 else 'giảm'} {abs(r['chg_4h']):.1f}% trong 4h"))
    if r.get("atr_ratio") and r["atr_ratio"] >= C.ATR_SPIKE_RATIO:
        s.append(("atr_spike", "high", f"ATR gấp {r['atr_ratio']:.1f} lần trung bình 7 ngày"))
    if r.get("rv_z") is not None and r["rv_z"] >= C.RV_ZSCORE:
        s.append(("rv_spike", "medium", f"Biến động thực 24h cao bất thường (z={r['rv_z']:.1f})"))
    if r.get("bbw_squeeze"):
        s.append(("squeeze", "medium", "Nén biến động: Bollinger hẹp nhất 30 ngày, thường báo trước cú bung"))
    if r.get("vol_ratio") and r["vol_ratio"] >= C.VOLUME_RATIO:
        s.append(("volume", "medium", f"Khối lượng gấp {r['vol_ratio']:.1f} lần trung bình 20 nến"))
    oi4 = r.get("oi_chg_4h") or 0
    f = r.get("funding") or 0
    ls = r.get("ls_accounts") or 1
    if r["chg_4h"] > 0 and oi4 >= C.OI_CHANGE_4H and (f >= C.FUNDING_HOT or ls >= C.LS_RATIO_HIGH):
        s.append(("long_hot", "high", f"Long quá nóng: OI +{oi4:.1f}%/4h, funding {f*100:.3f}%, L/S {ls:.2f}. Nguy cơ long squeeze"))
    if r["chg_4h"] <= 0 and oi4 >= C.OI_CHANGE_4H and (f <= C.FUNDING_COLD or ls <= C.LS_RATIO_LOW):
        s.append(("short_crowded", "high", f"Short quá đông: OI +{oi4:.1f}%/4h, funding {f*100:.3f}%, L/S {ls:.2f}. Nguy cơ short squeeze"))
    if r.get("oi_chg_24h") is not None and abs(r["oi_chg_24h"]) >= C.OI_CHANGE_24H:
        s.append(("oi_24h", "medium", f"OI {'tăng' if r['oi_chg_24h'] > 0 else 'giảm'} {abs(r['oi_chg_24h']):.1f}% trong 24h"))
    if r.get("chg_24h") and r.get("oi_chg_24h") is not None and r["chg_24h"] > 2 and r["oi_chg_24h"] < -3:
        s.append(("divergence", "medium", "Phân kỳ: giá tăng nhưng OI giảm, lực đẩy yếu dần"))
    if r.get("taker") and (r["taker"] >= C.TAKER_HIGH or r["taker"] <= C.TAKER_LOW):
        s.append(("taker", "low", f"Taker buy/sell {r['taker']:.2f}: lực {'mua' if r['taker'] > 1 else 'bán'} chủ động áp đảo"))
    if r.get("dvol_gap") is not None and abs(r["dvol_gap"]) >= C.DVOL_RV_GAP:
        s.append(("dvol_gap", "low", f"DVOL {r['dvol']:.0f} so với biến động thực {r['rv_24h']:.0f}: thị trường quyền chọn {'kỳ vọng biến động lớn hơn' if r['dvol_gap'] > 0 else 'đang bình thản hơn'} thực tế"))
    if r["trend"] != "flat":
        s.append(("trend", "high" if r["trend_strong"] else "medium", f"Pha 4h đang có xu hướng {'tăng' if r['trend'] == 'up' else 'giảm'} (ADX {r['adx']:.0f}), chỉ để tham khảo"))
    return s
