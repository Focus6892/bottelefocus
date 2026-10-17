"""Backtest các cách dự đoán xu hướng trên nến 4h (xác nhận 1D).

Mỗi chiến lược tạo tín hiệu +1 (lên), -1 (xuống) hoặc 0 tại mỗi nến đã đóng.
Hai cách đo độ tin cậy:
  1. Độ đúng hướng: sau tín hiệu, giá sau 1 ngày / 3 ngày / 7 ngày có đi đúng hướng không,
     so với xác suất nền (giá tăng ngẫu nhiên bao nhiêu % thời gian).
  2. Giao dịch theo tín hiệu: vào khi tín hiệu xuất hiện, thoát khi tín hiệu ngược hoặc
     dừng lỗ 2 ATR, phí 0,05% mỗi chiều. Đo lợi nhuận, tỷ lệ thắng, profit factor, sụt giảm tối đa.
Kết quả ghi ra backtest/results.md và results.json.
"""
import json
import math
import os
from statistics import mean, pstdev

try:
    from backtest import smc, stock
except ImportError:  # chạy trực tiếp: python backtest/run.py
    import smc, stock

DATA = os.path.join(os.path.dirname(__file__), "data")
SYMS = ["BTC", "ETH", "SOL"]
FEE = 0.0005

# Cấu hình theo khung: 4h (xác nhận 1D) hoặc 1d (xác nhận 1W)
TF = {
    "4h": dict(main="4H", high="1Dutc", main_ms=4 * 3600_000, high_ms=86_400_000,
               horizons={"1d": 6, "3d": 18, "7d": 42}, atr_stop=2.0, squeeze_lookback=180, squeeze_hold=42,
               recent_months=12, label="4h", out="results", vp_window=180, smc_n=5),
    "1d": dict(main="1Dutc", high="1Wutc", main_ms=86_400_000, high_ms=7 * 86_400_000,
               horizons={"1 tuần": 7, "2 tuần": 14, "4 tuần": 28}, atr_stop=3.5, squeeze_lookback=120, squeeze_hold=28,
               recent_months=24, label="1D", out="results_1d", vp_window=90, smc_n=3),
    # Ngắn hạn: 1h (xác nhận 4h), dừng lỗ 1,5 ATR, nén tính trong 7 ngày, giữ tối đa 1 ngày
    "1h": dict(main="1H", high="4H", main_ms=3600_000, high_ms=4 * 3600_000,
               horizons={"4 giờ": 4, "1 ngày": 24, "3 ngày": 72}, atr_stop=1.5, squeeze_lookback=168, squeeze_hold=24,
               recent_months=6, label="1h", out="results_1h", vp_window=168, smc_n=5),
    # Scalp: xác nhận bằng 4h, dừng lỗ 1,5 ATR, nén tính trong 2 ngày, giữ tối đa 1 ngày
    "15m": dict(main="15m", high="4H", main_ms=15 * 60_000, high_ms=4 * 3600_000,
                horizons={"1 giờ": 4, "4 giờ": 16, "1 ngày": 96}, atr_stop=1.5, squeeze_lookback=192, squeeze_hold=96,
                recent_months=3, label="15m", out="results_15m", vp_window=192, smc_n=5),
    "30m": dict(main="30m", high="4H", main_ms=30 * 60_000, high_ms=4 * 3600_000,
                horizons={"1 giờ": 2, "4 giờ": 8, "1 ngày": 48}, atr_stop=1.5, squeeze_lookback=96, squeeze_hold=48,
                recent_months=3, label="30m", out="results_30m", vp_window=96, smc_n=5),
}
CFG = TF["4h"]
HORIZONS = CFG["horizons"]


# ---------- chỉ báo dạng chuỗi ----------
def ema(v, n):
    k, out, e = 2 / (n + 1), [], None
    for x in v:
        e = x if e is None else x * k + e * (1 - k)
        out.append(e)
    return out


def wilder(v, n):
    out, s = [], None
    for i, x in enumerate(v):
        if i < n - 1:
            out.append(None)
            continue
        s = mean(v[:n]) if s is None else (s * (n - 1) + x) / n
        out.append(s)
    return out


def tr(k):
    out = [k[0]["h"] - k[0]["l"]]
    for i in range(1, len(k)):
        out.append(max(k[i]["h"] - k[i]["l"], abs(k[i]["h"] - k[i - 1]["c"]), abs(k[i]["l"] - k[i - 1]["c"])))
    return out


def adx_series(k, n=14):
    t = tr(k)
    plus, minus = [0.0], [0.0]
    for i in range(1, len(k)):
        up, dn = k[i]["h"] - k[i - 1]["h"], k[i - 1]["l"] - k[i]["l"]
        plus.append(up if up > dn and up > 0 else 0.0)
        minus.append(dn if dn > up and dn > 0 else 0.0)
    ts, ps, ms = wilder(t, n), wilder(plus, n), wilder(minus, n)
    pdi, mdi, dx = [], [], []
    for a, b, c in zip(ts, ps, ms):
        if a is None or a == 0:
            pdi.append(None); mdi.append(None); dx.append(None)
            continue
        p, m = 100 * b / a, 100 * c / a
        pdi.append(p); mdi.append(m)
        dx.append(100 * abs(p - m) / (p + m) if p + m else 0.0)
    first = next((i for i, x in enumerate(dx) if x is not None), len(dx))
    # giữ đúng vị trí: ATR = 0 giữa chuỗi coi như DX = 0, không được dồn trái (sẽ nhìn trước)
    sm = wilder([0.0 if x is None else x for x in dx[first:]], n)
    adx = [None] * first + sm
    return adx, pdi, mdi


def atr_series(k, n=14):
    return wilder(tr(k), n)


def bb(closes, n=20, m=2.0):
    up, lo, w = [], [], []
    for i in range(len(closes)):
        if i < n - 1:
            up.append(None); lo.append(None); w.append(None)
            continue
        s = closes[i - n + 1 : i + 1]
        mu, sd = mean(s), pstdev(s)
        up.append(mu + m * sd); lo.append(mu - m * sd); w.append(2 * m * sd / mu * 100)
    return up, lo, w


def day_index(k4, k1):
    """Với mỗi nến khung chính, chỉ số nến khung cao gần nhất ĐÃ ĐÓNG trước nó."""
    out, j = [], -1
    for bar in k4:
        while j + 1 < len(k1) and k1[j + 1]["t"] + CFG["high_ms"] <= bar["t"]:  # đã đóng trước khi nến chính mở
            j += 1
        out.append(j)
    return out


# ---------- chiến lược ----------
def strat_trend(k4, k1, adx_min=25):
    """Chiến lược đang dùng trong bot: EMA20/50 + ADX + xác nhận 1D."""
    c = [x["c"] for x in k4]
    e20, e50 = ema(c, 20), ema(c, 50)
    adx, pdi, mdi = adx_series(k4)
    c1 = [x["c"] for x in k1]
    d20, d50 = ema(c1, 20), ema(c1, 50)
    di = day_index(k4, k1)
    sig = []
    for i in range(len(k4)):
        j = di[i]
        if j < 50 or adx[i] is None:
            sig.append(0); continue
        up1 = d20[j] > d50[j] and c1[j] > d20[j]
        dn1 = d20[j] < d50[j] and c1[j] < d20[j]
        if adx[i] >= adx_min and e20[i] > e50[i] and c[i] > e20[i] and pdi[i] > mdi[i] and up1:
            sig.append(1)
        elif adx[i] >= adx_min and e20[i] < e50[i] and c[i] < e20[i] and mdi[i] > pdi[i] and dn1:
            sig.append(-1)
        else:
            sig.append(0)
    return sig


def strat_ema_cross(k4, k1):
    c = [x["c"] for x in k4]
    e20, e50 = ema(c, 20), ema(c, 50)
    return [0 if i < 50 else (1 if e20[i] > e50[i] else -1) for i in range(len(c))]


def strat_donchian(k4, k1, n=20, exit_n=10):
    """Phá đỉnh/đáy 20 nến 4h; trạng thái giữ tới khi phá ngược 10 nến."""
    sig, state = [], 0
    for i in range(len(k4)):
        if i < n:
            sig.append(0); continue
        hi = max(x["h"] for x in k4[i - n : i]); lo = min(x["l"] for x in k4[i - n : i])
        hx = max(x["h"] for x in k4[i - exit_n : i]); lx = min(x["l"] for x in k4[i - exit_n : i])
        c = k4[i]["c"]
        if c > hi:
            state = 1
        elif c < lo:
            state = -1
        elif state == 1 and c < lx:
            state = 0
        elif state == -1 and c > hx:
            state = 0
        sig.append(state)
    return sig


def strat_squeeze(k4, k1, lookback=None, hold=None):
    lookback = lookback or CFG["squeeze_lookback"]; hold = hold or CFG["squeeze_hold"]
    """Nén (BBW thấp nhất 30 ngày trong 5 nến gần) rồi đóng ngoài dải: theo hướng bung, giữ 7 ngày."""
    c = [x["c"] for x in k4]
    up, lo, w = bb(c)
    sig, state, left = [], 0, 0
    for i in range(len(c)):
        if i < lookback or w[i] is None:
            sig.append(0); continue
        recent = [x for x in w[i - lookback : i] if x is not None]
        squeezed = any(w[j] is not None and w[j] <= min(recent) * 1.05 for j in range(i - 5, i))
        if left > 0:
            left -= 1
        else:
            state = 0
        if state == 0 and squeezed:
            if c[i] > up[i]:
                state, left = 1, hold
            elif c[i] < lo[i]:
                state, left = -1, hold
        sig.append(state)
    return sig


def strat_combo(k4, k1):
    """Xu hướng (ADX 20) + phá đỉnh/đáy Donchian cùng chiều: vào chặt hơn."""
    a, b = strat_trend(k4, k1, adx_min=20), strat_donchian(k4, k1)
    return [x if x == y else 0 for x, y in zip(a, b)]


# ---------- volume profile ----------
def volume_profile(k, window, bin_pct=0.002, value_area=0.70):
    """Với mỗi nến i: POC, VAH, VAL của `window` nến TRƯỚC nó (không gồm nến i).
    Khối lượng mỗi nến rải đều trên khoảng low-high theo bin cố định (0,2% giá tham chiếu).
    Cập nhật dần (thêm nến mới, bỏ nến cũ) nên chạy được trên 35.000 nến."""
    ref = sorted(x["c"] for x in k)[len(k) // 2]
    width = ref * bin_pct
    hist = {}

    def spread(bar, sign):
        lo, hi = int(bar["l"] // width), int(bar["h"] // width)
        n = hi - lo + 1
        v = bar["v"] / n * sign
        for b in range(lo, hi + 1):
            hist[b] = hist.get(b, 0.0) + v
            if hist[b] <= 1e-9:
                hist.pop(b, None)

    out = []
    for i in range(len(k)):
        if i >= window:
            spread(k[i - window - 1], -1) if i - window - 1 >= 0 else None
        if i == 0:
            out.append(None); continue
        spread(k[i - 1], +1)
        if i < window or not hist:
            out.append(None); continue
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
        out.append({"poc": (poc + 0.5) * width, "vah": (hi + 1) * width, "val": lo * width})
    return out


def strat_vp_breakout(k4, k1):
    """Thoát vùng giá trị: đóng trên VAH (từ bên trong) -> lên; đóng dưới VAL -> xuống. Thoát khi quay vào trong VA."""
    vp = volume_profile(k4, CFG["vp_window"])
    sig, state = [], 0
    for i, bar in enumerate(k4):
        p = vp[i]
        if p is None:
            sig.append(0); continue
        c = bar["c"]
        if c > p["vah"]:
            state = 1
        elif c < p["val"]:
            state = -1
        elif state == 1 and c < p["poc"]:
            state = 0
        elif state == -1 and c > p["poc"]:
            state = 0
        sig.append(state)
    return sig


def strat_vp_revert(k4, k1):
    """Hồi về POC: giá rớt dưới VAL rồi đóng lại trên VAL -> lên (mục tiêu POC); ngược lại cho xuống.
    Thoát khi chạm POC hoặc rơi lại ngoài VA."""
    vp = volume_profile(k4, CFG["vp_window"])
    sig, state, outside = [], 0, 0
    for i, bar in enumerate(k4):
        p = vp[i]
        if p is None:
            sig.append(0); continue
        c = bar["c"]
        if state == 1 and (c >= p["poc"] or c < p["val"]):
            state = 0
        elif state == -1 and (c <= p["poc"] or c > p["vah"]):
            state = 0
        if state == 0:
            if outside == -1 and c > p["val"]:
                state = 1
            elif outside == 1 and c < p["vah"]:
                state = -1
        outside = -1 if c < p["val"] else 1 if c > p["vah"] else 0
        sig.append(state)
    return sig


def strat_vp_ema(k4, k1):
    """Cắt EMA20/50 nhưng chỉ nhận long khi giá trên POC, short khi giá dưới POC."""
    vp = volume_profile(k4, CFG["vp_window"])
    base = strat_ema_cross(k4, k1)
    out = []
    for i, bar in enumerate(k4):
        p = vp[i]
        if p is None or base[i] == 0:
            out.append(0); continue
        if base[i] == 1 and bar["c"] > p["poc"]:
            out.append(1)
        elif base[i] == -1 and bar["c"] < p["poc"]:
            out.append(-1)
        else:
            out.append(0)
    return out


# ---------- RSI và các tổ hợp ----------
def rsi_series(closes, n=14):
    out = [None] * len(closes)
    gains, losses = [0.0], [0.0]
    for i in range(1, len(closes)):
        d = closes[i] - closes[i - 1]
        gains.append(max(d, 0.0)); losses.append(max(-d, 0.0))
    ag, al = None, None
    for i in range(n, len(closes)):
        if ag is None:
            ag, al = mean(gains[1 : n + 1]), mean(losses[1 : n + 1])
        else:
            ag = (ag * (n - 1) + gains[i]) / n
            al = (al * (n - 1) + losses[i]) / n
        out[i] = 100.0 if al == 0 else 100 - 100 / (1 + ag / al)
    return out


def strat_rsi50(k4, k1):
    """Chuẩn so sánh: RSI14 trên 50 -> lên, dưới 50 -> xuống."""
    r = rsi_series([x["c"] for x in k4])
    return [0 if v is None else (1 if v > 50 else -1) for v in r]


def _vp_break_core(k4, enter_ok, exit_extra=None):
    """Khung chung: thoát vùng giá trị, vào khi enter_ok(i, hướng) đúng, thoát khi quay qua POC hoặc exit_extra."""
    vp = volume_profile(k4, CFG["vp_window"])
    sig, state = [], 0
    for i, bar in enumerate(k4):
        p = vp[i]
        if p is None:
            sig.append(0); continue
        c = bar["c"]
        if state == 1 and (c < p["poc"] or (exit_extra and exit_extra(i, 1))):
            state = 0
        elif state == -1 and (c > p["poc"] or (exit_extra and exit_extra(i, -1))):
            state = 0
        if state == 0:
            if c > p["vah"] and enter_ok(i, 1):
                state = 1
            elif c < p["val"] and enter_ok(i, -1):
                state = -1
        sig.append(state)
    return sig


def strat_vp_rsi(k4, k1):
    """Thoát vùng giá trị + RSI14 xác nhận (lên: RSI > 55, xuống: RSI < 45). Thoát thêm khi RSI về qua 50."""
    r = rsi_series([x["c"] for x in k4])
    ok = lambda i, d: r[i] is not None and (r[i] > 55 if d == 1 else r[i] < 45)
    ex = lambda i, d: r[i] is not None and (r[i] < 50 if d == 1 else r[i] > 50)
    return _vp_break_core(k4, ok, ex)


def strat_vp_rsi_vol(k4, k1):
    """Thoát vùng giá trị + RSI xác nhận + khối lượng nến bung >= 1,5 lần trung bình 20 nến."""
    r = rsi_series([x["c"] for x in k4])
    v = [x["v"] for x in k4]
    def ok(i, d):
        if i < 21 or r[i] is None:
            return False
        avg = mean(v[i - 20 : i])
        return v[i] >= 1.5 * avg and (r[i] > 55 if d == 1 else r[i] < 45)
    return _vp_break_core(k4, ok)


def strat_vp_rsi_adx(k4, k1):
    """Thoát vùng giá trị + RSI xác nhận + ADX14 >= 20 (có lực)."""
    r = rsi_series([x["c"] for x in k4])
    a, pdi, mdi = adx_series(k4)
    ok = lambda i, d: r[i] is not None and a[i] is not None and a[i] >= 20 and (r[i] > 55 if d == 1 else r[i] < 45)
    return _vp_break_core(k4, ok)


def strat_vp_rsi_revert(k4, k1):
    """Hồi trong vùng cân bằng: giá trong VA, gần VAL (dưới 1/3 vùng) và RSI < 30 -> lên tới POC;
    gần VAH và RSI > 70 -> xuống tới POC. Thoát tại POC hoặc khi rơi ra ngoài VA."""
    vp = volume_profile(k4, CFG["vp_window"])
    r = rsi_series([x["c"] for x in k4])
    sig, state = [], 0
    for i, bar in enumerate(k4):
        p = vp[i]
        if p is None or r[i] is None:
            sig.append(0); continue
        c = bar["c"]
        if state == 1 and (c >= p["poc"] or c < p["val"]):
            state = 0
        elif state == -1 and (c <= p["poc"] or c > p["vah"]):
            state = 0
        if state == 0 and p["val"] <= c <= p["vah"]:
            third = (p["vah"] - p["val"]) / 3
            if c <= p["val"] + third and r[i] < 30:
                state = 1
            elif c >= p["vah"] - third and r[i] > 70:
                state = -1
        sig.append(state)
    return sig


def strat_confluence(k4, k1):
    """Đồng thuận 3 yếu tố: giá trên POC + EMA20 > EMA50 + RSI > 50 -> lên (ngược lại -> xuống). Mất 2/3 thì thoát."""
    vp = volume_profile(k4, CFG["vp_window"])
    c = [x["c"] for x in k4]
    e20, e50 = ema(c, 20), ema(c, 50)
    r = rsi_series(c)
    sig, state = [], 0
    for i in range(len(c)):
        p = vp[i]
        if p is None or r[i] is None or i < 50:
            sig.append(0); continue
        up = [c[i] > p["poc"], e20[i] > e50[i], r[i] > 50]
        n_up = sum(up)
        if state == 0:
            state = 1 if n_up == 3 else -1 if n_up == 0 else 0
        elif state == 1 and n_up <= 1:
            state = 0
        elif state == -1 and n_up >= 2:
            state = 0
        sig.append(state)
    return sig


def _vp_rsi_vol_ok(k4):
    r = rsi_series([x["c"] for x in k4])
    v = [x["v"] for x in k4]
    def ok(i, d):
        if i < 21 or r[i] is None:
            return False
        return v[i] >= 1.5 * mean(v[i - 20 : i]) and (r[i] > 55 if d == 1 else r[i] < 45)
    return ok


def strat_vp_rsi_vol_ema(k4, k1):
    """Phương án 1 lọc bởi 2: VP + RSI + khối lượng, chỉ vào cùng hướng EMA20/50; thoát khi quay qua POC."""
    c = [x["c"] for x in k4]
    e20, e50 = ema(c, 20), ema(c, 50)
    base = _vp_rsi_vol_ok(k4)
    ok = lambda i, d: i >= 50 and base(i, d) and ((e20[i] > e50[i]) if d == 1 else (e20[i] < e50[i]))
    return _vp_break_core(k4, ok)


def strat_vp_rsi_vol_ema_x(k4, k1):
    """Như trên nhưng thoát thêm khi EMA20/50 đổi chiều ngược với lệnh."""
    c = [x["c"] for x in k4]
    e20, e50 = ema(c, 20), ema(c, 50)
    base = _vp_rsi_vol_ok(k4)
    ok = lambda i, d: i >= 50 and base(i, d) and ((e20[i] > e50[i]) if d == 1 else (e20[i] < e50[i]))
    ex = lambda i, d: (e20[i] < e50[i]) if d == 1 else (e20[i] > e50[i])
    return _vp_break_core(k4, ok, ex)


STRATS = {
    "trend": ("Xu hướng EMA20/50 + ADX25 + xác nhận khung cao (đang dùng)", strat_trend),
    "ema_cross": ("Cắt EMA20/50", strat_ema_cross),
    "donchian": ("Phá đỉnh/đáy 20 nến", strat_donchian),
    "squeeze": ("Nén Bollinger rồi bung", strat_squeeze),
    "combo": ("Xu hướng + phá đỉnh/đáy cùng chiều", strat_combo),
    "vp_breakout": ("Volume profile: thoát vùng giá trị", strat_vp_breakout),
    "vp_revert": ("Volume profile: hồi về POC", strat_vp_revert),
    "vp_ema": ("Volume profile: cắt EMA lọc theo POC", strat_vp_ema),
    "rsi50": ("RSI14 qua 50 (chuẩn so sánh)", strat_rsi50),
    "vp_rsi": ("VP thoát vùng + RSI xác nhận", strat_vp_rsi),
    "vp_rsi_vol": ("VP thoát vùng + RSI + khối lượng 1,5x", strat_vp_rsi_vol),
    "vp_rsi_adx": ("VP thoát vùng + RSI + ADX20", strat_vp_rsi_adx),
    "vp_rsi_revert": ("VP hồi trong vùng + RSI 30/70", strat_vp_rsi_revert),
    "confluence": ("Đồng thuận POC + EMA + RSI", strat_confluence),
    "vp_rsi_vol_ema": ("VP + RSI + KL, chỉ vào cùng hướng EMA", strat_vp_rsi_vol_ema),
    "vp_rsi_vol_ema_x": ("VP + RSI + KL, cùng hướng EMA, thoát khi EMA đổi", strat_vp_rsi_vol_ema_x),
}
# SMC và price action (backtest/smc.py); số nến xác nhận swing lấy theo khung
for _key, (_label, _fn) in smc.STRATS.items():
    STRATS[_key] = (_label, (lambda f: lambda k4, k1: f(k4, CFG["smc_n"]))(_fn))
# Phương pháp từ chứng khoán (backtest/stock.py)
for _key, (_label, _fn) in stock.STRATS.items():
    STRATS[_key] = (_label, (lambda f: lambda k4, k1: f(k4, k1, CFG))(_fn))


# ---------- đánh giá ----------
def entries(sig):
    """Các nến tín hiệu MỚI xuất hiện (đổi từ 0/ngược sang +1 hoặc -1)."""
    out = []
    for i in range(1, len(sig)):
        if sig[i] != 0 and sig[i] != sig[i - 1]:
            out.append((i, sig[i]))
    return out


def directional(k4, sig):
    c = [x["c"] for x in k4]
    res = {}
    for name, h in HORIZONS.items():
        base = [c[i + h] > c[i] for i in range(len(c) - h)]
        base_up = mean(base) if base else 0.5
        hits, rets = [], []
        for i, s in entries(sig):
            if i + h < len(c):
                r = (c[i + h] / c[i] - 1) * s
                rets.append(r); hits.append(r > 0)
        res[name] = {
            "n": len(hits),
            "hit": mean(hits) if hits else None,
            "base": max(base_up, 1 - base_up),
            "avg_ret": mean(rets) * 100 if rets else None,
        }
    return res


def trade_sim(k4, sig, atr_stop=None, start=0):
    """Mô phỏng: vào ở close nến có tín hiệu mới, thoát ở close khi tín hiệu đổi hoặc tại giá dừng lỗ (ATR) trong nến.
    Sau khi dính dừng lỗ, không vào lại cho tới khi tín hiệu đổi giá trị (chờ tín hiệu mới).
    Nếu nến mở qua dừng lỗ (gap) thì khớp ở giá mở. Sụt giảm tính theo vốn đánh giá lại mỗi nến (kể cả lệnh đang mở).
    `start`: chỉ tính các lệnh vào từ nến này (chỉ báo và dừng lỗ vẫn tính trên toàn chuỗi)."""
    atr_stop = atr_stop or CFG["atr_stop"]
    c = [x["c"] for x in k4]
    atr = atr_series(k4)
    pos, entry, stop, entry_i, blocked = 0, 0.0, 0.0, None, None
    trades = []  # (nến vào, nến ra, lợi nhuận)
    eq, peak, mdd = 1.0, 1.0, 0.0
    for i in range(1, len(c)):
        if pos != 0:
            hit_stop = (pos == 1 and k4[i]["l"] <= stop) or (pos == -1 and k4[i]["h"] >= stop)
            flip = sig[i] != pos
            if hit_stop or flip:
                if hit_stop:
                    px = min(stop, k4[i]["o"]) if pos == 1 else max(stop, k4[i]["o"])
                    blocked = sig[i]
                else:
                    px = c[i]
                r = (px / entry - 1) * pos - 2 * FEE
                if entry_i >= start:
                    trades.append((entry_i, i, r))
                    eq *= 1 + r
                pos = 0
        if blocked is not None and sig[i] != blocked:
            blocked = None
        if pos == 0 and sig[i] != 0 and atr[i] and blocked is None:
            pos, entry, entry_i = sig[i], c[i], i
            stop = entry - pos * atr_stop * atr[i]
        if i >= start:
            cur = eq * (1 + (c[i] / entry - 1) * pos) if pos != 0 and entry_i >= start else eq
            peak = max(peak, cur)
            mdd = max(mdd, 1 - cur / peak)
    if pos != 0 and entry_i >= start:  # đóng lệnh còn mở ở nến cuối
        r = (c[-1] / entry - 1) * pos - 2 * FEE
        trades.append((entry_i, len(c) - 1, r))
        eq *= 1 + r
    rets = [t[2] for t in trades]
    if not rets:
        return {"n": 0}
    wins = [t for t in rets if t > 0]; losses = [-t for t in rets if t <= 0]
    bh = c[-1] / c[start] - 1
    return {
        "n": len(rets),
        "win_rate": len(wins) / len(rets),
        "avg_trade": mean(rets) * 100,
        "profit_factor": (sum(wins) / sum(losses)) if losses and sum(losses) > 0 else float("inf"),
        "total_return": (eq - 1) * 100,
        "max_drawdown": mdd * 100,
        "buy_hold": bh * 100,
        "expectancy_ratio": (mean(wins) if wins else 0) / (mean(losses) if losses else 1e-9),
    }


def split(k4, k1, months=None):
    cut = k4[-1]["t"] - (months or CFG["recent_months"]) * 30 * 86_400_000
    i4 = next(i for i, x in enumerate(k4) if x["t"] >= cut)
    return i4


def run(tf="4h"):
    global CFG, HORIZONS
    CFG = TF[tf]; HORIZONS = CFG["horizons"]
    out = {"tf": tf}
    for sym in SYMS:
        k4 = json.load(open(os.path.join(DATA, f"{sym}_{CFG['main']}.json")))
        k1 = json.load(open(os.path.join(DATA, f"{sym}_{CFG['high']}.json")))
        out[sym] = {"bars": len(k4), "from": k4[0]["t"], "to": k4[-1]["t"]}
        i_recent = split(k4, k1)
        for key, (label, fn) in STRATS.items():
            sig = fn(k4, k1)
            res = {"label": label, "direction": directional(k4, sig), "trades": trade_sim(k4, sig)}
            # 12 tháng gần nhất (tín hiệu tính trên toàn bộ, chỉ đo giao dịch trong đoạn gần)
            res["recent"] = trade_sim(k4, sig, start=i_recent)
            out[sym][key] = res
    with open(os.path.join(os.path.dirname(__file__), CFG["out"] + ".json"), "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    write_md(out)
    return out


def f(x, d=1, suf=""):
    if x is None:
        return "-"
    if isinstance(x, float) and math.isinf(x):
        return "∞"
    return f"{x:.{d}f}{suf}"


def write_md(out):
    hz = list(HORIZONS)
    L = [f"# Kết quả backtest dự đoán xu hướng · khung {CFG['label']}", ""]
    import datetime as dt
    for sym in SYMS:
        d = out[sym]
        a, b = (dt.datetime.fromtimestamp(d[k] / 1000, dt.timezone.utc).strftime("%Y-%m-%d") for k in ("from", "to"))
        L += [f"## {sym} · {d['bars']} nến {CFG['label']} · {a} đến {b}", ""]
        L += [f"| Chiến lược | Số tín hiệu | Đúng hướng {hz[0]} | {hz[1]} | {hz[2]} | Nền {hz[2]} | LN TB {hz[2]} |", "|---|---|---|---|---|---|---|"]
        for key, (label, _) in STRATS.items():
            r = d[key]["direction"]
            h = lambda z: f(r[z]['hit']*100 if r[z]['hit'] is not None else None, 0, '%')
            L.append(f"| {label} | {r[hz[2]]['n']} | {h(hz[0])} | {h(hz[1])} | {h(hz[2])} | {f(r[hz[2]]['base']*100,0,'%')} | {f(r[hz[2]]['avg_ret'],2,'%')} |")
        L += ["", f"| Chiến lược | Số lệnh | Thắng | LN/lệnh | Profit factor | Tổng LN cả kỳ | Sụt giảm tối đa | Mua và giữ | Tổng LN {CFG['recent_months']} tháng |", "|---|---|---|---|---|---|---|---|---|"]
        for key, (label, _) in STRATS.items():
            t, rc = d[key]["trades"], d[key]["recent"]
            if t["n"] == 0:
                L.append(f"| {label} | 0 | | | | | | | |"); continue
            L.append(f"| {label} | {t['n']} | {f(t['win_rate']*100,0,'%')} | {f(t['avg_trade'],2,'%')} | {f(t['profit_factor'],2)} | {f(t['total_return'],0,'%')} | {f(t['max_drawdown'],0,'%')} | {f(t['buy_hold'],0,'%')} | {f(rc.get('total_return'),0,'%')} |")
        L.append("")
    with open(os.path.join(os.path.dirname(__file__), CFG["out"] + ".md"), "w") as fh:
        fh.write("\n".join(L))


if __name__ == "__main__":
    import sys
    run(sys.argv[1] if len(sys.argv) > 1 else "4h")
