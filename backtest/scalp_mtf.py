"""Backtest SCALP ĐA KHUNG: cùng một bộ cách vào lệnh chạy trên 5m, 15m, 30m, 1h, mỗi cách thử thêm lọc xu hướng khung lớn
(EMA20/50 của 1h, 4h, 1D, hoặc 4h và 1D cùng chiều). Mục tiêu: tìm cách nào có lợi thế ở NHIỀU khung chứ không chỉ một.

Dữ liệu: nến 5m OKX (3 năm) gộp thành 15m / 30m / 1h nên mọi khung cùng một nguồn; nến 4h và 1D tải riêng.
Mô phỏng (giống backtest/scalp.py, thêm chi phí thực tế hơn):
  - vào lệnh thị trường ở giá mở nến sau tín hiệu: phí taker 0,05% + trượt giá 0,01%; lệnh chờ: phí maker 0,02%, chờ tối đa 4 nến;
  - chốt lời là lệnh chờ: phí maker 0,02%, không trượt giá; dừng lỗ và đóng theo thời gian: taker 0,05% + trượt 0,01%;
  - cùng nến chạm cả chốt lời lẫn dừng lỗ tính là dừng lỗ; nến mở vượt mức thì khớp ở giá mở; một lệnh một lúc.
Chọn tham số: lưới TP {1; 1,5; 2; 3} ATR × SL {0,5; 1; 1,5} ATR × giữ {8; 16; 48} nến, chọn TRONG MẪU (70% đầu) theo PF trung bình
của cả 3 đồng (mỗi đồng >= 30 lệnh), bộ lọc khung lớn cũng chọn trong mẫu; rồi mới xem NGOÀI MẪU (30% cuối) với đúng tham số đó.
Agent review (quy tắc cố định, ghi ở cột kết luận):
  GIỮ      PF ngoài mẫu >= 1,15 ở ít nhất 2 đồng, không đồng nào < 0,95, tổng >= 60 lệnh, hai nửa ngoài mẫu đều PF >= 1, PF trong mẫu >= 1,05
  THEO DÕI PF ngoài mẫu trung bình >= 1,05 và ít nhất 2 đồng > 1
  BỎ       còn lại
"""
import datetime as dt
import json
import math
import os
import sys
from statistics import mean

try:
    from backtest import scalp as S
except ImportError:  # chạy trực tiếp
    import scalp as S

DATA = S.DATA
SYMS = S.SYMS
TAKER, MAKER, SLIP = 0.0005, 0.0002, 0.0001
TP_GRID, SL_GRID, HOLD_GRID = S.TP_GRID, S.SL_GRID, S.HOLD_GRID
MAX_HOLD = max(HOLD_GRID)
DAY, HOUR, BASE_MS = 86_400_000, 3_600_000, 300_000
INF = float("inf")
FRAMES = {
    "5m": dict(mult=1, ms=BASE_MS, bars_per_day=288, vp_window=288, orb_bars=12, filters=("none", "1h", "4h", "1d", "4h+1d")),
    "15m": dict(mult=3, ms=3 * BASE_MS, bars_per_day=96, vp_window=96, orb_bars=4, filters=("none", "1h", "4h", "1d", "4h+1d")),
    "30m": dict(mult=6, ms=6 * BASE_MS, bars_per_day=48, vp_window=96, orb_bars=2, filters=("none", "1h", "4h", "1d", "4h+1d")),
    "1h": dict(mult=12, ms=12 * BASE_MS, bars_per_day=24, vp_window=168, orb_bars=1, filters=("none", "4h", "1d", "4h+1d")),
}
FILTER_LABEL = {"none": "không lọc", "1h": "lọc 1h", "4h": "lọc 4h", "1d": "lọc ngày", "4h+1d": "lọc 4h + ngày"}


# ---------- dữ liệu ----------
def aggregate(k, mult, base_ms=BASE_MS):
    """Gộp nến nhỏ thành nến lớn gấp `mult` lần (neo theo giờ UTC). Bỏ nến lớn cuối nếu chưa đủ nến con."""
    if mult == 1:
        return k
    size = mult * base_ms
    out, cur, cnt, bucket = [], None, 0, None
    for b in k:
        t0 = b["t"] // size * size
        if t0 != bucket:
            if cur is not None:
                out.append(cur)
            bucket, cnt = t0, 0
            cur = {"t": t0, "o": b["o"], "h": b["h"], "l": b["l"], "c": b["c"], "v": b["v"]}
        else:
            cur["h"] = max(cur["h"], b["h"]); cur["l"] = min(cur["l"], b["l"]); cur["c"] = b["c"]; cur["v"] += b["v"]
        cnt += 1
    if cur is not None and cnt == mult:
        out.append(cur)
    return out


# ---------- chỉ báo thêm ----------
def sma(v, n):
    out, s = [None] * len(v), 0.0
    for i, x in enumerate(v):
        s += x
        if i >= n:
            s -= v[i - n]
        if i >= n - 1:
            out[i] = s / n
    return out


def stoch_rsi(c, n=14, k_n=3, d_n=3):
    r = S.rsi14(c, n)
    raw = [None] * len(c)
    for i in range(len(c)):
        w = [x for x in r[max(0, i - n + 1) : i + 1] if x is not None]
        if len(w) == n:
            lo, hi = min(w), max(w)
            raw[i] = 0.0 if hi == lo else (r[i] - lo) / (hi - lo) * 100
    def _sma_opt(v, m):
        out = [None] * len(v)
        for i in range(m - 1, len(v)):
            w = v[i - m + 1 : i + 1]
            if all(x is not None for x in w):
                out[i] = sum(w) / m
        return out
    kk = _sma_opt(raw, k_n)
    return kk, _sma_opt(kk, d_n)


def rolling_hl(k, n=20):
    """Đỉnh / đáy của n nến TRƯỚC nến i (không gồm nến i)."""
    hh, ll = [None] * len(k), [None] * len(k)
    from collections import deque
    qh, ql = deque(), deque()
    for i in range(len(k)):
        if i >= n:
            hh[i] = k[qh[0]]["h"]; ll[i] = k[ql[0]]["l"]
        while qh and k[qh[-1]]["h"] <= k[i]["h"]:
            qh.pop()
        qh.append(i)
        while ql and k[ql[-1]]["l"] >= k[i]["l"]:
            ql.pop()
        ql.append(i)
        while qh[0] <= i - n:
            qh.popleft()
        while ql[0] <= i - n:
            ql.popleft()
    return hh, ll


def context(k, cfg, kh):
    """Ngữ cảnh của scalp.py + chỉ báo thêm + xu hướng các khung lớn. kh: {'1h': nến 1h, '4h': ..., '1d': ...}."""
    ctx = S.context(k, cfg, kh)
    c = [x["c"] for x in k]
    ctx["e8"], ctx["e13"], ctx["e21"], ctx["e200"] = S.ema(c, 8), S.ema(c, 13), S.ema(c, 21), S.ema(c, 200)
    ctx["rsi2"] = S.rsi14(c, 2)
    ctx["srsi_k"], ctx["srsi_d"] = stoch_rsi(c)
    e12, e26 = S.ema(c, 12), S.ema(c, 26)
    macd = [a - b for a, b in zip(e12, e26)]
    sig = S.ema(macd, 9)
    ctx["macd"], ctx["macd_hist"] = macd, [a - b for a, b in zip(macd, sig)]
    ctx["hh20"], ctx["ll20"] = rolling_hl(k, 20)
    ctx["sma20"] = sma(c, 20)
    ctx["ms"] = cfg["ms"]
    reg = {"4h": ctx["reg4h"], "1d": ctx["reg1d"]}
    if kh.get("1h") and cfg["ms"] < HOUR:
        reg["1h"] = S.regime_from(k, kh["1h"], HOUR)
    ctx["reg"] = reg
    return ctx


# ---------- tín hiệu mới: (i, hướng, giá chờ | None, TP riêng | None, SL riêng | None, số nến giữ riêng | None) ----------
def _mod(t):
    return t % DAY


def sig_ema_ribbon(k, ctx):
    """Dải EMA 8/13/21 xếp tầng, nến trước hồi chạm EMA21, nến này đóng trên EMA8 và vượt đỉnh nến trước -> theo xu hướng."""
    e8, e13, e21 = ctx["e8"], ctx["e13"], ctx["e21"]
    out = []
    for i in range(60, len(k)):
        b, p = k[i], k[i - 1]
        up = e8[i] > e13[i] > e21[i] and e8[i - 1] > e13[i - 1] > e21[i - 1]
        dn = e8[i] < e13[i] < e21[i] and e8[i - 1] < e13[i - 1] < e21[i - 1]
        if up and p["l"] <= e21[i - 1] and b["c"] > e8[i] and b["c"] > p["h"]:
            out.append((i, 1, None, None, None, None))
        elif dn and p["h"] >= e21[i - 1] and b["c"] < e8[i] and b["c"] < p["l"]:
            out.append((i, -1, None, None, None, None))
    return out


def sig_stochrsi(k, ctx):
    """Stoch RSI 14/14/3/3: K cắt lên D dưới 20 khi giá trên EMA50 -> long; cắt xuống trên 80 khi giá dưới EMA50 -> short."""
    K, D, e50 = ctx["srsi_k"], ctx["srsi_d"], ctx["e50"]
    out = []
    for i in range(60, len(k)):
        if None in (K[i], D[i], K[i - 1], D[i - 1]):
            continue
        c = k[i]["c"]
        if K[i - 1] <= D[i - 1] and K[i] > D[i] and max(K[i], D[i]) < 20 and c > e50[i]:
            out.append((i, 1, None, None, None, None))
        elif K[i - 1] >= D[i - 1] and K[i] < D[i] and min(K[i], D[i]) > 80 and c < e50[i]:
            out.append((i, -1, None, None, None, None))
    return out


def sig_rsi2(k, ctx):
    """Connors RSI(2): RSI2 vừa xuống dưới 10 khi giá trên EMA200 -> mua hồi; vừa lên trên 90 khi dưới EMA200 -> bán."""
    r, e200 = ctx["rsi2"], ctx["e200"]
    out = []
    for i in range(201, len(k)):
        if r[i] is None or r[i - 1] is None:
            continue
        c = k[i]["c"]
        if r[i] < 10 <= r[i - 1] and c > e200[i]:
            out.append((i, 1, None, None, None, None))
        elif r[i] > 90 >= r[i - 1] and c < e200[i]:
            out.append((i, -1, None, None, None, None))
    return out


def sig_donchian(k, ctx):
    """Đóng vượt đỉnh 20 nến trước -> long, thủng đáy 20 nến -> short (quy tắc MAX/MIN của Quantpedia, thu nhỏ về khung giờ)."""
    hh, ll = ctx["hh20"], ctx["ll20"]
    out = []
    for i in range(21, len(k)):
        if hh[i] is None or hh[i - 1] is None:
            continue
        c, pc = k[i]["c"], k[i - 1]["c"]
        if c > hh[i] and pc <= hh[i - 1]:
            out.append((i, 1, None, None, None, None))
        elif c < ll[i] and pc >= ll[i - 1]:
            out.append((i, -1, None, None, None, None))
    return out


def sig_macd(k, ctx):
    """MACD 12/26/9: histogram đổi dấu lên khi MACD còn dưới 0 và giá trên EMA200 -> long; đối xứng cho short."""
    h, m, e200 = ctx["macd_hist"], ctx["macd"], ctx["e200"]
    out = []
    for i in range(201, len(k)):
        c = k[i]["c"]
        if h[i - 1] <= 0 < h[i] and m[i] < 0 and c > e200[i]:
            out.append((i, 1, None, None, None, None))
        elif h[i - 1] >= 0 > h[i] and m[i] > 0 and c < e200[i]:
            out.append((i, -1, None, None, None, None))
    return out


def sig_ttm(k, ctx):
    """TTM Squeeze (John Carter): Bollinger 20/2 nằm trong Keltner 20/1,5 ATR >= 6 nến rồi bung ra; hướng theo giá so với SMA20."""
    up, lo, a, e20, s20 = ctx["bb_up"], ctx["bb_lo"], ctx["atr"], ctx["e20"], ctx["sma20"]
    on = [None] * len(k)
    for i in range(len(k)):
        if up[i] is None or a[i] is None:
            continue
        on[i] = up[i] < e20[i] + 1.5 * a[i] and lo[i] > e20[i] - 1.5 * a[i]
    out = []
    for i in range(30, len(k)):
        if on[i] is not False or not all(on[j] for j in range(i - 6, i)):
            continue
        c = k[i]["c"]
        if c > s20[i]:
            out.append((i, 1, None, None, None, None))
        elif c < s20[i]:
            out.append((i, -1, None, None, None, None))
    return out


def sig_vwap_trend(k, ctx):
    """Xu hướng EMA20 > EMA50, nến hồi chạm VWAP phiên rồi đóng trên VWAP, nến xanh -> long (đi theo xu hướng); đối xứng."""
    vw, nb, e20, e50 = ctx["vwap"], ctx["vnb"], ctx["e20"], ctx["e50"]
    out = []
    for i in range(60, len(k)):
        if vw[i] is None or nb[i] < 6:
            continue
        b = k[i]
        if e20[i] > e50[i] and b["l"] <= vw[i] < b["c"] and b["c"] > b["o"]:
            out.append((i, 1, None, None, None, None))
        elif e20[i] < e50[i] and b["h"] >= vw[i] > b["c"] and b["c"] < b["o"]:
            out.append((i, -1, None, None, None, None))
    return out


def _asia(k, i, day_start, cache):
    """Đỉnh/đáy phiên Á 00:00-07:00 UTC của ngày chứa nến i (chỉ khi đã kết thúc)."""
    if day_start not in cache:
        hi = lo = None
        j = i
        while j >= 0 and k[j]["t"] >= day_start:
            j -= 1
        for m in range(j + 1, len(k)):
            if k[m]["t"] >= day_start + 7 * HOUR:
                break
            hi = k[m]["h"] if hi is None else max(hi, k[m]["h"])
            lo = k[m]["l"] if lo is None else min(lo, k[m]["l"])
        cache[day_start] = (hi, lo)
    return cache[day_start]


def sig_asia_sweep(k, ctx):
    """07:00-20:00 UTC: râu quét qua đỉnh (đáy) phiên Á rồi đóng lại vào trong -> đánh ngược, dừng lỗ ngay sau râu. Mỗi chiều một lần/ngày."""
    a, cache, out, done, cur = ctx["atr"], {}, [], set(), None
    for i, b in enumerate(k):
        ds = b["t"] - _mod(b["t"])
        if ds != cur:
            cur, done = ds, set()
        if not (7 * HOUR <= _mod(b["t"]) < 20 * HOUR) or a[i] is None:
            continue
        hi, lo = _asia(k, i, ds, cache)
        if hi is None:
            continue
        if -1 not in done and b["h"] > hi and b["c"] < hi:
            out.append((i, -1, None, None, b["h"] + 0.1 * a[i], None)); done.add(-1)
        elif 1 not in done and b["l"] < lo and b["c"] > lo:
            out.append((i, 1, None, None, b["l"] - 0.1 * a[i], None)); done.add(1)
    return out


def sig_asia_break(k, ctx):
    """London breakout: 07:00-12:00 UTC lần đầu đóng ngoài biên phiên Á -> đi theo. Một lệnh/ngày."""
    cache, out, done, cur = {}, [], False, None
    for i, b in enumerate(k):
        ds = b["t"] - _mod(b["t"])
        if ds != cur:
            cur, done = ds, False
        if done or not (7 * HOUR <= _mod(b["t"]) < 12 * HOUR):
            continue
        hi, lo = _asia(k, i, ds, cache)
        if hi is None:
            continue
        if b["c"] > hi:
            out.append((i, 1, None, None, None, None)); done = True
        elif b["c"] < lo:
            out.append((i, -1, None, None, None, None)); done = True
    return out


def sig_pdh_sweep(k, ctx):
    """Râu quét qua đỉnh (đáy) ngày hôm trước rồi đóng lại vào trong -> đánh ngược, dừng lỗ sau râu. Mỗi chiều một lần/ngày."""
    a, out = ctx["atr"], []
    cur, prev, today, done = None, None, None, set()
    for i, b in enumerate(k):
        ds = b["t"] - _mod(b["t"])
        if ds != cur:
            prev = today if cur is not None and ds - cur == DAY else None
            cur, today, done = ds, [b["h"], b["l"]], set()
        else:
            today[0] = max(today[0], b["h"]); today[1] = min(today[1], b["l"])
        if prev is None or a[i] is None or _mod(b["t"]) < HOUR:
            continue
        if -1 not in done and b["h"] > prev[0] and b["c"] < prev[0]:
            out.append((i, -1, None, None, b["h"] + 0.1 * a[i], None)); done.add(-1)
        elif 1 not in done and b["l"] < prev[1] and b["c"] > prev[1]:
            out.append((i, 1, None, None, b["l"] - 0.1 * a[i], None)); done.add(1)
    return out


def _time_signal(k, ms, enter_at, hold_ms, direction):
    """Vào ở giá mở nến bắt đầu lúc `enter_at` (ms trong ngày UTC), giữ `hold_ms`, không chốt lời / dừng lỗ."""
    if enter_at % ms or hold_ms % ms or hold_ms < ms:
        return []
    out = []
    for i in range(len(k) - 1):
        if _mod(k[i]["t"] + ms) == enter_at and k[i + 1]["t"] == k[i]["t"] + ms:
            d = direction(i)
            if d:
                out.append((i, d, None, INF * d, -INF * d, hold_ms // ms - 1))
    return out


def sig_tod22(k, ctx):
    """Mùa vụ trong ngày (Padyšák & Vojtko, SSRN 4081000): mua lúc 22:00 UTC, bán lúc 00:00 UTC. Chỉ long."""
    return _time_signal(k, ctx["ms"], 22 * HOUR, 2 * HOUR, lambda i: 1)


def _first_window_dir(k, i, start, length):
    """Hướng của đoạn [start, start+length) trong ngày chứa nến i: +1 / -1 / 0. Chỉ dùng nến đã đóng trước nến i+1."""
    ds = k[i]["t"] - _mod(k[i]["t"])
    a, b = ds + start, ds + start + length
    j = i
    while j >= 0 and k[j]["t"] >= a:
        j -= 1
    w = [x for x in k[j + 1 : i + 1] if a <= x["t"] < b]
    if not w or w[0]["t"] != a:
        return 0
    r = w[-1]["c"] - w[0]["o"]
    return 1 if r > 0 else -1 if r < 0 else 0


def sig_ism_day(k, ctx):
    """Động lượng trong ngày (Bitcoin intraday time-series momentum): chiều của 30 phút đầu ngày UTC -> lệnh 30 phút cuối ngày.
    Khung 1h dùng 1 giờ đầu -> 1 giờ cuối."""
    ms = ctx["ms"]
    w = max(30 * 60_000, ms)
    return _time_signal(k, ms, DAY - w, w, lambda i: _first_window_dir(k, i, 0, w))


def _us_open(t):
    """Giờ mở cửa chứng khoán Mỹ theo UTC (13:30 mùa hè, 14:30 mùa đông), None vào cuối tuần."""
    d = dt.datetime.fromtimestamp(t / 1000, dt.timezone.utc).date()
    if d.weekday() >= 5:
        return None
    mar = dt.date(d.year, 3, 8); nov = dt.date(d.year, 11, 1)
    dst = mar + dt.timedelta(days=(6 - mar.weekday()) % 7) <= d < nov + dt.timedelta(days=(6 - nov.weekday()) % 7)
    return int((13.5 if dst else 14.5) * HOUR)


def sig_ism_us(k, ctx):
    """Như trên nhưng theo phiên Mỹ: chiều của 30 phút đầu phiên (13:30/14:30 UTC) -> lệnh 30 phút cuối phiên (19:30/20:30 UTC)."""
    ms = ctx["ms"]
    if (30 * 60_000) % ms:
        return []
    out = []
    for i in range(len(k) - 1):
        op = _us_open(k[i]["t"])
        if op is None:
            continue
        enter = op + 6 * HOUR
        if _mod(k[i]["t"] + ms) != enter or k[i + 1]["t"] != k[i]["t"] + ms:
            continue
        d = _first_window_dir(k, i, op, 30 * 60_000)
        if d:
            out.append((i, d, None, INF * d, -INF * d, 30 * 60_000 // ms - 1))
    return out


def _old(fn):
    """Bọc tín hiệu của scalp.py (không lọc ngày, lọc làm chung ở đây) về dạng 6 phần tử."""
    return lambda k, ctx: [tuple(s) + (None,) for s in fn(k, ctx, False)]


STRATS = {
    "vp_rotation": ("VP: từ chối tại VAL/VAH", _old(S.sig_vp_rotation)),
    "vp_rotation_poc": ("VP: từ chối tại VAL/VAH, chốt ở POC", _old(S.sig_vp_rotation_poc)),
    "vp_limit": ("VP: lệnh chờ tại VAL/VAH", _old(S.sig_vp_limit)),
    "pullback": ("Hồi theo xu hướng 4h rồi vượt đỉnh nến trước", _old(S.sig_pullback)),
    "vwap_bounce": ("VWAP phiên: xuyên -1 sd rồi đóng lại", _old(S.sig_vwap_bounce)),
    "vwap_trend": ("VWAP phiên: hồi chạm VWAP theo xu hướng EMA", sig_vwap_trend),
    "squeeze": ("Nén Bollinger 48 nến rồi bung + khối lượng", _old(S.sig_squeeze)),
    "ttm": ("TTM Squeeze (Bollinger trong Keltner) bung", sig_ttm),
    "lvn_break": ("VP: thoát vùng qua node thấp + khối lượng", _old(S.sig_lvn_break)),
    "orb": ("Bung biên độ 60 phút đầu ngày UTC", _old(S.sig_orb)),
    "ema_ribbon": ("Dải EMA 8/13/21 hồi chạm EMA21", sig_ema_ribbon),
    "stochrsi": ("Stoch RSI cắt ở vùng quá mua/bán theo EMA50", sig_stochrsi),
    "rsi2": ("Connors RSI(2) < 10 / > 90 theo EMA200", sig_rsi2),
    "macd": ("MACD histogram đổi dấu theo EMA200", sig_macd),
    "donchian": ("Phá đỉnh/đáy 20 nến (Donchian)", sig_donchian),
    "asia_sweep": ("Quét đỉnh/đáy phiên Á rồi quay lại", sig_asia_sweep),
    "asia_break": ("Phá biên phiên Á giờ London", sig_asia_break),
    "pdh_sweep": ("Quét đỉnh/đáy ngày trước rồi quay lại", sig_pdh_sweep),
    "tod22": ("Mùa vụ giờ: mua 22:00, bán 00:00 UTC", sig_tod22),
    "ism_day": ("Động lượng đầu ngày -> cuối ngày UTC", sig_ism_day),
    "ism_us": ("Động lượng đầu phiên Mỹ -> cuối phiên", sig_ism_us),
}


def apply_filter(sigs, reg, f):
    if f == "none":
        return sigs
    keys = f.split("+")
    if any(x not in reg for x in keys):
        return None
    return [s for s in sigs if all(reg[x][s[0]] == s[1] for x in keys)]


# ---------- mô phỏng nhanh: tính trước điểm chạm của mọi mức TP/SL rồi chạy từng tổ hợp ----------
def prepare(k, atr, sigs, wait=4, max_hold=MAX_HOLD):
    o = [x["o"] for x in k]; h = [x["h"] for x in k]; l = [x["l"] for x in k]
    n, out = len(k), []
    for i, d, limit, tp_px, sl_px, hov in sigs:
        if i + 1 >= n or not atr[i]:
            continue
        a = atr[i]
        if limit is None:
            j, px, maker = i + 1, o[i + 1], False
        else:
            j = None
            for m in range(i + 1, min(i + 1 + wait, n)):
                if d == 1 and l[m] <= limit:
                    j, px = m, min(limit, o[m]); break
                if d == -1 and h[m] >= limit:
                    j, px = m, max(limit, o[m]); break
            if j is None:
                out.append((i, None, min(i + 1 + wait, n)))
                continue
            maker = True
        tps = [tp_px] if tp_px is not None else [px + d * m * a for m in TP_GRID]
        sls = [sl_px] if sl_px is not None else [px - d * m * a for m in SL_GRID]
        ftp, fsl = [None] * len(tps), [None] * len(sls)
        last = min(j + (hov if hov is not None else max_hold), n - 1)
        left = len(tps) + len(sls)
        for m in range(j, last + 1):
            hi, lo = h[m], l[m]
            for q, lv in enumerate(sls):
                if fsl[q] is None and (lo <= lv if d == 1 else hi >= lv):
                    fsl[q] = m; left -= 1
            for q, lv in enumerate(tps):
                if ftp[q] is None and (hi >= lv if d == 1 else lo <= lv):
                    ftp[q] = m; left -= 1
            if not left:
                break
        out.append((i, d, j, px, maker, tps, sls, ftp, fsl, hov))
    return out


def run_combo(k, prep, ti, si, hold, lo_i, hi_i, fee_tp=MAKER, slip=SLIP, fee_in_market=TAKER, fee_stop=TAKER):
    """Chạy một tổ hợp (chỉ số TP, chỉ số SL, giữ) trên các tín hiệu có lo_i <= i < hi_i. Trả về [(i, j, nến ra, lợi nhuận)]."""
    n, trades, busy = len(k), [], -1
    for e in prep:
        i = e[0]
        if i < lo_i or i >= hi_i or i < busy:
            continue
        if e[1] is None:
            busy = e[2]
            continue
        _, d, j, px, maker, tps, sls, ftp, fsl, hov = e
        qt = ti if len(tps) > 1 else 0
        qs = si if len(sls) > 1 else 0
        tp, sl = tps[qt], sls[qs]
        if d == 1 and (tp <= px or sl >= px) or d == -1 and (tp >= px or sl <= px):
            busy = j + 1
            continue
        last = min(j + (hov if hov is not None else hold), n - 1)
        ms_, mt = fsl[qs], ftp[qt]
        if ms_ is not None and ms_ <= last and (mt is None or ms_ <= mt):
            m, kind = ms_, "sl"
            xp = (min(sl, k[m]["o"]) if d == 1 else max(sl, k[m]["o"])) if m > j else sl
        elif mt is not None and mt <= last:
            m, kind = mt, "tp"
            xp = (max(tp, k[m]["o"]) if d == 1 else min(tp, k[m]["o"])) if m > j else tp
        else:
            m, kind, xp = last, "time", k[last]["c"]
        f_in = MAKER if maker else fee_in_market + slip
        f_out = fee_tp if kind == "tp" else fee_stop + slip
        trades.append((i, j, m, (xp / px - 1) * d - f_in - f_out))
        busy = m + 1
    return trades


def _sums(trades):
    w = sum(t[3] for t in trades if t[3] > 0)
    return w, -sum(t[3] for t in trades if t[3] <= 0)


def evaluate(k, cfg, prep, cut):
    """Lưới trong mẫu và ngoài mẫu cho mọi tổ hợp; kèm tổng lãi/lỗ hai nửa ngoài mẫu để soát độ ổn định."""
    n = len(k)
    mid = cut + (n - cut) // 2
    gis, goos = {}, {}
    for ti, tp in enumerate(TP_GRID):
        for si, sl in enumerate(SL_GRID):
            for hold in HOLD_GRID:
                key = f"{tp}/{sl}/{hold}"
                gis[key] = S.metrics(run_combo(k, prep, ti, si, hold, 0, cut), cut, cfg["bars_per_day"])
                tr = run_combo(k, prep, ti, si, hold, cut, n)
                m = S.metrics(tr, n - cut, cfg["bars_per_day"])
                m["halves"] = [_sums([t for t in tr if t[0] < mid]), _sums([t for t in tr if t[0] >= mid])]
                goos[key] = m
    return gis, goos


def _pf(m):
    return min(m.get("profit_factor", 0.0) if m.get("n") else 0.0, 5.0)


def pool(per_sym):
    """per_sym: {đồng: (lưới trong mẫu, lưới ngoài mẫu)} -> tổ hợp chung chọn trong mẫu + kết quả ngoài mẫu + kết luận review."""
    combos = list(next(iter(per_sym.values()))[0].keys())
    best, best_pf = None, 0.0
    for c in combos:
        ms = [per_sym[s][0][c] for s in per_sym]
        if all(m.get("n", 0) >= 30 for m in ms):
            pf = mean(_pf(m) for m in ms)
            if pf > best_pf:
                best, best_pf = c, pf
    if not best:
        return {"best": None, "verdict": "BỎ", "why": "trong mẫu không tổ hợp nào đủ 30 lệnh mỗi đồng"}
    oos = {s: {k: v for k, v in per_sym[s][1][best].items() if k != "halves"} for s in per_sym}
    halves = []
    for h in (0, 1):
        w = sum(per_sym[s][1][best]["halves"][h][0] for s in per_sym)
        lo = sum(per_sym[s][1][best]["halves"][h][1] for s in per_sym)
        halves.append(w / lo if lo else (5.0 if w else 0.0))
    pfs = [_pf(oos[s]) for s in per_sym]
    n_tot = sum(oos[s].get("n", 0) for s in per_sym)
    good = sum(p >= 1.15 for p in pfs)
    bad = any(_pf(oos[s]) < 0.95 and oos[s].get("n", 0) >= 20 for s in per_sym)
    if good >= 2 and not bad and n_tot >= 60 and min(halves) >= 1.0 and best_pf >= 1.05:
        verdict, why = "GIỮ", "lãi ngoài mẫu ở >= 2 đồng, không đồng nào lỗ rõ, hai nửa ngoài mẫu đều dương"
    elif mean(pfs) >= 1.05 and sum(p > 1 for p in pfs) >= 2:
        verdict = "THEO DÕI"
        why = "ngoài mẫu hơi dương nhưng chưa đủ chuẩn giữ: " + ", ".join(
            x for x, ok in (("ít đồng đạt PF 1,15", good < 2), ("có đồng lỗ", bad), ("ít lệnh", n_tot < 60),
                            ("một nửa ngoài mẫu âm", min(halves) < 1.0), ("trong mẫu yếu", best_pf < 1.05)) if ok)
    else:
        verdict, why = "BỎ", "ngoài mẫu không có lãi đủ rõ"
    return {"best": best, "is_pf": best_pf, "oos": oos, "oos_halves_pf": halves, "oos_pf_mean": mean(pfs),
            "oos_ret_mean": mean(oos[s].get("total_return", 0.0) for s in per_sym),
            "per_day": mean(oos[s].get("per_day", 0.0) for s in per_sym), "n_oos": n_tot, "verdict": verdict, "why": why}


def load(sym, file):
    with open(os.path.join(DATA, f"{sym}_{file}.json")) as fh:
        return json.load(fh)


def run(frames=None):
    frames = frames or list(FRAMES)
    grids = {tf: {} for tf in frames}  # tf -> (strat, filter) -> sym -> (is, oos)
    meta = {tf: {} for tf in frames}
    for sym in SYMS:
        k5 = load(sym, "5m")
        kh = {"4h": load(sym, "4H"), "1d": load(sym, "1Dutc"), "1h": aggregate(k5, 12)}
        for tf in frames:
            cfg = FRAMES[tf]
            k = aggregate(k5, cfg["mult"])
            ctx = context(k, cfg, kh)
            cut = int(len(k) * 0.7)
            meta[tf][sym] = {"bars": len(k), "from": k[0]["t"], "to": k[-1]["t"], "cut_t": k[cut]["t"]}
            for key, (label, fn) in STRATS.items():
                raw = fn(k, ctx)
                prep_all = prepare(k, ctx["atr"], raw)
                for f in cfg["filters"]:
                    sigs = apply_filter(raw, ctx["reg"], f)
                    if sigs is None:
                        continue
                    keep = {s[0] for s in sigs}
                    prep = [e for e in prep_all if e[0] in keep]
                    gis, goos = evaluate(k, cfg, prep, cut)
                    grids[tf].setdefault((key, f), {})[sym] = (gis, goos)
                    meta[tf].setdefault("signals", {}).setdefault(f"{key}|{f}", {})[sym] = len(sigs)
            print(f"{sym} {tf}: {len(k)} nến, {len(STRATS)} cách", flush=True)
            del k, ctx
        del k5, kh
    out = {"frames": {}, "meta": {}}
    for tf in frames:
        res = {}
        for (key, f), per_sym in grids[tf].items():
            if len(per_sym) < len(SYMS):
                continue
            r = pool(per_sym)
            r["label"], r["filter"] = STRATS[key][0], f
            r["signals"] = meta[tf]["signals"][f"{key}|{f}"]
            res.setdefault(key, {})[f] = r
        # chọn bộ lọc theo TRONG MẪU (không nhìn ngoài mẫu)
        for key, by_f in res.items():
            cands = [(v.get("is_pf") or 0.0, f) for f, v in by_f.items() if v.get("best")]
            by_f["_chosen"] = max(cands)[1] if cands else None
        out["frames"][tf] = res
        out["meta"][tf] = {s: meta[tf][s] for s in SYMS}
    with open(os.path.join(os.path.dirname(__file__), "scalp_mtf.json"), "w") as fh:
        json.dump(out, fh, indent=1, ensure_ascii=False)
    write_md(out)
    return out


def _fmt(x, d=2):
    return "-" if x is None else ("∞" if isinstance(x, float) and math.isinf(x) else f"{x:.{d}f}")


def _cell(m):
    if not m or not m.get("n"):
        return "0 lệnh"
    return f"PF {_fmt(m['profit_factor'])} · {m['total_return']:+.0f}% · {m['n']} lệnh"


def write_md(out):
    frames = list(out["frames"])
    L = ["# Scalp đa khung · 5m, 15m, 30m, 1h · nến 5m OKX 3 năm gộp lên", "",
         "Mỗi ô: PF trung bình NGOÀI MẪU của 3 đồng (BTC, ETH, SOL) · lãi trung bình mỗi đồng · lệnh/ngày/đồng · kết luận. "
         "Bộ lọc khung lớn và tham số TP/SL/giữ đều chọn TRONG MẪU (70% đầu); ngoài mẫu là 30% cuối, chưa từng dùng để chọn. "
         "Chi phí: vào lệnh thị trường 0,05% + trượt 0,01%; chốt lời bằng lệnh chờ 0,02%; dừng lỗ 0,05% + trượt 0,01%.", ""]
    for tf in frames:
        mt = out["meta"][tf]
        a, b, c = (dt.datetime.fromtimestamp(mt["BTC"][x] / 1000, dt.timezone.utc).strftime("%Y-%m-%d") for x in ("from", "to", "cut_t"))
        L.append(f"- {tf}: {mt['BTC']['bars']} nến BTC, {a} đến {b}, ngoài mẫu từ {c}")
    L += ["", "## Tổng hợp: bộ lọc chọn trong mẫu", "", "| Cách | " + " | ".join(frames) + " |", "|---|" + "---|" * len(frames)]
    keep = []
    for key, (label, _) in STRATS.items():
        cells = []
        for tf in frames:
            by_f = out["frames"][tf].get(key) or {}
            f = by_f.get("_chosen")
            if not f:
                cells.append("không đủ lệnh"); continue
            r = by_f[f]
            cells.append(f"{_fmt(r['oos_pf_mean'])} · {r['oos_ret_mean']:+.0f}% · {_fmt(r['per_day'], 1)}/ngày · {FILTER_LABEL[f]} · **{r['verdict']}**")
            for ff, rr in by_f.items():
                if ff != "_chosen" and rr.get("verdict") in ("GIỮ", "THEO DÕI"):
                    keep.append((tf, key, ff, rr, ff == f))
        L.append(f"| {label} | " + " | ".join(cells) + " |")
    L += ["", "## Các biến thể đạt GIỮ hoặc THEO DÕI (mọi bộ lọc)", "",
          "Dấu ✓ ở cột cuối: đây là bộ lọc được chọn trong mẫu. Biến thể không có ✓ chỉ đẹp khi nhìn ngoài mẫu, dễ là may.", "",
          "| Khung | Cách | Lọc | TP/SL/giữ | PF trong mẫu | BTC | ETH | SOL | Hai nửa ngoài mẫu | Lệnh/ngày | Kết luận | Chọn trong mẫu |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    order = {"GIỮ": 0, "THEO DÕI": 1}
    for tf, key, f, r, chosen in sorted(keep, key=lambda x: (order[x[3]["verdict"]], -x[3]["oos_pf_mean"])):
        L.append(f"| {tf} | {r['label']} | {FILTER_LABEL[f]} | {r['best']} | {_fmt(r['is_pf'])} | " + " | ".join(_cell(r["oos"][s]) for s in SYMS)
                 + f" | {_fmt(r['oos_halves_pf'][0])} / {_fmt(r['oos_halves_pf'][1])} | {_fmt(r['per_day'], 1)} | {r['verdict']}: {r['why']} | {'✓' if chosen else ''} |")
    if not keep:
        L.append("| - | không có | | | | | | | | | | |")
    for tf in frames:
        L += ["", f"## Chi tiết khung {tf}", "",
              "| Cách | Lọc | Tín hiệu BTC/ETH/SOL | TP/SL/giữ | PF trong mẫu | BTC ngoài mẫu | ETH ngoài mẫu | SOL ngoài mẫu | Kết luận |", "|---|---|---|---|---|---|---|---|---|"]
        for key, by_f in out["frames"][tf].items():
            for f, r in by_f.items():
                if f == "_chosen":
                    continue
                sig = "/".join(str(r["signals"].get(s, 0)) for s in SYMS)
                if not r.get("best"):
                    L.append(f"| {r['label']} | {FILTER_LABEL[f]} | {sig} | không có | | | | | BỎ |"); continue
                L.append(f"| {r['label']} | {FILTER_LABEL[f]} | {sig} | {r['best']} | {_fmt(r['is_pf'])} | " + " | ".join(_cell(r["oos"][s]) for s in SYMS) + f" | {r['verdict']} |")
    with open(os.path.join(os.path.dirname(__file__), "scalp_mtf.md"), "w") as fh:
        fh.write("\n".join(L) + "\n")


if __name__ == "__main__":
    run(sys.argv[1].split(",") if len(sys.argv) > 1 else None)
