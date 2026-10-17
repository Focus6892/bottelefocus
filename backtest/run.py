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

DATA = os.path.join(os.path.dirname(__file__), "data")
SYMS = ["BTC", "ETH", "SOL"]
FEE = 0.0005
HORIZONS = {"1d": 6, "3d": 18, "7d": 42}


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
    sm = wilder([x for x in dx if x is not None], n)
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
    """Với mỗi nến 4h, chỉ số nến 1D gần nhất ĐÃ ĐÓNG trước nó."""
    out, j = [], -1
    for bar in k4:
        while j + 1 < len(k1) and k1[j + 1]["t"] + 86_400_000 <= bar["t"] + 4 * 3600_000:
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


def strat_squeeze(k4, k1, lookback=180, hold=42):
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


STRATS = {
    "trend": ("Xu hướng EMA20/50 + ADX25 + xác nhận 1D (đang dùng)", strat_trend),
    "ema_cross": ("Cắt EMA20/50 trên 4h", strat_ema_cross),
    "donchian": ("Phá đỉnh/đáy 20 nến 4h", strat_donchian),
    "squeeze": ("Nén Bollinger rồi bung", strat_squeeze),
    "combo": ("Xu hướng + phá đỉnh/đáy cùng chiều", strat_combo),
}


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


def trade_sim(k4, sig, atr_stop=2.0):
    c = [x["c"] for x in k4]
    atr = atr_series(k4)
    pos, entry, stop, trades = 0, 0.0, 0.0, []
    eq, peak, mdd = 1.0, 1.0, 0.0
    for i in range(1, len(c)):
        if pos != 0:
            hit_stop = (pos == 1 and k4[i]["l"] <= stop) or (pos == -1 and k4[i]["h"] >= stop)
            flip = sig[i] != pos
            if hit_stop or flip:
                px = stop if hit_stop else c[i]
                r = (px / entry - 1) * pos - 2 * FEE
                trades.append(r)
                eq *= 1 + r
                peak = max(peak, eq)
                mdd = max(mdd, 1 - eq / peak)
                pos = 0
        if pos == 0 and sig[i] != 0 and atr[i]:
            pos, entry = sig[i], c[i]
            stop = entry - pos * atr_stop * atr[i]
    if pos != 0:  # đóng lệnh còn mở ở nến cuối
        r = (c[-1] / entry - 1) * pos - 2 * FEE
        trades.append(r)
        eq *= 1 + r
        peak = max(peak, eq)
        mdd = max(mdd, 1 - eq / peak)
    if not trades:
        return {"n": 0}
    wins = [t for t in trades if t > 0]; losses = [-t for t in trades if t <= 0]
    bh = c[-1] / c[0] - 1
    return {
        "n": len(trades),
        "win_rate": len(wins) / len(trades),
        "avg_trade": mean(trades) * 100,
        "profit_factor": (sum(wins) / sum(losses)) if losses and sum(losses) > 0 else float("inf"),
        "total_return": (eq - 1) * 100,
        "max_drawdown": mdd * 100,
        "buy_hold": bh * 100,
        "expectancy_ratio": (mean(wins) if wins else 0) / (mean(losses) if losses else 1e-9),
    }


def split(k4, k1, months=12):
    cut = k4[-1]["t"] - months * 30 * 86_400_000
    i4 = next(i for i, x in enumerate(k4) if x["t"] >= cut)
    return i4


def run():
    out = {}
    for sym in SYMS:
        k4 = json.load(open(os.path.join(DATA, f"{sym}_4H.json")))
        k1 = json.load(open(os.path.join(DATA, f"{sym}_1Dutc.json")))
        out[sym] = {"bars": len(k4), "from": k4[0]["t"], "to": k4[-1]["t"]}
        i_recent = split(k4, k1)
        for key, (label, fn) in STRATS.items():
            sig = fn(k4, k1)
            res = {"label": label, "direction": directional(k4, sig), "trades": trade_sim(k4, sig)}
            # 12 tháng gần nhất (tín hiệu tính trên toàn bộ, chỉ đo giao dịch trong đoạn gần)
            res["recent"] = trade_sim(k4[i_recent:], sig[i_recent:])
            out[sym][key] = res
    with open(os.path.join(os.path.dirname(__file__), "results.json"), "w") as f:
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
    L = ["# Kết quả backtest dự đoán xu hướng", ""]
    import datetime as dt
    for sym in SYMS:
        d = out[sym]
        a, b = (dt.datetime.utcfromtimestamp(d[k] / 1000).strftime("%Y-%m-%d") for k in ("from", "to"))
        L += [f"## {sym} · {d['bars']} nến 4h · {a} đến {b}", ""]
        L += ["| Chiến lược | Số tín hiệu | Đúng hướng 1 ngày | 3 ngày | 7 ngày | Nền 7 ngày | LN TB 7 ngày |", "|---|---|---|---|---|---|---|"]
        for key, (label, _) in STRATS.items():
            r = d[key]["direction"]
            L.append(f"| {label} | {r['7d']['n']} | {f(r['1d']['hit']*100 if r['1d']['hit'] is not None else None,0,'%')} | {f(r['3d']['hit']*100 if r['3d']['hit'] is not None else None,0,'%')} | {f(r['7d']['hit']*100 if r['7d']['hit'] is not None else None,0,'%')} | {f(r['7d']['base']*100,0,'%')} | {f(r['7d']['avg_ret'],2,'%')} |")
        L += ["", "| Chiến lược | Số lệnh | Thắng | LN/lệnh | Profit factor | Tổng LN 3 năm | Sụt giảm tối đa | Mua và giữ | Tổng LN 12 tháng |", "|---|---|---|---|---|---|---|---|---|"]
        for key, (label, _) in STRATS.items():
            t, rc = d[key]["trades"], d[key]["recent"]
            if t["n"] == 0:
                L.append(f"| {label} | 0 | | | | | | | |"); continue
            L.append(f"| {label} | {t['n']} | {f(t['win_rate']*100,0,'%')} | {f(t['avg_trade'],2,'%')} | {f(t['profit_factor'],2)} | {f(t['total_return'],0,'%')} | {f(t['max_drawdown'],0,'%')} | {f(t['buy_hold'],0,'%')} | {f(rc.get('total_return'),0,'%')} |")
        L.append("")
    with open(os.path.join(os.path.dirname(__file__), "results.md"), "w") as fh:
        fh.write("\n".join(L))


if __name__ == "__main__":
    run()
