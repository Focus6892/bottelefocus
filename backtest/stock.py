"""Phương pháp hệ thống từ thị trường chứng khoán, chuyển sang crypto để backtest.

Mỗi hàm nhận (k, kh, cfg): k = nến khung chính, kh = nến khung cao (đã đóng), cfg = cấu hình khung (main_ms, high_ms...).
Trả về trạng thái -1/0/1 theo từng nến (1 = giữ long, -1 = giữ short, 0 = ngoài). Không nhìn trước:
mọi chỉ báo tại nến i chỉ dùng nến <= i; khung cao chỉ dùng nến đã đóng trước nến i.
"""
from statistics import mean


# ---------- chuỗi ----------
def ema(v, n):
    k = 2 / (n + 1)
    out, e = [], None
    for x in v:
        e = x if e is None else x * k + e * (1 - k)
        out.append(e)
    return out


def sma(v, n):
    out, s = [], 0.0
    for i, x in enumerate(v):
        s += x
        if i >= n:
            s -= v[i - n]
        out.append(s / n if i >= n - 1 else None)
    return out


def wilder(v, n):
    out, e = [], None
    for i, x in enumerate(v):
        if x is None:
            out.append(None); continue
        if e is None:
            e = x if i < n - 1 else x
        e = x if i < n else (e * (n - 1) + x) / n
        out.append(e if i >= n - 1 else None)
    return out


def tr(k):
    return [k[0]["h"] - k[0]["l"]] + [max(k[i]["h"] - k[i]["l"], abs(k[i]["h"] - k[i - 1]["c"]), abs(k[i]["l"] - k[i - 1]["c"])) for i in range(1, len(k))]


def atr(k, n=14):
    return wilder(tr(k), n)


def rsi(c, n=14):
    out = [None] * len(c)
    ag = al = None
    for i in range(1, len(c)):
        d = c[i] - c[i - 1]
        g, l = max(d, 0), max(-d, 0)
        if i <= n:
            ag = (ag or 0) + g / n; al = (al or 0) + l / n
            if i == n:
                out[i] = 100 - 100 / (1 + ag / al) if al else 100.0
            continue
        ag = (ag * (n - 1) + g) / n; al = (al * (n - 1) + l) / n
        out[i] = 100 - 100 / (1 + ag / al) if al else 100.0
    return out


def high_index(k, kh, cfg):
    """Với mỗi nến khung chính i: chỉ số nến khung cao gần nhất ĐÃ ĐÓNG trước khi nến i mở."""
    out, j = [], -1
    for bar in k:
        while j + 1 < len(kh) and kh[j + 1]["t"] + cfg["high_ms"] <= bar["t"]:
            j += 1
        out.append(j)
    return out


def _hold(k, enter, exit_, long_only=False):
    """Khung chung: enter(i) -> 1/-1/0, exit_(i, pos) -> True để thoát."""
    sig, pos = [], 0
    for i in range(len(k)):
        if pos != 0 and exit_(i, pos):
            pos = 0
        if pos == 0:
            e = enter(i)
            if e and not (long_only and e == -1):
                pos = e
        sig.append(pos)
    return sig


# ---------- 1. Larry Connors RSI(2) ----------
def strat_rsi2(k, kh, cfg):
    """Connors: giá trên SMA200 và RSI(2) < 10 -> long, thoát khi đóng trên SMA5. Ngược lại cho short."""
    c = [x["c"] for x in k]
    r2, s200, s5 = rsi(c, 2), sma(c, 200), sma(c, 5)
    def enter(i):
        if s200[i] is None or r2[i] is None:
            return 0
        if c[i] > s200[i] and r2[i] < 10:
            return 1
        if c[i] < s200[i] and r2[i] > 90:
            return -1
        return 0
    def exit_(i, pos):
        return s5[i] is not None and ((pos == 1 and c[i] > s5[i]) or (pos == -1 and c[i] < s5[i]))
    return _hold(k, enter, exit_)


# ---------- 2. Golden / death cross 50/200 ----------
def strat_golden_cross(k, kh, cfg):
    c = [x["c"] for x in k]
    s50, s200 = sma(c, 50), sma(c, 200)
    return [0 if s200[i] is None else (1 if s50[i] > s200[i] else -1) for i in range(len(c))]


# ---------- 3. MACD histogram + lọc EMA200 ----------
def strat_macd(k, kh, cfg):
    c = [x["c"] for x in k]
    m = [a - b for a, b in zip(ema(c, 12), ema(c, 26))]
    sig_line = ema(m, 9)
    e200 = ema(c, 200)
    out = []
    for i in range(len(c)):
        if i < 200:
            out.append(0); continue
        h = m[i] - sig_line[i]
        out.append(1 if h > 0 and c[i] > e200[i] else -1 if h < 0 and c[i] < e200[i] else 0)
    return out


# ---------- 4. Supertrend (10, 3) ----------
def supertrend(k, n=10, mult=3.0):
    a = atr(k, n)
    up = dn = None; trend = []; t = 0
    fu = fd = None
    for i, bar in enumerate(k):
        if a[i] is None:
            trend.append(0); continue
        mid = (bar["h"] + bar["l"]) / 2
        bu, bd = mid + mult * a[i], mid - mult * a[i]
        fu = bu if fu is None or bu < fu or k[i - 1]["c"] > fu else fu
        fd = bd if fd is None or bd > fd or k[i - 1]["c"] < fd else fd
        if t <= 0 and bar["c"] > fu:
            t = 1
        elif t >= 0 and bar["c"] < fd:
            t = -1
        elif t == 0:
            t = 1 if bar["c"] > fd else -1
        trend.append(t)
    return trend


def strat_supertrend(k, kh, cfg):
    return supertrend(k)


# ---------- 5. Parabolic SAR ----------
def strat_psar(k, kh, cfg, step=0.02, mx=0.2):
    if len(k) < 3:
        return [0] * len(k)
    sig = [0, 0]
    t = 1 if k[1]["c"] > k[0]["c"] else -1
    ep = k[1]["h"] if t == 1 else k[1]["l"]
    sar = k[0]["l"] if t == 1 else k[0]["h"]
    af = step
    for i in range(2, len(k)):
        sar = sar + af * (ep - sar)
        if t == 1:
            sar = min(sar, k[i - 1]["l"], k[i - 2]["l"])
            if k[i]["l"] < sar:
                t, sar, ep, af = -1, ep, k[i]["l"], step
            elif k[i]["h"] > ep:
                ep, af = k[i]["h"], min(af + step, mx)
        else:
            sar = max(sar, k[i - 1]["h"], k[i - 2]["h"])
            if k[i]["h"] > sar:
                t, sar, ep, af = 1, ep, k[i]["h"], step
            elif k[i]["l"] < ep:
                ep, af = k[i]["l"], min(af + step, mx)
        sig.append(t)
    return sig


# ---------- 6. Ichimoku ----------
def strat_ichimoku(k, kh, cfg):
    """Tenkan 9 / Kijun 26 / mây 52 (dịch 26). Long: giá trên mây và Tenkan > Kijun; short ngược lại; thoát khi giá vào mây."""
    h = [x["h"] for x in k]; l = [x["l"] for x in k]; c = [x["c"] for x in k]
    def mid(n, i):
        return (max(h[i - n + 1 : i + 1]) + min(l[i - n + 1 : i + 1])) / 2
    sig, pos = [], 0
    for i in range(len(k)):
        if i < 52 + 26:
            sig.append(0); continue
        tenkan, kijun = mid(9, i), mid(26, i)
        j = i - 26  # mây tại nến i được vẽ từ nến j
        sa = (mid(9, j) + mid(26, j)) / 2; sb = mid(52, j)
        top, bot = max(sa, sb), min(sa, sb)
        if pos == 1 and c[i] < top:
            pos = 0
        elif pos == -1 and c[i] > bot:
            pos = 0
        if pos == 0:
            if c[i] > top and tenkan > kijun:
                pos = 1
            elif c[i] < bot and tenkan < kijun:
                pos = -1
        sig.append(pos)
    return sig


# ---------- 7. Keltner breakout (Chester Keltner / Linda Raschke) ----------
def strat_keltner(k, kh, cfg):
    """Đóng trên EMA20 + 2 ATR10 -> long tới khi đóng dưới EMA20; ngược lại cho short."""
    c = [x["c"] for x in k]
    e20, a = ema(c, 20), atr(k, 10)
    def enter(i):
        if a[i] is None or i < 20:
            return 0
        return 1 if c[i] > e20[i] + 2 * a[i] else -1 if c[i] < e20[i] - 2 * a[i] else 0
    def exit_(i, pos):
        return (pos == 1 and c[i] < e20[i]) or (pos == -1 and c[i] > e20[i])
    return _hold(k, enter, exit_)


# ---------- 8. Bollinger mean reversion + lọc SMA200 ----------
def strat_bb_revert(k, kh, cfg):
    c = [x["c"] for x in k]
    s20, s200 = sma(c, 20), sma(c, 200)
    sd = [None] * len(c)
    for i in range(19, len(c)):
        w = c[i - 19 : i + 1]; m = s20[i]
        sd[i] = (sum((x - m) ** 2 for x in w) / 20) ** 0.5
    def enter(i):
        if s200[i] is None or sd[i] is None:
            return 0
        if c[i] > s200[i] and c[i] < s20[i] - 2 * sd[i]:
            return 1
        if c[i] < s200[i] and c[i] > s20[i] + 2 * sd[i]:
            return -1
        return 0
    def exit_(i, pos):
        return (pos == 1 and c[i] >= s20[i]) or (pos == -1 and c[i] <= s20[i])
    return _hold(k, enter, exit_)


# ---------- 9. Minervini trend template ----------
def strat_minervini(k, kh, cfg):
    """Long khi: giá > SMA50 > SMA150 > SMA200, SMA200 tăng so với 20 nến trước, giá >= 1,25 đáy 250 nến và >= 0,75 đỉnh 250 nến.
    Thoát khi giá đóng dưới SMA50. Short đối xứng."""
    c = [x["c"] for x in k]
    s50, s150, s200 = sma(c, 50), sma(c, 150), sma(c, 200)
    def enter(i):
        if i < 250 or s200[i] is None:
            return 0
        lo, hi = min(c[i - 250 : i]), max(c[i - 250 : i])
        if c[i] > s50[i] > s150[i] > s200[i] and s200[i] > s200[i - 20] and c[i] >= 1.25 * lo and c[i] >= 0.75 * hi:
            return 1
        if c[i] < s50[i] < s150[i] < s200[i] and s200[i] < s200[i - 20] and c[i] <= 0.75 * hi and c[i] <= 1.25 * lo:
            return -1
        return 0
    def exit_(i, pos):
        return (pos == 1 and c[i] < s50[i]) or (pos == -1 and c[i] > s50[i])
    return _hold(k, enter, exit_)


# ---------- 10. Nền tích lũy rồi bung với khối lượng (O'Neil / VCP) ----------
def strat_base_breakout(k, kh, cfg):
    """Biên độ 20 nến co lại (ATR10 thấp hơn ATR10 cách 20 nến >= 25%), rồi đóng trên đỉnh 20 nến với khối lượng >= 1,5x TB 20 -> long.
    Thoát khi đóng dưới đáy 10 nến. Short đối xứng."""
    c = [x["c"] for x in k]; v = [x["v"] for x in k]
    a = atr(k, 10)
    def enter(i):
        if i < 60 or a[i] is None or a[i - 20] is None:
            return 0
        contracted = a[i] <= 0.75 * a[i - 20]
        vol_ok = v[i] >= 1.5 * mean(v[i - 20 : i])
        hi = max(x["h"] for x in k[i - 20 : i]); lo = min(x["l"] for x in k[i - 20 : i])
        if contracted and vol_ok:
            if c[i] > hi:
                return 1
            if c[i] < lo:
                return -1
        return 0
    def exit_(i, pos):
        lx = min(x["l"] for x in k[i - 10 : i]); hx = max(x["h"] for x in k[i - 10 : i])
        return (pos == 1 and c[i] < lx) or (pos == -1 and c[i] > hx)
    return _hold(k, enter, exit_)


# ---------- 11. Elder Triple Screen ----------
def strat_elder(k, kh, cfg):
    """Màn 1: khung cao, EMA13 dốc lên -> chỉ long (dốc xuống -> chỉ short).
    Màn 2: khung chính, Force Index EMA2 < 0 (hồi) rồi màn 3: nến đóng trên đỉnh nến trước -> long. Thoát khi màn 1 đổi chiều."""
    hi_idx = high_index(k, kh, cfg)
    he13 = ema([x["c"] for x in kh], 13)
    c = [x["c"] for x in k]
    fi = ema([(k[i]["c"] - k[i - 1]["c"]) * k[i]["v"] if i else 0.0 for i in range(len(k))], 2)
    def screen1(i):
        j = hi_idx[i]
        if j < 14:
            return 0
        return 1 if he13[j] > he13[j - 1] else -1
    def enter(i):
        if i < 2:
            return 0
        s = screen1(i)
        if s == 1 and fi[i - 1] < 0 and c[i] > k[i - 1]["h"]:
            return 1
        if s == -1 and fi[i - 1] > 0 and c[i] < k[i - 1]["l"]:
            return -1
        return 0
    def exit_(i, pos):
        return screen1(i) != pos
    return _hold(k, enter, exit_)


# ---------- 12. Weinstein stage analysis ----------
def strat_weinstein(k, kh, cfg):
    """Khung cao: SMA30 dốc lên và giá trên SMA30 = giai đoạn 2 -> long; SMA30 dốc xuống và giá dưới = giai đoạn 4 -> short."""
    hi_idx = high_index(k, kh, cfg)
    hc = [x["c"] for x in kh]
    s30 = sma(hc, 30)
    out = []
    for i in range(len(k)):
        j = hi_idx[i]
        if j < 31 or s30[j] is None:
            out.append(0); continue
        if hc[j] > s30[j] and s30[j] > s30[j - 1]:
            out.append(1)
        elif hc[j] < s30[j] and s30[j] < s30[j - 1]:
            out.append(-1)
        else:
            out.append(0)
    return out


# ---------- 13. Turtle (Donchian 55 vào / 20 ra) ----------
def strat_turtle(k, kh, cfg):
    c = [x["c"] for x in k]
    def enter(i):
        if i < 55:
            return 0
        hi = max(x["h"] for x in k[i - 55 : i]); lo = min(x["l"] for x in k[i - 55 : i])
        return 1 if c[i] > hi else -1 if c[i] < lo else 0
    def exit_(i, pos):
        hx = max(x["h"] for x in k[i - 20 : i]); lx = min(x["l"] for x in k[i - 20 : i])
        return (pos == 1 and c[i] < lx) or (pos == -1 and c[i] > hx)
    return _hold(k, enter, exit_)


# ---------- 14. Opening range breakout (chỉ khung trong ngày) ----------
def _day_bars(cfg):
    return 86_400_000 // cfg["main_ms"]


def strat_orb(k, kh, cfg):
    """Biên độ 60 phút đầu ngày UTC; đóng trên đỉnh biên độ -> long (dưới đáy -> short), thoát cuối ngày hoặc khi đóng ngược lại qua biên.
    Chỉ có nghĩa ở khung < 1D."""
    if cfg["main_ms"] >= 4 * 3600_000:
        return [0] * len(k)
    n = max(1, 3600_000 // cfg["main_ms"])
    sig, pos, day, rng = [], 0, None, None
    for i, bar in enumerate(k):
        d = bar["t"] // 86_400_000
        if d != day:
            day, rng, pos, start = d, None, 0, i
        if rng is None and i - start + 1 >= n:
            w = k[start : start + n]
            rng = (min(x["l"] for x in w), max(x["h"] for x in w))
            sig.append(0); continue
        if rng is None:
            sig.append(0); continue
        if pos == 1 and bar["c"] < rng[0]:
            pos = 0
        elif pos == -1 and bar["c"] > rng[1]:
            pos = 0
        if pos == 0:
            if bar["c"] > rng[1]:
                pos = 1
            elif bar["c"] < rng[0]:
                pos = -1
        sig.append(pos)
    return sig


# ---------- 15. VWAP ngày hồi về trung bình (khung trong ngày) ----------
def strat_vwap_revert(k, kh, cfg):
    """VWAP neo đầu ngày UTC và độ lệch chuẩn theo khối lượng; đóng dưới VWAP - 2 sd -> long tới khi chạm VWAP; ngược lại cho short."""
    if cfg["main_ms"] >= 4 * 3600_000:
        return [0] * len(k)
    sig, pos, day = [], 0, None
    pv = vv = pv2 = 0.0
    for bar in k:
        d = bar["t"] // 86_400_000
        if d != day:
            day, pv, vv, pv2, pos = d, 0.0, 0.0, 0.0, 0
        tp = (bar["h"] + bar["l"] + bar["c"]) / 3
        pv += tp * bar["v"]; vv += bar["v"]; pv2 += tp * tp * bar["v"]
        if vv <= 0:
            sig.append(0); continue
        vwap = pv / vv
        sd = max(pv2 / vv - vwap * vwap, 0) ** 0.5
        if pos == 1 and bar["c"] >= vwap:
            pos = 0
        elif pos == -1 and bar["c"] <= vwap:
            pos = 0
        if pos == 0 and sd > 0:
            if bar["c"] < vwap - 2 * sd:
                pos = 1
            elif bar["c"] > vwap + 2 * sd:
                pos = -1
        sig.append(pos)
    return sig


# ---------- 16. Đồng thuận nhiều biểu đồ (loại trừ sai số) ----------
def strat_vote(k, kh, cfg):
    """Ba họ ít tương quan: Supertrend (xu hướng), Keltner (bung biên), Weinstein khung cao (bối cảnh).
    Vào khi >= 2/3 cùng chiều và không cái nào ngược; thoát khi còn < 2 đồng thuận."""
    a, b, w = supertrend(k), strat_keltner(k, kh, cfg), strat_weinstein(k, kh, cfg)
    sig, pos = [], 0
    for i in range(len(k)):
        votes = [a[i], b[i], w[i]]
        up, dn = votes.count(1), votes.count(-1)
        if pos == 1 and up < 2:
            pos = 0
        elif pos == -1 and dn < 2:
            pos = 0
        if pos == 0:
            if up >= 2 and dn == 0:
                pos = 1
            elif dn >= 2 and up == 0:
                pos = -1
        sig.append(pos)
    return sig


def strat_vote_mtf(k, kh, cfg):
    """Như trên nhưng bắt buộc khung cao (Weinstein) cùng chiều: lọc đa khung thời gian."""
    v, w = strat_vote(k, kh, cfg), strat_weinstein(k, kh, cfg)
    return [x if x == y else 0 for x, y in zip(v, w)]


# ---------- 17. Darvas box ----------
def strat_darvas(k, kh, cfg, confirm=3, lookback=250):
    """Hộp Darvas: sau đỉnh mới `lookback` nến, đỉnh hộp = đỉnh không bị vượt trong 3 nến, đáy hộp = đáy không bị thủng trong 3 nến.
    Long khi đóng trên đỉnh hộp với khối lượng > TB 20; thoát khi đóng dưới đáy hộp (đáy được nâng theo hộp mới). Short đối xứng."""
    h = [x["h"] for x in k]; l = [x["l"] for x in k]; c = [x["c"] for x in k]; v = [x["v"] for x in k]
    sig, pos, box = [], 0, None
    for i in range(len(k)):
        if i < lookback:
            sig.append(0); continue
        # hộp xác nhận tại nến i: đỉnh tại i-confirm cao nhất trong 2*confirm+1 nến quanh nó và là đỉnh lookback
        j = i - confirm
        if h[j] == max(h[j - confirm : i + 1]) and h[j] >= max(h[i - lookback : j]):
            lo = min(l[j : i + 1])
            box = (lo, h[j])
        if l[j] == min(l[j - confirm : i + 1]) and l[j] <= min(l[i - lookback : j]):
            hi = max(h[j : i + 1])
            box = (l[j], hi)
        if pos == 1 and box and c[i] < box[0]:
            pos = 0
        elif pos == -1 and box and c[i] > box[1]:
            pos = 0
        if pos == 0 and box and v[i] > mean(v[i - 20 : i]):
            if c[i] > box[1]:
                pos = 1
            elif c[i] < box[0]:
                pos = -1
        sig.append(pos)
    return sig


# ---------- 18. Bollinger %b (Connors) ----------
def strat_pct_b(k, kh, cfg):
    """%b < 0,2 ba nến liên tiếp và giá trên SMA200 -> long; thoát khi %b > 0,8. Short đối xứng."""
    c = [x["c"] for x in k]
    s20, s200 = sma(c, 20), sma(c, 200)
    pb = [None] * len(c)
    for i in range(19, len(c)):
        w = c[i - 19 : i + 1]; m = s20[i]
        sd = (sum((x - m) ** 2 for x in w) / 20) ** 0.5
        pb[i] = (c[i] - (m - 2 * sd)) / (4 * sd) if sd else 0.5
    def enter(i):
        if i < 200 or s200[i] is None or pb[i - 2] is None:
            return 0
        if c[i] > s200[i] and all(pb[j] < 0.2 for j in (i - 2, i - 1, i)):
            return 1
        if c[i] < s200[i] and all(pb[j] > 0.8 for j in (i - 2, i - 1, i)):
            return -1
        return 0
    def exit_(i, pos):
        return (pos == 1 and pb[i] > 0.8) or (pos == -1 and pb[i] < 0.2)
    return _hold(k, enter, exit_)


# ---------- 19. Động lượng tuyệt đối (Antonacci) ----------
def strat_abs_momentum(k, kh, cfg, lookback=90):
    """Lợi nhuận `lookback` nến > 0 -> long, < 0 -> short (nửa 'tuyệt đối' của dual momentum, không có tài sản an toàn)."""
    c = [x["c"] for x in k]
    return [0 if i < lookback else (1 if c[i] > c[i - lookback] else -1) for i in range(len(c))]


STRATS = {
    "st_rsi2": ("CK: Connors RSI(2) hồi về trung bình + SMA200", strat_rsi2),
    "st_golden": ("CK: cắt SMA50/200 (golden/death cross)", strat_golden_cross),
    "st_macd": ("CK: MACD histogram + lọc EMA200", strat_macd),
    "st_supertrend": ("CK: Supertrend 10/3", strat_supertrend),
    "st_psar": ("CK: Parabolic SAR", strat_psar),
    "st_ichimoku": ("CK: Ichimoku (mây + Tenkan/Kijun)", strat_ichimoku),
    "st_keltner": ("CK: bung kênh Keltner EMA20 ± 2 ATR", strat_keltner),
    "st_bb_revert": ("CK: Bollinger hồi về trung bình + SMA200", strat_bb_revert),
    "st_minervini": ("CK: Minervini trend template", strat_minervini),
    "st_base": ("CK: nền co biên rồi bung với khối lượng (O'Neil/VCP)", strat_base_breakout),
    "st_elder": ("CK: Elder Triple Screen (khung cao + Force Index)", strat_elder),
    "st_weinstein": ("CK: Weinstein giai đoạn 2/4 (SMA30 khung cao)", strat_weinstein),
    "st_turtle": ("CK: Turtle Donchian 55/20", strat_turtle),
    "st_orb": ("CK: bung biên độ 60 phút đầu ngày (chỉ khung < 4h)", strat_orb),
    "st_vwap": ("CK: VWAP ngày hồi về trung bình (chỉ khung < 4h)", strat_vwap_revert),
    "st_darvas": ("CK: hộp Darvas (đỉnh mới + khối lượng)", strat_darvas),
    "st_pct_b": ("CK: Bollinger %b < 0,2 ba nến + SMA200 (Connors)", strat_pct_b),
    "st_abs_mom": ("CK: động lượng tuyệt đối 90 nến (Antonacci)", strat_abs_momentum),
    "st_vote": ("Đồng thuận 2/3: Supertrend + Keltner + Weinstein", strat_vote),
    "st_vote_mtf": ("Đồng thuận 2/3 bắt buộc cùng chiều khung cao", strat_vote_mtf),
}
