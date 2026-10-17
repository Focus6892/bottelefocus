"""Chiến lược Smart Money Concepts (SMC) và price action cho backtest.

Mọi hàm nhận (k, n) với k = danh sách nến {t,o,h,l,c,v} khung chính, n = số nến hai bên để xác nhận đỉnh/đáy swing.
Trả về danh sách trạng thái -1/0/1 cùng độ dài k (1 = đang giữ long, -1 = short, 0 = đứng ngoài).
Không nhìn trước: đỉnh/đáy swing tại nến j chỉ được dùng từ nến j+n trở đi.
"""


def swings(k, n):
    """Với mỗi nến i: (đỉnh swing gần nhất đã xác nhận, đáy swing gần nhất đã xác nhận), mỗi cái là (chỉ số, giá) hoặc None.
    Đồng thời trả về danh sách đầy đủ đỉnh/đáy kèm nến xác nhận."""
    hi = [x["h"] for x in k]; lo = [x["l"] for x in k]
    highs, lows = [], []  # (j, giá, nến xác nhận = j+n)
    last_h, last_l = [None] * len(k), [None] * len(k)
    for i in range(len(k)):
        j = i - n
        if j >= n:
            if hi[j] >= max(hi[j - n : j]) and hi[j] > max(hi[j + 1 : j + n + 1]):
                highs.append((j, hi[j], i))
            if lo[j] <= min(lo[j - n : j]) and lo[j] < min(lo[j + 1 : j + n + 1]):
                lows.append((j, lo[j], i))
        last_h[i] = highs[-1][:2] if highs else None
        last_l[i] = lows[-1][:2] if lows else None
    return last_h, last_l, highs, lows


def _ema(v, n):
    k = 2 / (n + 1)
    out, e = [], None
    for x in v:
        e = x if e is None else x * k + e * (1 - k)
        out.append(e)
    return out


def structure(k, n):
    """Cấu trúc thị trường: +1 sau khi đóng nến vượt đỉnh swing gần nhất (BOS lên / CHoCH lên),
    -1 sau khi đóng nến thủng đáy swing gần nhất. Trả về (trạng thái, danh sách nến xảy ra phá vỡ kèm hướng)."""
    last_h, last_l, _, _ = swings(k, n)
    state, out, breaks = 0, [], []
    used_h = used_l = None
    for i, bar in enumerate(k):
        h, l = last_h[i], last_l[i]
        if h and h != used_h and bar["c"] > h[1]:
            if state != 1:
                breaks.append((i, 1))
            state, used_h = 1, h
        elif l and l != used_l and bar["c"] < l[1]:
            if state != -1:
                breaks.append((i, -1))
            state, used_l = -1, l
        out.append(state)
    return out, breaks


# ---------- SMC ----------
def strat_bos(k, n):
    """Cấu trúc thuần: giữ long khi cấu trúc tăng (BOS lên), short khi cấu trúc giảm; đổi khi CHoCH."""
    return structure(k, n)[0]


def _order_block(k, i_break, direction, lookback=20):
    """Order block: nến ngược chiều cuối cùng trước đợt đẩy gây phá vỡ cấu trúc. Trả về (thấp, cao) hoặc None."""
    for j in range(i_break - 1, max(i_break - lookback, 0), -1):
        bar = k[j]
        if direction == 1 and bar["c"] < bar["o"]:
            return bar["l"], bar["h"]
        if direction == -1 and bar["c"] > bar["o"]:
            return bar["l"], bar["h"]
    return None


def strat_ob(k, n):
    """Order block: sau BOS, chờ giá hồi về OB rồi đóng nến thoát ra cùng chiều -> vào. Hủy khi đóng nến xuyên qua OB.
    Thoát khi cấu trúc đổi chiều hoặc đóng nến qua phía kia của OB."""
    st, breaks = structure(k, n)
    bmap = dict(breaks)
    sig, pos, ob, ob_dir, armed = [], 0, None, 0, 0
    for i, bar in enumerate(k):
        c = bar["c"]
        if i in bmap:
            ob_dir = bmap[i]
            ob = _order_block(k, i, ob_dir)
            armed = i + 1  # chỉ được vào từ nến sau (phải có nhịp hồi thật)
            if pos != 0 and pos != ob_dir:
                pos = 0
        if pos == 1 and (st[i] == -1 or (ob and c < ob[0])):
            pos = 0
        elif pos == -1 and (st[i] == 1 or (ob and c > ob[1])):
            pos = 0
        if pos == 0 and ob and st[i] == ob_dir and i >= armed:
            lo, hi = ob
            if ob_dir == 1 and bar["l"] <= hi and c > hi:
                pos = 1
            elif ob_dir == -1 and bar["h"] >= lo and c < lo:
                pos = -1
            elif (ob_dir == 1 and c < lo) or (ob_dir == -1 and c > hi):
                ob = None  # OB bị xuyên qua: bỏ
        sig.append(pos)
    return sig


def strat_fvg(k, n):
    """Fair value gap: khoảng trống 3 nến (đáy nến i > đỉnh nến i-2) khi cấu trúc tăng. Vào khi giá hồi vào FVG và đóng lại trên FVG.
    Hủy FVG khi đóng nến dưới đáy FVG. Thoát khi cấu trúc đổi chiều."""
    st, _ = structure(k, n)
    sig, pos, gap, gap_dir, armed = [], 0, None, 0, 0
    for i, bar in enumerate(k):
        c = bar["c"]
        if st[i] == 1 and pos != 1 and i >= 2 and bar["l"] > k[i - 2]["h"] and c > bar["o"]:
            gap, gap_dir, armed = (k[i - 2]["h"], bar["l"]), 1, i + 1  # vào từ nến sau, khi giá hồi vào gap
        elif st[i] == -1 and pos != -1 and i >= 2 and bar["h"] < k[i - 2]["l"] and c < bar["o"]:
            gap, gap_dir, armed = (bar["h"], k[i - 2]["l"]), -1, i + 1
        if (pos == 1 and st[i] == -1) or (pos == -1 and st[i] == 1):
            pos = 0
        if pos == 0 and gap and st[i] == gap_dir and i >= armed:
            lo, hi = gap
            if gap_dir == 1 and bar["l"] <= hi and c > hi:
                pos = 1
            elif gap_dir == -1 and bar["h"] >= lo and c < lo:
                pos = -1
            elif (gap_dir == 1 and c < lo) or (gap_dir == -1 and c > hi):
                gap = None
        sig.append(pos)
    return sig


def strat_sweep(k, n):
    """Quét thanh khoản: râu nến xuyên đáy swing nhưng đóng lại trên đáy -> long đảo chiều (ngược lại cho short).
    Thoát khi đóng nến dưới đáy râu quét (sai) hoặc chạm đỉnh swing đối diện (mục tiêu)."""
    last_h, last_l, _, _ = swings(k, n)
    sig, pos, inval, target = [], 0, None, None
    for i, bar in enumerate(k):
        c = bar["c"]
        if pos == 1 and (c < inval or (target and bar["h"] >= target)):
            pos = 0
        elif pos == -1 and (c > inval or (target and bar["l"] <= target)):
            pos = 0
        if pos == 0:
            l, h = last_l[i], last_h[i]
            if l and bar["l"] < l[1] and c > l[1]:
                pos, inval, target = 1, bar["l"], h[1] if h else None
            elif h and bar["h"] > h[1] and c < h[1]:
                pos, inval, target = -1, bar["h"], l[1] if l else None
        sig.append(pos)
    return sig


def strat_sweep_bos(k, n, within=6):
    """Quét thanh khoản rồi trong `within` nến có nến đóng vượt đỉnh của nến quét (displacement) -> long.
    Thoát khi cấu trúc đổi chiều hoặc đóng dưới đáy quét."""
    last_h, last_l, _, _ = swings(k, n)
    st, _ = structure(k, n)
    sig, pos, pend, inval = [], 0, None, None
    for i, bar in enumerate(k):
        c = bar["c"]
        if pos == 1 and (c < inval or st[i] == -1):
            pos = 0
        elif pos == -1 and (c > inval or st[i] == 1):
            pos = 0
        l, h = last_l[i], last_h[i]
        if pos == 0:
            if pend and i - pend[0] <= within:
                d, lvl, ext = pend[1], pend[2], pend[3]
                if d == 1 and c > lvl:
                    pos, inval, pend = 1, ext, None
                elif d == -1 and c < lvl:
                    pos, inval, pend = -1, ext, None
            else:
                pend = None
            if pos == 0 and l and bar["l"] < l[1] and c > l[1]:
                pend = (i, 1, bar["h"], bar["l"])
            elif pos == 0 and h and bar["h"] > h[1] and c < h[1]:
                pend = (i, -1, bar["l"], bar["h"])
        sig.append(pos)
    return sig


# ---------- price action ----------
def _bull_engulf(a, b):
    return b["c"] > b["o"] and a["c"] < a["o"] and b["c"] >= a["o"] and b["o"] <= a["c"]


def _bear_engulf(a, b):
    return b["c"] < b["o"] and a["c"] > a["o"] and b["c"] <= a["o"] and b["o"] >= a["c"]


def _pin(bar):
    rng = bar["h"] - bar["l"]
    if rng <= 0:
        return 0
    body = abs(bar["c"] - bar["o"])
    lower = min(bar["o"], bar["c"]) - bar["l"]; upper = bar["h"] - max(bar["o"], bar["c"])
    if lower >= 2 * body and lower >= 0.6 * rng:
        return 1
    if upper >= 2 * body and upper >= 0.6 * rng:
        return -1
    return 0


def strat_engulf(k, n):
    """Nến nhấn chìm cùng chiều EMA50: nhấn chìm tăng khi giá trên EMA50 -> long; thoát khi đóng dưới EMA50 hoặc nhấn chìm ngược."""
    e50 = _ema([x["c"] for x in k], 50)
    sig, pos = [], 0
    for i, bar in enumerate(k):
        c = bar["c"]
        if i < 50:
            sig.append(0); continue
        if pos == 1 and (c < e50[i] or _bear_engulf(k[i - 1], bar)):
            pos = 0
        elif pos == -1 and (c > e50[i] or _bull_engulf(k[i - 1], bar)):
            pos = 0
        if pos == 0:
            if c > e50[i] and _bull_engulf(k[i - 1], bar):
                pos = 1
            elif c < e50[i] and _bear_engulf(k[i - 1], bar):
                pos = -1
        sig.append(pos)
    return sig


def strat_pin(k, n):
    """Pin bar tại đáy/đỉnh swing: râu dưới dài chạm hoặc xuyên đáy swing gần nhất -> long; thoát khi đóng dưới đáy pin bar
    hoặc chạm đỉnh swing (mục tiêu)."""
    last_h, last_l, _, _ = swings(k, n)
    sig, pos, inval, target = [], 0, None, None
    for i, bar in enumerate(k):
        c = bar["c"]
        if pos == 1 and (c < inval or (target and bar["h"] >= target)):
            pos = 0
        elif pos == -1 and (c > inval or (target and bar["l"] <= target)):
            pos = 0
        if pos == 0:
            p = _pin(bar)
            l, h = last_l[i], last_h[i]
            if p == 1 and l and bar["l"] <= l[1] * 1.003 and c > l[1]:
                pos, inval, target = 1, bar["l"], h[1] if h else None
            elif p == -1 and h and bar["h"] >= h[1] * 0.997 and c < h[1]:
                pos, inval, target = -1, bar["h"], l[1] if l else None
        sig.append(pos)
    return sig


def strat_break_retest(k, n, within=10):
    """Phá đỉnh swing rồi quay lại kiểm tra: sau khi đóng trên đỉnh, trong `within` nến có nến chạm lại mức đó và đóng trên -> long.
    Thoát khi đóng dưới mức phá hoặc cấu trúc đổi chiều."""
    st, breaks = structure(k, n)
    last_h, last_l, _, _ = swings(k, n)
    bmap = dict(breaks)
    sig, pos, lvl, lvl_dir, lvl_i = [], 0, None, 0, None
    for i, bar in enumerate(k):
        c = bar["c"]
        if i in bmap:
            lvl_dir, lvl_i = bmap[i], i
            lvl = (last_h[i][1] if lvl_dir == 1 else last_l[i][1]) if (last_h[i] and last_l[i]) else None
        if pos == 1 and (st[i] == -1 or (lvl and c < lvl)):
            pos = 0
        elif pos == -1 and (st[i] == 1 or (lvl and c > lvl)):
            pos = 0
        if pos == 0 and lvl and lvl_i is not None and 0 < i - lvl_i <= within:
            if lvl_dir == 1 and bar["l"] <= lvl and c > lvl:
                pos = 1
            elif lvl_dir == -1 and bar["h"] >= lvl and c < lvl:
                pos = -1
        sig.append(pos)
    return sig


def strat_inside(k, n):
    """Inside bar theo xu hướng EMA20/50: nến nằm trong nến mẹ, nến sau đóng ngoài nến mẹ cùng chiều EMA -> vào.
    Thoát khi đóng qua phía kia của nến mẹ hoặc EMA đổi chiều."""
    c = [x["c"] for x in k]
    e20, e50 = _ema(c, 20), _ema(c, 50)
    sig, pos, mother = [], 0, None
    for i, bar in enumerate(k):
        if i < 50:
            sig.append(0); continue
        trend = 1 if e20[i] > e50[i] else -1
        if pos == 1 and (trend == -1 or (mother and bar["c"] < mother[0])):
            pos = 0
        elif pos == -1 and (trend == 1 or (mother and bar["c"] > mother[1])):
            pos = 0
        if pos == 0 and i >= 2:
            m, ins = k[i - 2], k[i - 1]
            if ins["h"] <= m["h"] and ins["l"] >= m["l"]:
                if trend == 1 and bar["c"] > m["h"]:
                    pos, mother = 1, (m["l"], m["h"])
                elif trend == -1 and bar["c"] < m["l"]:
                    pos, mother = -1, (m["l"], m["h"])
        sig.append(pos)
    return sig


STRATS = {
    "smc_bos": ("SMC: cấu trúc BOS/CHoCH", strat_bos),
    "smc_ob": ("SMC: hồi về order block sau BOS", strat_ob),
    "smc_fvg": ("SMC: hồi về fair value gap", strat_fvg),
    "smc_sweep": ("SMC: quét thanh khoản đảo chiều", strat_sweep),
    "smc_sweep_bos": ("SMC: quét thanh khoản + displacement", strat_sweep_bos),
    "pa_engulf": ("PA: nến nhấn chìm theo EMA50", strat_engulf),
    "pa_pin": ("PA: pin bar tại đỉnh/đáy swing", strat_pin),
    "pa_break_retest": ("PA: phá đỉnh/đáy rồi retest", strat_break_retest),
    "pa_inside": ("PA: inside bar theo xu hướng EMA", strat_inside),
}
