"""Nghiên cứu: volume profile có dự báo BIẾN ĐỘNG ngắn hạn không? Khung 1h, 4h, 1D.

Với mỗi nến i, profile tính trên `window` nến TRƯỚC nó. Đặc trưng (chỉ dùng dữ liệu tới nến i):
  - state: giá đóng trên VAH / trong vùng / dưới VAL
  - width: độ rộng vùng giá trị (VAH-VAL)/POC, xếp hạng phần trăm so với 250 profile trước (hẹp <= 25%, rộng >= 75%)
  - shape: vị trí POC trong vùng giá trị (POC thấp: dạng b, POC cao: dạng P, giữa: dạng D)
  - node: khối lượng tại bin giá đóng so với trung bình bin trong vùng giá trị (LVN < 0,5; HVN > 1,5)
  - dist: khoảng cách giá tới POC tính theo ATR14 (gần < 1 ATR, xa > 3 ATR)
Mục tiêu (nến i+1 .. i+H, mẫu KHÔNG chồng lấn: lấy mỗi H nến một mẫu):
  - mở rộng: biến động thực H nến tới / biến động thực `rv_bars` nến trước > 1
  - biên độ: (đỉnh - đáy) H nến tới / giá, %
  - tăng: giá đóng sau H nến cao hơn hiện tại
  - tiếp tục (chỉ khi ngoài vùng giá trị): giá đi tiếp xa POC
Đánh dấu ✓ khi tỷ lệ của nhóm lệch nền quá 2 sai số chuẩn (xấp xỉ, nhị thức).
"""
import json
import math
import os
from statistics import mean, pstdev

DATA = os.path.join(os.path.dirname(__file__), "data")
SYMS = ["BTC", "ETH", "SOL"]
FRAMES = {
    "1h": dict(file="1H", window=168, horizons={"24 giờ": 24, "3 ngày": 72}, rv_bars=24, label="1h (profile 7 ngày)"),
    "4h": dict(file="4H", window=180, horizons={"24 giờ": 6, "3 ngày": 18, "7 ngày": 42}, rv_bars=42, label="4h (profile 30 ngày)"),
    "1d": dict(file="1Dutc", window=90, horizons={"3 ngày": 3, "7 ngày": 7, "14 ngày": 14}, rv_bars=14, label="1D (profile 90 ngày)"),
}
RANK_WINDOW = 250


def atr14(k, n=14):
    tr = [k[0]["h"] - k[0]["l"]] + [max(k[i]["h"] - k[i]["l"], abs(k[i]["h"] - k[i - 1]["c"]), abs(k[i]["l"] - k[i - 1]["c"])) for i in range(1, len(k))]
    out, e = [], None
    for i, x in enumerate(tr):
        if i < n - 1:
            out.append(None); continue
        e = sum(tr[:n]) / n if i == n - 1 else (e * (n - 1) + x) / n
        out.append(e)
    return out


def profiles(k, window, bin_pct=0.002, value_area=0.70):
    """Như run.volume_profile nhưng trả thêm width, poc_pos, node (khối lượng bin giá đóng / TB bin trong VA)."""
    ref = sorted(x["c"] for x in k)[len(k) // 2]
    width = ref * bin_pct
    hist = {}

    def spread(bar, sign):
        lo, hi = int(bar["l"] // width), int(bar["h"] // width)
        v = bar["v"] / (hi - lo + 1) * sign
        for b in range(lo, hi + 1):
            hist[b] = hist.get(b, 0.0) + v
            if hist[b] <= 1e-9:
                hist.pop(b, None)

    out = []
    for i in range(len(k)):
        if i >= window and i - window - 1 >= 0:
            spread(k[i - window - 1], -1)
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
        va_bins = hi - lo + 1
        va_mean = acc / va_bins
        cb = int(k[i]["c"] // width)
        node = hist.get(cb, 0.0) / va_mean if va_mean else 0.0
        vah, val, pocp = (hi + 1) * width, lo * width, (poc + 0.5) * width
        out.append({"poc": pocp, "vah": vah, "val": val, "width": (vah - val) / pocp, "poc_pos": (pocp - val) / (vah - val) if vah > val else 0.5, "node": node})
    return out


def classify(c, p, a, width_bucket):
    """Đặc trưng profile tại một nến: c = giá đóng, p = profile (trước nến), a = ATR14, width_bucket = hẹp/vừa/rộng hoặc None."""
    return {
        "state": "trên VAH" if c > p["vah"] else "dưới VAL" if c < p["val"] else "trong vùng",
        "width": width_bucket,
        "shape": "POC thấp (b)" if p["poc_pos"] < 0.35 else "POC cao (P)" if p["poc_pos"] > 0.65 else "POC giữa (D)",
        "node": "LVN" if p["node"] < 0.5 else "HVN" if p["node"] > 1.5 else "bình thường",
        "dist": "gần POC (<1 ATR)" if abs(c - p["poc"]) < a else "xa POC (>3 ATR)" if abs(c - p["poc"]) > 3 * a else "vừa",
        "side": 1 if c > p["poc"] else -1,
    }


def width_bucket(w, q25, q75):
    return "hẹp" if w <= q25 else "rộng" if w >= q75 else "vừa"


def features(k, cfg):
    """Danh sách đặc trưng theo nến (None khi chưa đủ dữ liệu). Độ rộng xếp hạng so với 250 profile trước (chỉ quá khứ)."""
    prof = profiles(k, cfg["window"])
    a = atr14(k)
    widths = []
    out = []
    for i, bar in enumerate(k):
        p = prof[i]
        if p is None or a[i] is None:
            out.append(None); widths.append(None); continue
        hist_w = sorted(w for w in widths[-RANK_WINDOW:] if w is not None)
        wb = None
        if len(hist_w) >= 50:
            wb = width_bucket(p["width"], hist_w[len(hist_w) // 4], hist_w[(3 * len(hist_w)) // 4])
        widths.append(p["width"])
        out.append(classify(bar["c"], p, a[i], wb))
    return out


def width_quantiles(k, cfg):
    """Ngưỡng độ rộng vùng giá trị (q25, q75) trên toàn bộ lịch sử, cho bot phân loại trực tiếp."""
    ws = sorted(p["width"] for p in profiles(k, cfg["window"]) if p)
    if len(ws) < 50:
        return None
    return [ws[len(ws) // 4], ws[(3 * len(ws)) // 4]]


def targets(k, i, h, rv_bars):
    c = [x["c"] for x in k]
    if i + h >= len(c) or i - rv_bars < 1:
        return None
    back = [math.log(c[j] / c[j - 1]) for j in range(i - rv_bars + 1, i + 1)]
    fwd = [math.log(c[j] / c[j - 1]) for j in range(i + 1, i + h + 1)]
    rv_b, rv_f = pstdev(back), pstdev(fwd)
    if rv_b == 0:
        return None
    hi = max(x["h"] for x in k[i + 1 : i + h + 1]); lo = min(x["l"] for x in k[i + 1 : i + h + 1])
    return {"ratio": rv_f / rv_b, "expand": rv_f > rv_b, "range": (hi - lo) / c[i] * 100, "up": c[i + h] > c[i], "move": c[i + h] - c[i]}


def study(k, cfg):
    feats = features(k, cfg)
    res = {}
    for hname, h in cfg["horizons"].items():
        rows = []  # (feature dict, target)
        for i in range(0, len(k), h):  # mẫu không chồng lấn
            if feats[i] is None:
                continue
            t = targets(k, i, h, cfg["rv_bars"])
            if t:
                rows.append((feats[i], t))
        base = _agg(rows)
        groups = {}
        for key in ("state", "width", "shape", "node", "dist"):
            for val in sorted({f[key] for f, _ in rows if f[key] is not None}):
                sub = [(f, t) for f, t in rows if f[key] == val]
                g = _agg(sub)
                if key == "state" and val != "trong vùng":
                    cont = [((t["move"] > 0) == (f["side"] > 0)) for f, t in sub]
                    g["continue"] = mean(cont) if cont else None
                g["sig_expand"] = _sig(g, base, "p_expand")
                g["sig_up"] = _sig(g, base, "p_up")
                groups[f"{key}={val}"] = g
        res[hname] = {"base": base, "groups": groups}
    return res


def _agg(rows):
    if not rows:
        return {"n": 0}
    ts = [t for _, t in rows]
    return {
        "n": len(ts),
        "p_expand": mean(t["expand"] for t in ts),
        "ratio": mean(t["ratio"] for t in ts),
        "range": mean(t["range"] for t in ts),
        "p_up": mean(t["up"] for t in ts),
    }


def _sig(g, base, key):
    if g.get("n", 0) < 30 or base.get("n", 0) == 0:
        return False
    p = base[key]
    se = math.sqrt(p * (1 - p) / g["n"]) if 0 < p < 1 else 0
    return se > 0 and abs(g[key] - p) > 2 * se


def run():
    out = {}
    for tf, cfg in FRAMES.items():
        out[tf] = {}
        pooled = {}
        for sym in SYMS:
            path = os.path.join(DATA, f"{sym}_{cfg['file']}.json")
            if not os.path.exists(path):
                print(f"thiếu {path}", flush=True); continue
            k = json.load(open(path))
            out[tf][sym] = study(k, cfg)
            out[tf][sym]["bars"] = len(k)
            out[tf][sym]["width_q"] = width_quantiles(k, cfg)
            print(f"{tf} {sym}: {len(k)} nến", flush=True)
    with open(os.path.join(os.path.dirname(__file__), "vp_vol.json"), "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    write_md(out)
    return out


def f(x, d=0, suf=""):
    return "-" if x is None else f"{x:.{d}f}{suf}"


def write_md(out):
    L = ["# Volume profile và biến động ngắn hạn", "",
         "Mỗi dòng: nhóm nến theo đặc trưng profile; P(mở rộng) = xác suất biến động thực H nến tới cao hơn biến động vừa qua; "
         "tỷ lệ = biến động tới / vừa qua; biên độ = (đỉnh-đáy)/giá trong H nến; P(tăng) = xác suất giá cao hơn sau H nến; "
         "P(tiếp tục) = khi ngoài vùng giá trị, xác suất giá đi tiếp xa POC. ✓ = lệch nền quá 2 sai số chuẩn.", ""]
    for tf, cfg in FRAMES.items():
        L += [f"## Khung {cfg['label']}", ""]
        for sym in SYMS:
            d = out[tf].get(sym)
            if not d:
                continue
            L += [f"### {sym} · {d['bars']} nến", ""]
            for hname, r in d.items():
                if hname in ("bars", "width_q"):
                    continue
                b = r["base"]
                L += [f"**Sau {hname}** · nền: n={b['n']}, P(mở rộng) {f(b['p_expand']*100)}%, tỷ lệ {f(b['ratio'],2)}, biên độ {f(b['range'],1)}%, P(tăng) {f(b['p_up']*100)}%", "",
                      "| Nhóm | n | P(mở rộng) | Tỷ lệ | Biên độ | P(tăng) | P(tiếp tục) |", "|---|---|---|---|---|---|---|"]
                for name, g in r["groups"].items():
                    if g.get("n", 0) == 0:
                        continue
                    L.append(f"| {name} | {g['n']} | {f(g['p_expand']*100)}%{' ✓' if g['sig_expand'] else ''} | {f(g['ratio'],2)} | {f(g['range'],1)}% | {f(g['p_up']*100)}%{' ✓' if g['sig_up'] else ''} | {f(g.get('continue')*100 if g.get('continue') is not None else None)}{'%' if g.get('continue') is not None else ''} |")
                L.append("")
    with open(os.path.join(os.path.dirname(__file__), "vp_vol.md"), "w") as fh:
        fh.write("\n".join(L))


if __name__ == "__main__":
    run()
