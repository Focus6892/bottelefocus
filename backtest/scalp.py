"""Khung backtest SCALP riêng (15m, 1h): lệnh ngắn có chốt lời / dừng lỗ / giới hạn thời gian, phí maker-taker,
tối ưu tham số trong mẫu (70% đầu) và kiểm tra ngoài mẫu (30% cuối).

Khác với run.py (giữ lệnh tới khi tín hiệu đổi), ở đây mỗi lệnh:
  - vào ở giá MỞ nến sau tín hiệu (lệnh thị trường, phí taker 0,05%) hoặc lệnh chờ tại mức (phí maker 0,02%, chờ tối đa 4 nến, không khớp thì bỏ);
  - chốt lời = TP × ATR14, dừng lỗ = SL × ATR14 (hoặc mức giá riêng của chiến lược), tối đa HOLD nến rồi đóng ở giá đóng;
  - cùng nến chạm cả TP lẫn SL thì tính là SL (thận trọng); nến mở qua SL thì khớp ở giá mở; một lệnh một lúc.
Tham số tối ưu: TP ∈ {1; 1,5; 2; 3}, SL ∈ {0,5; 1; 1,5}, HOLD ∈ {8; 16; 48} nến.
"""
import json
import math
import os
from statistics import mean

try:
    from backtest.vp_vol import profiles
except ImportError:  # chạy trực tiếp
    from vp_vol import profiles

DATA = os.path.join(os.path.dirname(__file__), "data")
SYMS = ["BTC", "ETH", "SOL"]
TAKER, MAKER = 0.0005, 0.0002
TP_GRID, SL_GRID, HOLD_GRID = (1.0, 1.5, 2.0, 3.0), (0.5, 1.0, 1.5), (8, 16, 48)
DEFAULT = (1.5, 1.0, 16)
FRAMES = {
    "15m": dict(file="15m", ms=15 * 60_000, vp_window=96, bars_per_day=96, orb_bars=4, label="15m"),
    "1h": dict(file="1H", ms=3600_000, vp_window=168, bars_per_day=24, orb_bars=1, label="1h"),
}
HIGH = {"1d": ("1Dutc", 86_400_000), "4h": ("4H", 4 * 3600_000)}


# ---------- chuỗi ----------
def ema(v, n):
    k = 2 / (n + 1)
    out, e = [], None
    for x in v:
        e = x if e is None else x * k + e * (1 - k)
        out.append(e)
    return out


def atr14(k, n=14):
    tr = [k[0]["h"] - k[0]["l"]] + [max(k[i]["h"] - k[i]["l"], abs(k[i]["h"] - k[i - 1]["c"]), abs(k[i]["l"] - k[i - 1]["c"])) for i in range(1, len(k))]
    out, e = [], None
    for i, x in enumerate(tr):
        if i < n - 1:
            out.append(None); continue
        e = sum(tr[:n]) / n if i == n - 1 else (e * (n - 1) + x) / n
        out.append(e)
    return out


def rsi14(c, n=14):
    out = [None] * len(c)
    ag = al = None
    for i in range(1, len(c)):
        d = c[i] - c[i - 1]
        g, l = max(d, 0.0), max(-d, 0.0)
        if i <= n:
            ag = (ag or 0.0) + g / n; al = (al or 0.0) + l / n
            if i == n:
                out[i] = 100 - 100 / (1 + ag / al) if al else 100.0
            continue
        ag = (ag * (n - 1) + g) / n; al = (al * (n - 1) + l) / n
        out[i] = 100 - 100 / (1 + ag / al) if al else 100.0
    return out


def bbands(c, n=20, m=2.0):
    up, lo, w = [None] * len(c), [None] * len(c), [None] * len(c)
    s = s2 = 0.0
    for i, x in enumerate(c):
        s += x; s2 += x * x
        if i >= n:
            s -= c[i - n]; s2 -= c[i - n] ** 2
        if i >= n - 1:
            mu = s / n
            sd = math.sqrt(max(s2 / n - mu * mu, 0.0))
            up[i], lo[i], w[i] = mu + m * sd, mu - m * sd, 2 * m * sd / mu
    return up, lo, w


def align(k, kh, high_ms):
    """Chỉ số nến khung cao đã ĐÓNG trước khi nến k[i] mở."""
    out, j = [], -1
    for bar in k:
        while j + 1 < len(kh) and kh[j + 1]["t"] + high_ms <= bar["t"]:
            j += 1
        out.append(j)
    return out


def regime_from(k, kh, high_ms):
    """+1 khi EMA20 > EMA50 khung cao (đã đóng), -1 ngược lại, 0 khi chưa đủ."""
    idx = align(k, kh, high_ms)
    hc = [x["c"] for x in kh]
    e20, e50 = ema(hc, 20), ema(hc, 50)
    return [0 if j < 50 else (1 if e20[j] > e50[j] else -1) for j in idx]


def session_vwap(k):
    """VWAP và độ lệch chuẩn theo khối lượng, neo đầu ngày UTC; kèm số nến đã qua trong phiên."""
    vw, sd, nb = [None] * len(k), [None] * len(k), [0] * len(k)
    day, pv, vv, pv2, cnt = None, 0.0, 0.0, 0.0, 0
    for i, bar in enumerate(k):
        d = bar["t"] // 86_400_000
        if d != day:
            day, pv, vv, pv2, cnt = d, 0.0, 0.0, 0.0, 0
        tp = (bar["h"] + bar["l"] + bar["c"]) / 3
        pv += tp * bar["v"]; vv += bar["v"]; pv2 += tp * tp * bar["v"]; cnt += 1
        if vv > 0:
            v = pv / vv
            vw[i], sd[i], nb[i] = v, math.sqrt(max(pv2 / vv - v * v, 0.0)), cnt
    return vw, sd, nb


def vol_ratio(k, n=20):
    v = [x["v"] for x in k]
    out = [None] * len(v)
    s = 0.0
    for i, x in enumerate(v):
        if i >= 1:
            s += v[i - 1]
        if i > n:
            s -= v[i - n - 1]
        if i >= n and s > 0:
            out[i] = x / (s / n)
    return out


# ---------- tín hiệu: danh sách (i, hướng, giá chờ hoặc None, TP riêng hoặc None, SL riêng hoặc None) ----------
def sig_vp_rotation(k, ctx, use_regime):
    """Chạm VAL rồi đóng lại trong vùng (từ chối) -> long; chạm VAH rồi đóng lại -> short. TP/SL theo lưới."""
    prof, reg = ctx["prof"], ctx["reg1d"]
    out = []
    for i in range(1, len(k)):
        p = prof[i]
        if p is None or (use_regime and reg[i] == 0):
            continue
        b, pb = k[i], k[i - 1]
        if b["l"] <= p["val"] < b["c"] and pb["c"] > p["val"] and b["c"] < p["poc"] and (not use_regime or reg[i] == 1):
            out.append((i, 1, None, None, None))
        elif b["h"] >= p["vah"] > b["c"] and pb["c"] < p["vah"] and b["c"] > p["poc"] and (not use_regime or reg[i] == -1):
            out.append((i, -1, None, None, None))
    return out


def sig_vp_rotation_poc(k, ctx, use_regime):
    """Như trên nhưng chốt lời tại POC, dừng lỗ dưới đáy nến từ chối."""
    prof, reg = ctx["prof"], ctx["reg1d"]
    out = []
    for i in range(1, len(k)):
        p = prof[i]
        if p is None or (use_regime and reg[i] == 0):
            continue
        b, pb = k[i], k[i - 1]
        if b["l"] <= p["val"] < b["c"] and pb["c"] > p["val"] and b["c"] < p["poc"] and (not use_regime or reg[i] == 1):
            out.append((i, 1, None, p["poc"], b["l"]))
        elif b["h"] >= p["vah"] > b["c"] and pb["c"] < p["vah"] and b["c"] > p["poc"] and (not use_regime or reg[i] == -1):
            out.append((i, -1, None, p["poc"], b["h"]))
    return out


def sig_vp_limit(k, ctx, use_regime):
    """Giá trong vùng, cách VAL dưới 1 ATR -> đặt lệnh chờ mua tại VAL (phí maker); đối xứng tại VAH."""
    prof, reg, a = ctx["prof"], ctx["reg1d"], ctx["atr"]
    out, last = [], -10
    for i in range(1, len(k)):
        p = prof[i]
        if p is None or a[i] is None or i - last < 4:
            continue
        c = k[i]["c"]
        if p["val"] < c < p["val"] + a[i] and c < p["poc"] and (not use_regime or reg[i] == 1):
            out.append((i, 1, p["val"], None, None)); last = i
        elif p["vah"] - a[i] < c < p["vah"] and c > p["poc"] and (not use_regime or reg[i] == -1):
            out.append((i, -1, p["vah"], None, None)); last = i
    return out


def sig_pullback(k, ctx, use_regime):
    """Xu hướng 4h (và ngày nếu lọc) cùng chiều, giá trên EMA50, vừa hồi (RSI < 40 hoặc đóng dưới EMA20), nến đóng vượt đỉnh nến trước -> long."""
    c = [x["c"] for x in k]
    e20, e50, r = ctx["e20"], ctx["e50"], ctx["rsi"]
    reg4, reg1 = ctx["reg4h"], ctx["reg1d"]
    out = []
    for i in range(50, len(k)):
        if r[i - 1] is None:
            continue
        ok_l = reg4[i] == 1 and (not use_regime or reg1[i] == 1)
        ok_s = reg4[i] == -1 and (not use_regime or reg1[i] == -1)
        if ok_l and c[i] > e50[i] and (r[i - 1] < 40 or c[i - 1] < e20[i - 1]) and c[i] > k[i - 1]["h"] and c[i] > k[i]["o"]:
            out.append((i, 1, None, None, None))
        elif ok_s and c[i] < e50[i] and (r[i - 1] > 60 or c[i - 1] > e20[i - 1]) and c[i] < k[i - 1]["l"] and c[i] < k[i]["o"]:
            out.append((i, -1, None, None, None))
    return out


def sig_vwap_bounce(k, ctx, use_regime):
    """Đáy nến xuyên VWAP - 1 sd rồi đóng lại trên -> long (phiên đã qua >= 8 nến); đối xứng cho short."""
    vw, sd, nb, reg = ctx["vwap"], ctx["vsd"], ctx["vnb"], ctx["reg1d"]
    out = []
    for i in range(1, len(k)):
        if vw[i] is None or nb[i] < 8 or sd[i] == 0:
            continue
        b = k[i]
        lo_band, hi_band = vw[i] - sd[i], vw[i] + sd[i]
        if b["l"] < lo_band < b["c"] and b["c"] > b["o"] and (not use_regime or reg[i] == 1):
            out.append((i, 1, None, None, None))
        elif b["h"] > hi_band > b["c"] and b["c"] < b["o"] and (not use_regime or reg[i] == -1):
            out.append((i, -1, None, None, None))
    return out


def sig_squeeze(k, ctx, use_regime, lookback=48):
    """Bollinger hẹp nhất 48 nến (trong 5 nến gần) rồi đóng ngoài dải với khối lượng >= 1,5x -> theo hướng bung."""
    up, lo, w, vr, reg = ctx["bb_up"], ctx["bb_lo"], ctx["bbw"], ctx["vr"], ctx["reg1d"]
    c = [x["c"] for x in k]
    out = []
    for i in range(lookback + 5, len(k)):
        if w[i] is None or vr[i] is None:
            continue
        recent = [x for x in w[i - lookback : i] if x is not None]
        if not recent:
            continue
        squeezed = any(w[j] is not None and w[j] <= min(recent) * 1.05 for j in range(i - 5, i))
        if not squeezed or vr[i] < 1.5:
            continue
        if c[i] > up[i] and (not use_regime or reg[i] == 1):
            out.append((i, 1, None, None, None))
        elif c[i] < lo[i] and (not use_regime or reg[i] == -1):
            out.append((i, -1, None, None, None))
    return out


def sig_lvn_break(k, ctx, use_regime):
    """Từ trong vùng giá trị đóng ra ngoài tại vùng khối lượng thấp (node < 0,5) với khối lượng >= 1,2x -> đi tiếp."""
    prof, vr, reg = ctx["prof"], ctx["vr"], ctx["reg1d"]
    out = []
    for i in range(1, len(k)):
        p, pp = prof[i], prof[i - 1]
        if p is None or pp is None or vr[i] is None or vr[i] < 1.2 or p["node"] >= 0.5:
            continue
        c, pc = k[i]["c"], k[i - 1]["c"]
        if c > p["vah"] and pp["val"] <= pc <= pp["vah"] and (not use_regime or reg[i] == 1):
            out.append((i, 1, None, None, None))
        elif c < p["val"] and pp["val"] <= pc <= pp["vah"] and (not use_regime or reg[i] == -1):
            out.append((i, -1, None, None, None))
    return out


def sig_orb(k, ctx, use_regime):
    """Biên độ 60 phút đầu ngày UTC; lần đầu đóng trên đỉnh -> long, dưới đáy -> short (một lần mỗi ngày mỗi chiều)."""
    n, reg = ctx["orb_bars"], ctx["reg1d"]
    out = []
    day, start, rng, done = None, 0, None, set()
    for i, b in enumerate(k):
        d = b["t"] // 86_400_000
        if d != day:
            day, start, rng, done = d, i, None, set()
        if rng is None:
            if i - start + 1 >= n:
                w = k[start : start + n]
                rng = (min(x["l"] for x in w), max(x["h"] for x in w))
            continue
        if b["c"] > rng[1] and 1 not in done and (not use_regime or reg[i] == 1):
            out.append((i, 1, None, None, None)); done.add(1)
        elif b["c"] < rng[0] and -1 not in done and (not use_regime or reg[i] == -1):
            out.append((i, -1, None, None, None)); done.add(-1)
    return out


STRATS = {
    "vp_rotation": ("VP: từ chối tại VAL/VAH, TP/SL theo ATR", sig_vp_rotation, TAKER),
    "vp_rotation_poc": ("VP: từ chối tại VAL/VAH, chốt tại POC, dừng dưới nến", sig_vp_rotation_poc, TAKER),
    "vp_limit": ("VP: lệnh chờ tại VAL/VAH (phí maker)", sig_vp_limit, MAKER),
    "pullback": ("Hồi theo xu hướng 4h: RSI<40/EMA20 rồi vượt đỉnh nến trước", sig_pullback, TAKER),
    "vwap_bounce": ("VWAP phiên: xuyên -1 sd rồi đóng lại", sig_vwap_bounce, TAKER),
    "squeeze": ("Nén Bollinger 48 nến rồi bung + khối lượng 1,5x", sig_squeeze, TAKER),
    "lvn_break": ("VP: thoát vùng qua node khối lượng thấp + khối lượng 1,2x", sig_lvn_break, TAKER),
    "orb": ("Bung biên độ 60 phút đầu ngày", sig_orb, TAKER),
}


# ---------- mô phỏng ----------
def simulate(k, atr, signals, tp_m, sl_m, hold, fee_in, fee_out=TAKER, limit_wait=4):
    n = len(k)
    trades = []  # (nến tín hiệu, nến vào, nến ra, lợi nhuận)
    busy = -1
    for i, d, limit, tp_px, sl_px in signals:
        if i < busy or i + 1 >= n or not atr[i]:
            continue
        a = atr[i]
        if limit is None:
            j, px = i + 1, k[i + 1]["o"]
        else:
            j = None
            for m in range(i + 1, min(i + 1 + limit_wait, n)):
                if d == 1 and k[m]["l"] <= limit:
                    j, px = m, min(limit, k[m]["o"]); break
                if d == -1 and k[m]["h"] >= limit:
                    j, px = m, max(limit, k[m]["o"]); break
            if j is None:
                busy = min(i + 1 + limit_wait, n)
                continue
        tp = tp_px if tp_px is not None else px + d * tp_m * a
        sl = sl_px if sl_px is not None else px - d * sl_m * a
        if d == 1 and (tp <= px or sl >= px) or d == -1 and (tp >= px or sl <= px):
            busy = j + 1
            continue
        last = min(j + hold, n - 1)
        exit_px, m_exit = None, last
        for m in range(j, last + 1):
            b = k[m]
            if d == 1:
                if b["l"] <= sl:
                    exit_px, m_exit = (min(sl, b["o"]) if m > j else sl), m; break
                if b["h"] >= tp:
                    exit_px, m_exit = (max(tp, b["o"]) if m > j else tp), m; break
            else:
                if b["h"] >= sl:
                    exit_px, m_exit = (max(sl, b["o"]) if m > j else sl), m; break
                if b["l"] <= tp:
                    exit_px, m_exit = (min(tp, b["o"]) if m > j else tp), m; break
        if exit_px is None:
            exit_px = k[last]["c"]
        r = (exit_px / px - 1) * d - fee_in - fee_out
        trades.append((i, j, m_exit, r))
        busy = m_exit + 1
    return trades


def metrics(trades, bars, bars_per_day):
    if not trades:
        return {"n": 0}
    rets = [t[3] for t in trades]
    wins = [r for r in rets if r > 0]; losses = [-r for r in rets if r <= 0]
    eq, peak, mdd = 1.0, 1.0, 0.0
    for r in rets:
        eq *= 1 + r
        peak = max(peak, eq); mdd = max(mdd, 1 - eq / peak)
    return {
        "n": len(rets),
        "win_rate": len(wins) / len(rets),
        "avg_trade": mean(rets) * 100,
        "profit_factor": sum(wins) / sum(losses) if losses and sum(losses) > 0 else float("inf"),
        "total_return": (eq - 1) * 100,
        "max_drawdown": mdd * 100,
        "per_day": len(rets) / (bars / bars_per_day),
        "avg_hold": mean(t[2] - t[1] + 1 for t in trades),
    }


def context(k, cfg, kh):
    c = [x["c"] for x in k]
    up, lo, w = bbands(c)
    vw, sd, nb = session_vwap(k)
    return {
        "prof": profiles(k, cfg["vp_window"]), "atr": atr14(k), "e20": ema(c, 20), "e50": ema(c, 50), "rsi": rsi14(c),
        "bb_up": up, "bb_lo": lo, "bbw": w, "vwap": vw, "vsd": sd, "vnb": nb, "vr": vol_ratio(k), "orb_bars": cfg["orb_bars"],
        "reg1d": regime_from(k, kh["1d"], HIGH["1d"][1]), "reg4h": regime_from(k, kh["4h"], HIGH["4h"][1]),
    }


def evaluate(k, cfg, ctx, signals, fee_in, cut):
    """Tối ưu trong mẫu (tín hiệu trước `cut`), kiểm tra ngoài mẫu; trả về mọi tổ hợp trong mẫu để chọn tham số chung."""
    is_sig = [s for s in signals if s[0] < cut]; oos_sig = [s for s in signals if s[0] >= cut]
    bars_is, bars_oos = cut, len(k) - cut
    grid = {}
    for tp in TP_GRID:
        for sl in SL_GRID:
            for hold in HOLD_GRID:
                grid[(tp, sl, hold)] = metrics(simulate(k, ctx["atr"], is_sig, tp, sl, hold, fee_in), bars_is, cfg["bars_per_day"])
    ok = {p: m for p, m in grid.items() if m["n"] >= 40 and m["profit_factor"] > 1.1}
    best = max(ok, key=lambda p: ok[p]["profit_factor"]) if ok else None
    res = {
        "n_signals": len(signals),
        "default_oos": metrics(simulate(k, ctx["atr"], oos_sig, *DEFAULT, fee_in), bars_oos, cfg["bars_per_day"]),
        "grid_is": {f"{tp}/{sl}/{hold}": m for (tp, sl, hold), m in grid.items()},
    }
    if best:
        res["best"] = list(best)
        res["is"] = grid[best]
        res["oos"] = metrics(simulate(k, ctx["atr"], oos_sig, *best, fee_in), bars_oos, cfg["bars_per_day"])
    return res, oos_sig, bars_oos


def run(tf):
    cfg = FRAMES[tf]
    out = {"tf": tf}
    data, ctxs, sigs = {}, {}, {}
    for sym in SYMS:
        k = json.load(open(os.path.join(DATA, f"{sym}_{cfg['file']}.json")))
        kh = {name: json.load(open(os.path.join(DATA, f"{sym}_{HIGH[name][0]}.json"))) for name in HIGH}
        data[sym] = k
        ctxs[sym] = context(k, cfg, kh)
        cut = int(len(k) * 0.7)
        out[sym] = {"bars": len(k), "from": k[0]["t"], "to": k[-1]["t"], "cut": cut, "strats": {}}
        for key, (label, fn, fee_in) in STRATS.items():
            for use_regime in (False, True):
                name = key + ("+1d" if use_regime else "")
                signals = fn(k, ctxs[sym], use_regime)
                res, oos_sig, bars_oos = evaluate(k, cfg, ctxs[sym], signals, fee_in, cut)
                res["label"] = label + (" · lọc xu hướng ngày" if use_regime else "")
                res["fee_in"] = fee_in
                out[sym]["strats"][name] = res
                sigs[(sym, name)] = (oos_sig, bars_oos, fee_in)
        print(f"{tf} {sym}: {len(k)} nến, {len(STRATS) * 2} biến thể", flush=True)
    # tham số chung: tổ hợp có PF trung bình trong mẫu cao nhất ở cả 3 đồng (mỗi đồng n >= 30), rồi kiểm tra ngoài mẫu
    pooled = {}
    for key in STRATS:
        for use_regime in (False, True):
            name = key + ("+1d" if use_regime else "")
            combos = out[SYMS[0]]["strats"][name]["grid_is"].keys()
            best, best_pf = None, 0
            for combo in combos:
                ms = [out[s]["strats"][name]["grid_is"][combo] for s in SYMS]
                if all(m["n"] >= 30 for m in ms):
                    pf = mean(min(m["profit_factor"], 5.0) for m in ms)
                    if pf > best_pf:
                        best, best_pf = combo, pf
            if not best:
                pooled[name] = {"best": None}
                continue
            tp, sl, hold = (float(x) for x in best.split("/"))
            oos = {}
            for s in SYMS:
                oos_sig, bars_oos, fee_in = sigs[(s, name)]
                oos[s] = metrics(simulate(data[s], ctxs[s]["atr"], oos_sig, tp, sl, int(hold), fee_in), bars_oos, cfg["bars_per_day"])
            pooled[name] = {"best": best, "is_pf": best_pf, "oos": oos}
    out["pooled"] = pooled
    for sym in SYMS:  # bỏ lưới chi tiết khỏi json cho gọn
        for name in out[sym]["strats"]:
            out[sym]["strats"][name].pop("grid_is", None)
    with open(os.path.join(os.path.dirname(__file__), f"scalp_{tf}.json"), "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    write_md(out, cfg)
    return out


def f(x, d=1, suf=""):
    if x is None:
        return "-"
    if isinstance(x, float) and math.isinf(x):
        return "∞"
    return f"{x:.{d}f}{suf}"


def _row(m):
    if not m or m.get("n", 0) == 0:
        return "0 lệnh"
    return f"{m['n']} lệnh · thắng {f(m['win_rate']*100,0,'%')} · PF {f(m['profit_factor'],2)} · {f(m['avg_trade'],3,'%')}/lệnh · tổng {f(m['total_return'],0,'%')} · sụt {f(m['max_drawdown'],0,'%')} · {f(m['per_day'],1)}/ngày"


def write_md(out, cfg):
    import datetime as dt
    L = [f"# Scalp · khung {cfg['label']} · tối ưu trong mẫu 70% đầu, kiểm tra ngoài mẫu 30% cuối", "",
         "Cột: số lệnh | thắng | profit factor | lãi/lệnh | tổng lãi | sụt giảm | lệnh/ngày. Phí: taker 0,05% mỗi chiều; lệnh chờ 0,02% vào + 0,05% ra. "
         "'Mặc định' = TP 1,5 / SL 1 / giữ 16 nến không tối ưu. 'Tốt nhất trong mẫu' chọn theo PF với >= 40 lệnh; nếu không tổ hợp nào đạt PF > 1,1 thì bỏ trống.", ""]
    for sym in SYMS:
        d = out[sym]
        a, b = (dt.datetime.fromtimestamp(d[key] / 1000, dt.timezone.utc).strftime("%Y-%m-%d") for key in ("from", "to"))
        L += [f"## {sym} · {d['bars']} nến · {a} đến {b} · ngoài mẫu từ nến thứ {d['cut']}", "",
              "| Chiến lược | Tín hiệu | Tham số tốt nhất (TP/SL/giữ) | Trong mẫu | Ngoài mẫu (cùng tham số) | Ngoài mẫu, mặc định |",
              "|---|---|---|---|---|---|"]
        for name, r in d["strats"].items():
            best = f"{r['best'][0]}/{r['best'][1]}/{int(r['best'][2])}" if r.get("best") else "không có"
            L.append(f"| {r['label']} | {r['n_signals']} | {best} | {_row(r.get('is'))} | {_row(r.get('oos'))} | {_row(r['default_oos'])} |")
        L.append("")
    L += ["## Tham số chung cho cả 3 đồng (chọn trong mẫu theo PF trung bình, kiểm tra ngoài mẫu từng đồng)", "",
          "| Chiến lược | TP/SL/giữ | PF TB trong mẫu | BTC ngoài mẫu | ETH ngoài mẫu | SOL ngoài mẫu |", "|---|---|---|---|---|---|"]
    for name, p in out["pooled"].items():
        label = out[SYMS[0]]["strats"][name]["label"]
        if not p.get("best"):
            L.append(f"| {label} | không có | | | | |"); continue
        L.append(f"| {label} | {p['best']} | {f(p['is_pf'],2)} | " + " | ".join(_row(p["oos"][s]) for s in SYMS) + " |")
    L.append("")
    with open(os.path.join(os.path.dirname(__file__), f"scalp_{out['tf']}.md"), "w") as fh:
        fh.write("\n".join(L))


if __name__ == "__main__":
    import sys
    run(sys.argv[1] if len(sys.argv) > 1 else "15m")
