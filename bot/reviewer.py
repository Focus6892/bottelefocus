"""Agent review: kiểm tra lại khuyến nghị của agent đề xuất trước khi gửi.

Các bước soát:
1. Bằng chứng: đọc backtest/results*.json, nguồn nào có profit factor < 1,2 ở đồng này thì hạ trọng số về 0 và tính lại điểm.
2. Mâu thuẫn khung cao: khuyến nghị ngược xu hướng ngày -> bác (khung ngày là xương sống, backtest tốt nhất).
3. Dòng tiền: long alt khi tiền đang rút về stablecoin -> giữ lại.
4. Biến động cực đoan (điểm >= 85) hoặc ATR tăng vọt -> giữ lại, chờ ổn định.
5. Đám đông: long khi funding quá nóng, short khi funding quá âm -> cảnh báo.
6. Dừng lỗ: khoảng cách > 15% -> cảnh báo, gợi ý khối lượng = 1% vốn / khoảng dừng lỗ.
Kết luận: "ĐỒNG Ý" (gửi), "GIỮ LẠI" (gửi kèm cảnh báo, không mở lệnh mới), "BÁC" (đổi về đứng ngoài).
"""
import json
import os

from . import advisor, config as C

RESULTS = {"1d": "backtest/results_1d.json", "4h": "backtest/results.json"}
# nguồn -> (khung backtest, mã chiến lược trong results)
EVIDENCE = {"daily_regime": ("1d", "ema_cross"), "vp_1d": ("1d", "vp_rsi_vol"), "vp_4h": ("4h", "vp_breakout"), "inside_4h": ("4h", "pa_inside"),
            "ichimoku_1d": ("1d", "st_ichimoku"), "weinstein_1d": ("4h", "st_weinstein")}
MIN_PF = 1.2


def load_stats(root="."):
    out = {}
    for tf, path in RESULTS.items():
        try:
            with open(os.path.join(root, path)) as f:
                out[tf] = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
    return out


def evidence(name, stats):
    """{mã nguồn: profit factor ở đồng `name`} từ kết quả backtest, thiếu thì None."""
    ev = {}
    for src, (tf, key) in EVIDENCE.items():
        try:
            ev[src] = stats[tf][name][key]["trades"]["profit_factor"]
        except (KeyError, TypeError):
            ev[src] = None
    return ev


def review(rec, r, ana, stats=None):
    stats = stats if stats is not None else load_stats()
    ev = evidence(rec["name"], stats)
    notes, verdict = [], "ĐỒNG Ý"

    # 1. hạ trọng số nguồn yếu theo backtest rồi tính lại
    kept = []
    for code, d, w, desc in rec["sources"]:
        pf = ev.get(code)
        if pf is not None and pf < MIN_PF:
            notes.append(f"bỏ nguồn '{desc}': backtest {rec['name']} chỉ PF {pf:.2f}")
            continue
        kept.append((code, d, w, desc))
    adj = advisor.recommend(r, ana, kept)
    if adj["side"] != rec["side"]:
        notes.append(f"sau khi bỏ nguồn yếu, khuyến nghị đổi {rec['side']} -> {adj['side']}")
        verdict = "GIỮ LẠI"
    side = adj["side"]

    # 2. ngược khung ngày
    regime = (r.get("daily") or {}).get("regime")
    if side == "LONG" and regime == "down" or side == "SHORT" and regime == "up":
        notes.append("ngược xu hướng EMA20/50 ngày: chỉ được giao dịch cùng chiều khung ngày")
        verdict = "BÁC"

    # 3. dòng tiền
    if ana and side == "LONG" and ana["regime"] in ("risk_off", "risk_off_alt") and rec["name"] in ("ETH", "SOL"):
        notes.append("tiền đang rút về stablecoin, long alt rủi ro cao")
        verdict = "GIỮ LẠI" if verdict != "BÁC" else verdict
    if ana and side == "SHORT" and ana["regime"] == "alt_season" and rec["name"] in ("ETH", "SOL"):
        notes.append("mùa altcoin, short alt rủi ro cao")
        verdict = "GIỮ LẠI" if verdict != "BÁC" else verdict

    # 4. biến động cực đoan
    if side != "NGOÀI" and (r.get("score", 50) >= 85 or (r.get("atr_ratio") or 0) >= C.ATR_SPIKE_RATIO):
        notes.append(f"biến động cực đoan (điểm {r.get('score')}, ATR {r.get('atr_ratio') or 0:.1f}x): chờ nến 4h ổn định rồi vào")
        verdict = "GIỮ LẠI" if verdict != "BÁC" else verdict

    # 4b. dự báo biến động từ volume profile
    fc = ((r.get("vp_forecast") or {}).get("forecast") or {}).get("24 giờ tới")
    if fc and side != "NGOÀI":
        if fc["level"] == "TĂNG":
            notes.append(f"VP dự báo biến động 24h tăng (biên độ ~{fc['range']:.1f}%): giảm khối lượng hoặc nới dừng lỗ")
        elif fc["level"] == "GIẢM":
            notes.append(f"VP dự báo biến động 24h giảm (biên độ ~{fc['range']:.1f}%): chốt lời gần, tránh kỳ vọng chạy xa")

    # 5. đám đông
    f = r.get("funding")
    if f is not None and side == "LONG" and f >= C.FUNDING_HOT:
        notes.append(f"funding {f*100:+.3f}% quá nóng: long đang đông, dễ bị quét")
    if f is not None and side == "SHORT" and f <= C.FUNDING_COLD:
        notes.append(f"funding {f*100:+.3f}% quá âm: short đang đông, dễ bị squeeze")

    # 6. dừng lỗ và khối lượng
    if side != "NGOÀI" and adj.get("stop"):
        dist = abs(adj["price"] - adj["stop"]) / adj["price"] * 100
        if dist > 15:
            notes.append(f"dừng lỗ cách {dist:.1f}%: quá xa, cân nhắc chờ điểm vào tốt hơn")
        adj["risk_pct"] = dist
        adj["size_note"] = f"rủi ro 1% vốn -> khối lượng = 1% vốn / {dist:.1f}% = {100/dist:.1f}% vốn" if dist else ""

    if verdict == "BÁC":
        adj["side"], adj["stop"] = "NGOÀI", None
    if not notes:
        notes.append("các nguồn đồng thuận, không mâu thuẫn khung ngày, dòng tiền hay biến động")
    return {"verdict": verdict, "notes": notes, "final": adj, "evidence": ev}
