"""Dự báo biến động ngắn hạn từ volume profile, dựa trên thống kê của backtest/vp_vol.json.

Với mỗi khung (1h: profile 7 ngày, 4h: 30 ngày, 1D: 90 ngày) tính đặc trưng profile hiện tại (vị trí giá so với vùng giá trị,
độ rộng vùng, dạng profile, node khối lượng, khoảng cách tới POC) rồi tra bảng thống kê: nhóm nào trong quá khứ có
xác suất mở rộng biến động / xác suất tăng lệch nền có ý nghĩa (✓) thì cộng vào điểm. Không có thống kê -> không dự báo.
"""
import json
import os

from backtest import vp_vol

STUDY_PATH = os.environ.get("VP_STUDY", "backtest/vp_vol.json")
FRAME_KEYS = {"1h": "1h", "4h": "4h", "1d": "1d"}
HORIZONS = {  # tên hiển thị -> [(khung, chân trời trong nghiên cứu)]
    "24 giờ tới": [("1h", "24 giờ"), ("4h", "24 giờ")],
    "7 ngày tới": [("4h", "7 ngày"), ("1d", "7 ngày")],
}
MIN_N = 30
_cache = {}


def load_study(path=STUDY_PATH):
    if path in _cache:
        return _cache[path]
    try:
        with open(path) as f:
            _cache[path] = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        _cache[path] = None
    return _cache[path]


def live_features(k, frame, sym, study):
    """Đặc trưng profile tại nến đóng gần nhất của khung `frame` (k: nến đã đóng)."""
    cfg = vp_vol.FRAMES[frame]
    if len(k) <= cfg["window"] + 1:
        return None
    prof = vp_vol.profiles(k[-(cfg["window"] + 2):], cfg["window"])
    p = prof[-1]
    a = vp_vol.atr14(k)[-1]
    if p is None or not a:
        return None
    wq = ((study or {}).get(frame, {}).get(sym, {}) or {}).get("width_q")
    wb = vp_vol.width_bucket(p["width"], wq[0], wq[1]) if wq else None
    f = vp_vol.classify(k[-1]["c"], p, a, wb)
    f["profile"] = p
    return f


def _lookup(study, frame, sym, horizon, feats):
    """Các nhóm có ý nghĩa cho đặc trưng hiện tại: [(mô tả, Δ P(mở rộng), Δ P(tăng), tỷ lệ biên độ, tiếp tục)]."""
    try:
        r = study[frame][sym][horizon]
    except (KeyError, TypeError):
        return None, []
    base = r["base"]
    hits = []
    for key in ("state", "width", "shape", "node", "dist"):
        val = feats.get(key)
        if val is None:
            continue
        g = r["groups"].get(f"{key}={val}")
        if not g or g.get("n", 0) < MIN_N:
            continue
        hits.append({
            "desc": val, "n": g["n"],
            "d_expand": g["p_expand"] - base["p_expand"], "sig_expand": g["sig_expand"],
            "d_up": g["p_up"] - base["p_up"], "sig_up": g["sig_up"],
            "range_ratio": g["range"] / base["range"] if base["range"] else 1.0,
            "cont": g.get("continue"),
        })
    return base, hits


def forecast(sym, frames, study):
    """frames: {'1h': feats, '4h': feats, '1d': feats}. Trả về {tên chân trời: {...}} hoặc None nếu thiếu thống kê."""
    if not study:
        return None
    out = {}
    for name, pairs in HORIZONS.items():
        d_exp, d_up, rr, reasons, bases = [], [], [], [], []
        for frame, horizon in pairs:
            feats = frames.get(frame)
            if not feats:
                continue
            base, hits = _lookup(study, frame, sym, horizon, feats)
            if base is None:
                continue
            bases.append(base)
            for h in hits:
                rr.append(h["range_ratio"])
                if h["sig_expand"]:
                    d_exp.append(h["d_expand"])
                    reasons.append(f"{h['desc']} ({vp_vol.FRAMES[frame]['label'].split(' ')[0]}: mở rộng {'+' if h['d_expand'] > 0 else ''}{h['d_expand']*100:.0f} điểm)")
                if h["sig_up"]:
                    d_up.append(h["d_up"])
                    reasons.append(f"{h['desc']} ({vp_vol.FRAMES[frame]['label'].split(' ')[0]}: tăng {'+' if h['d_up'] > 0 else ''}{h['d_up']*100:.0f} điểm)")
        if not bases:
            continue
        base_p = sum(b["p_expand"] for b in bases) / len(bases)
        base_range = sum(b["range"] for b in bases) / len(bases)
        ex = sum(d_exp) / len(d_exp) if d_exp else 0.0
        up = sum(d_up) / len(d_up) if d_up else 0.0
        level = "TĂNG" if ex >= 0.05 else "GIẢM" if ex <= -0.05 else "bình thường"
        lean = "nghiêng tăng" if up >= 0.05 else "nghiêng giảm" if up <= -0.05 else "không rõ hướng"
        out[name] = {
            "level": level, "p_expand": base_p + ex, "base_p": base_p,
            "range": base_range * (sum(rr) / len(rr) if rr else 1.0), "base_range": base_range,
            "lean": lean, "d_up": up, "reasons": reasons[:3], "evidence": len(d_exp) + len(d_up),
        }
    return out or None


def compute(sym, k4h, k1d, k1h):
    """Gom: đặc trưng 3 khung + dự báo. k*: nến đã đóng."""
    study = load_study()
    frames = {}
    if k1h:
        frames["1h"] = live_features(k1h, "1h", sym, study)
    frames["4h"] = live_features(k4h, "4h", sym, study)
    frames["1d"] = live_features(k1d, "1d", sym, study)
    fc = forecast(sym, frames, study)
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
