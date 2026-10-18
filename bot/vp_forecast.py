"""Dự báo biến động ngắn hạn từ volume profile, dựa trên thống kê của backtest/vp_vol.json (3 năm, gộp 3 đồng).

Với mỗi khung (1h: profile 7 ngày, 4h: 30 ngày, 1D: 90 ngày) tính đặc trưng profile hiện tại (vị trí giá so với vùng giá trị,
độ rộng vùng, dạng profile, node khối lượng, khoảng cách tới POC) rồi tra bảng thống kê GỘP 3 đồng: nhóm nào có xác suất
mở rộng biến động / xác suất tăng lệch nền với |z| >= 2 (n >= 200) thì tính là bằng chứng. Không có thống kê -> không dự báo.
"""
import json
import math
import os

from backtest import vp_vol

STUDY_PATH = os.environ.get("VP_STUDY", "backtest/vp_vol.json")
SYMS = ("BTC", "ETH", "SOL")
HORIZONS = {  # tên hiển thị -> [(khung, chân trời trong nghiên cứu)]
    "24 giờ tới": [("1h", "24 giờ"), ("4h", "24 giờ")],
    "7 ngày tới": [("4h", "7 ngày"), ("1d", "7 ngày")],
}
MIN_N, Z_MIN = 200, 2.0
_cache = {}


def pool(study):
    """Gộp 3 đồng: {khung: {chân trời: {"base": {...}, "groups": {tên: {n, p_expand, p_up, range_ratio, cont, z_expand, z_up, z_cont}}}}}"""
    out = {}
    for tf, per_sym in study.items():
        out[tf] = {}
        horizons = [h for h in per_sym.get(SYMS[0], {}) if h not in ("bars", "width_q")]
        for h in horizons:
            bases = [per_sym[s][h]["base"] for s in SYMS if s in per_sym and h in per_sym[s]]
            nb = sum(b["n"] for b in bases)
            if nb == 0:
                continue
            pe = sum(b["p_expand"] * b["n"] for b in bases) / nb
            pu = sum(b["p_up"] * b["n"] for b in bases) / nb
            rg = sum(b["range"] * b["n"] for b in bases) / nb
            groups = {}
            for name in per_sym[SYMS[0]][h]["groups"]:
                rows = [(per_sym[s][h]["groups"].get(name), per_sym[s][h]["base"]) for s in SYMS if s in per_sym and h in per_sym[s]]
                rows = [(g, b) for g, b in rows if g and g.get("n", 0) > 0]
                n = sum(g["n"] for g, _ in rows)
                if n < MIN_N:
                    continue
                ge = sum(g["p_expand"] * g["n"] for g, _ in rows) / n
                gu = sum(g["p_up"] * g["n"] for g, _ in rows) / n
                rr = sum(g["range"] / b["range"] * g["n"] for g, b in rows if b["range"]) / n
                conts = [(g["continue"], g["n"]) for g, _ in rows if g.get("continue") is not None]
                gc = sum(c * k for c, k in conts) / sum(k for _, k in conts) if conts else None
                groups[name] = {
                    "n": n, "p_expand": ge, "p_up": gu, "range_ratio": rr, "cont": gc,
                    "z_expand": (ge - pe) / math.sqrt(pe * (1 - pe) / n) if 0 < pe < 1 else 0.0,
                    "z_up": (gu - pu) / math.sqrt(pu * (1 - pu) / n) if 0 < pu < 1 else 0.0,
                    "z_cont": (gc - 0.5) / math.sqrt(0.25 / n) if gc is not None else None,
                }
            out[tf][h] = {"base": {"n": nb, "p_expand": pe, "p_up": pu, "range": rg}, "groups": groups}
    return out


def load_study(path=None):
    """Trả về (thống kê theo đồng, thống kê gộp) hoặc (None, None)."""
    path = path or STUDY_PATH
    if path in _cache:
        return _cache[path]
    try:
        with open(path) as f:
            raw = json.load(f)
        _cache[path] = (raw, pool(raw))
    except (FileNotFoundError, json.JSONDecodeError, KeyError, TypeError):
        _cache[path] = (None, None)
    return _cache[path]


def live_features(k, frame, sym, raw):
    """Đặc trưng profile tại nến đóng gần nhất của khung `frame` (k: nến đã đóng)."""
    cfg = vp_vol.FRAMES[frame]
    if len(k) <= cfg["window"] + 1:
        return None
    prof = vp_vol.profiles(k[-(cfg["window"] + 2):], cfg["window"])
    p = prof[-1]
    a = vp_vol.atr14(k)[-1]
    if p is None or not a:
        return None
    wq = (((raw or {}).get(frame) or {}).get(sym) or {}).get("width_q")
    wb = vp_vol.width_bucket(p["width"], wq[0], wq[1]) if wq else None
    f = vp_vol.classify(k[-1]["c"], p, a, wb)
    f["profile"] = p
    return f


def _label(key, val):
    """Tên nhóm đọc được một mình trong bản tin (giá trị gốc trong nghiên cứu ngắn gọn hơn)."""
    if key == "state":
        return "giá trong vùng giá trị" if val == "trong vùng" else f"giá {val}"
    if key == "width":
        return f"vùng giá trị {val}"
    if key == "node":
        return "node khối lượng bình thường" if val == "bình thường" else f"giá ở {val}"
    if key == "dist":
        return "cách POC vừa" if val == "vừa" else val
    return val


def evidence(pooled, frame, horizon, feats):
    """Các nhóm khớp đặc trưng hiện tại có |z| >= Z_MIN: [(mô tả, Δ mở rộng, Δ tăng, tỷ lệ biên độ, cont, cờ)]."""
    try:
        r = pooled[frame][horizon]
    except (KeyError, TypeError):
        return None, []
    base, hits = r["base"], []
    for key in ("state", "width", "shape", "node", "dist"):
        val = feats.get(key)
        if val is None:
            continue
        g = r["groups"].get(f"{key}={val}")
        if not g:
            continue
        sig_e, sig_u = abs(g["z_expand"]) >= Z_MIN, abs(g["z_up"]) >= Z_MIN
        sig_c = g["z_cont"] is not None and abs(g["z_cont"]) >= Z_MIN
        if sig_e or sig_u or sig_c:
            hits.append({"desc": _label(key, val), "n": g["n"], "d_expand": g["p_expand"] - base["p_expand"], "d_up": g["p_up"] - base["p_up"],
                         "range_ratio": g["range_ratio"], "cont": g["cont"], "sig_e": sig_e, "sig_u": sig_u, "sig_c": sig_c, "side": feats.get("side", 0)})
    return base, hits


def forecast(frames, pooled):
    """frames: {'1h': feats, '4h': feats, '1d': feats}. Trả về {tên chân trời: {...}} hoặc None nếu thiếu thống kê."""
    if not pooled:
        return None
    out = {}
    for name, pairs in HORIZONS.items():
        d_exp, d_up, rr, reasons, bases = [], [], [], {}, []
        for frame, horizon in pairs:
            feats = frames.get(frame)
            if not feats:
                continue
            base, hits = evidence(pooled, frame, horizon, feats)
            if base is None:
                continue
            bases.append(base)
            tag = vp_vol.FRAMES[frame]["label"].split(" ")[0]
            for h in hits:
                rr.append(h["range_ratio"])
                why = reasons.setdefault(f"{h['desc']} ({tag})", [])  # gộp các tác dụng của cùng một nhóm vào một vế
                if h["sig_e"]:
                    d_exp.append(h["d_expand"])
                    why.append(f"mở rộng {h['d_expand']*100:+.0f} điểm, biên độ ×{h['range_ratio']:.2f}")
                if h["sig_u"]:
                    d_up.append(h["d_up"])
                    why.append(f"xác suất tăng {h['d_up']*100:+.0f} điểm")
                if h["sig_c"] and h["cont"] is not None and h["side"]:
                    # tiếp tục < 50% nghĩa là hay quay lại POC: thiên hướng ngược với phía đang đứng
                    lean = (1 if h["cont"] > 0.5 else -1) * h["side"]
                    d_up.append(lean * abs(h["cont"] - 0.5))
                    why.append(f"{'đi tiếp' if h['cont'] > 0.5 else 'quay về POC'} {max(h['cont'], 1 - h['cont'])*100:.0f}% số lần")
        if not bases:
            continue
        reasons = [f"{k}: {', '.join(v)}" for k, v in reasons.items() if v]
        base_p = sum(b["p_expand"] for b in bases) / len(bases)
        base_range = sum(b["range"] for b in bases) / len(bases)
        ex = sum(d_exp) / len(d_exp) if d_exp else 0.0
        up = sum(d_up) / len(d_up) if d_up else 0.0
        level = "TĂNG" if ex >= 0.03 else "GIẢM" if ex <= -0.03 else "bình thường"
        lean = "nghiêng tăng" if up >= 0.03 else "nghiêng giảm" if up <= -0.03 else "không rõ hướng"
        out[name] = {
            "level": level, "p_expand": base_p + ex, "base_p": base_p,
            "range": base_range * (sum(rr) / len(rr) if rr else 1.0), "base_range": base_range,
            "lean": lean, "d_up": up, "reasons": reasons[:3], "evidence": len(reasons),
        }
    return out or None


def compute(sym, k4h, k1d, k1h):
    """Gom: đặc trưng 3 khung + dự báo. k*: nến đã đóng."""
    raw, pooled = load_study()
    frames = {}
    if k1h:
        frames["1h"] = live_features(k1h, "1h", sym, raw)
    frames["4h"] = live_features(k4h, "4h", sym, raw)
    frames["1d"] = live_features(k1d, "1d", sym, raw)
    fc = forecast(frames, pooled)
    return {"features": {k: ({kk: vv for kk, vv in v.items() if kk != "profile"} if v else None) for k, v in frames.items()}, "forecast": fc}


def lines(vf):
    """Dòng hiển thị trong bản tin."""
    if not vf or not vf.get("forecast"):
        return []
    out = []
    for name, f in vf["forecast"].items():
        mark = {"TĂNG": "🔺", "GIẢM": "🔹", "bình thường": "▫️"}[f["level"]]
        txt = f"🔮 {name}: biến động <b>{f['level']}</b> {mark} ({f['p_expand']*100:.0f}% so với nền {f['base_p']*100:.0f}%) · biên độ ~{f['range']:.1f}% · {f['lean']}"
        if f["reasons"]:
            txt += " · vì " + "; ".join(f["reasons"])
        out.append(txt)
    return out
