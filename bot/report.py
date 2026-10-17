"""Soạn nội dung tin nhắn."""
from datetime import datetime, timezone, timedelta

VN = timezone(timedelta(hours=7))
TV = "https://www.tradingview.com/chart/?symbol=BINANCE%3A{sym}.P"


def _fmt_price(p):
    return f"{p:,.0f}" if p >= 1000 else f"{p:,.2f}"


def _arrow(x):
    return "▲" if x > 0 else "▼" if x < 0 else "•"


def _trend_word(r):
    if r["trend"] == "up":
        return "TĂNG mạnh" if r["trend_strong"] else "tăng"
    if r["trend"] == "down":
        return "GIẢM mạnh" if r["trend_strong"] else "giảm"
    return "đi ngang"


def _score_word(s):
    return "cao" if s >= 70 else "thấp" if s <= 30 else "bình thường"


def _daily_line(r):
    d = r.get("daily") or {}
    if not d.get("stop"):
        return "Xu hướng ngày: chưa đủ dữ liệu"
    word = "TĂNG" if d["regime"] == "up" else "GIẢM"
    return f"Xu hướng ngày: <b>{word}</b> (EMA20/50, {d['bars_in_regime']} ngày) · dừng lỗ gợi ý {_fmt_price(d['stop'])}"


def _vp_line(r):
    out = []
    for tf, name in (("vp_4h", "30 ngày"), ("vp_1d", "90 ngày")):
        v = r.get(tf) or {}
        p = v.get("profile")
        if not p:
            continue
        pos = {"above": "TRÊN vùng", "below": "DƯỚI vùng", "inside": "trong vùng"}[v["state"]]
        out.append(f"VP {name}: POC {_fmt_price(p['poc'])} · vùng {_fmt_price(p['val'])}–{_fmt_price(p['vah'])} · giá {pos}")
    return out


def coin_block(r):
    lines = [
        f"<b>{r['name']}</b> {_fmt_price(r['price'])}  {_arrow(r['chg_4h'])}{r['chg_4h']:+.1f}% 4h  {r['chg_24h']:+.1f}% 24h",
        _daily_line(r),
        f"Pha 4h: {_trend_word(r)} (ADX {r['adx']:.0f}) · Điểm biến động {r['score']} ({_score_word(r['score'])})",
        f"ATR {r['atr_pct']:.2f}% · RV24h {r['rv_24h']:.0f}%" + (f" · DVOL {r['dvol']:.0f}" if r.get("dvol") else "") + (" · <b>nén</b>" if r.get("bbw_squeeze") else ""),
        f"OI {r['oi_chg_4h']:+.1f}% 4h / {r['oi_chg_24h']:+.1f}% 24h · Funding {r['funding']*100:+.3f}% · L/S {r['ls_accounts']:.2f} (top {r['ls_top']:.2f}) · Taker {r['taker']:.2f}",
    ]
    lines += _vp_line(r)
    for code, level, text in r["signals"]:
        mark = "🔴" if level == "high" else "🟡" if level == "medium" else "⚪"
        lines.append(f"{mark} {text}")
    return "\n".join(lines)


def hourly_digest(results):
    now = datetime.now(VN).strftime("%H:%M %d/%m")
    parts = [f"📊 <b>Bản tin mỗi giờ · {now} (giờ VN)</b>"]
    for r in results:
        parts.append(coin_block(r))
    parts.append("Biểu đồ: " + " · ".join(f"<a href=\"{TV.format(sym=r['symbol'])}\">{r['name']}</a>" for r in results))
    return "\n\n".join(parts)


def trend_alert(r, previous):
    now = datetime.now(VN).strftime("%H:%M %d/%m")
    head = {
        "up": "🟢 <b>XU HƯỚNG TĂNG RÕ</b>",
        "down": "🔻 <b>XU HƯỚNG GIẢM RÕ</b>",
        "flat": "⚪ <b>Xu hướng kết thúc, về đi ngang</b>",
    }[r["trend"]]
    was = {"up": "tăng", "down": "giảm", "flat": "đi ngang"}[previous]
    return f"{head} · {r['name']} · {now}\nTrước đó: {was}\n\n{coin_block(r)}\n\n<a href=\"{TV.format(sym=r['symbol'])}\">Mở biểu đồ</a>"


def daily_trend_alert(r, previous):
    now = datetime.now(VN).strftime("%H:%M %d/%m")
    d = r["daily"]
    head = "🟢 <b>EMA20 CẮT LÊN EMA50 KHUNG NGÀY</b>" if d["regime"] == "up" else "🔻 <b>EMA20 CẮT XUỐNG EMA50 KHUNG NGÀY</b>"
    was = "tăng" if previous == "up" else "giảm"
    side = "long" if d["regime"] == "up" else "short"
    return (
        f"{head} · {r['name']} · {now}\nXu hướng ngày đổi từ {was}. Theo backtest 6 năm, đây là tín hiệu swing ổn định nhất "
        f"(profit factor 2,4–3,2) nhưng chỉ 4/10 lệnh thắng, lãi đến từ các đợt dài.\n"
        f"Gợi ý {side}: vào quanh {_fmt_price(d['close'])}, dừng lỗ {_fmt_price(d['stop'])} (3,5 ATR ngày = {d['atr']/d['close']*100*3.5:.1f}%).\n\n"
        f"{coin_block(r)}\n\n<a href=\"{TV.format(sym=r['symbol'])}\">Mở biểu đồ</a>"
    )


def vp_alert(r, tf, previous):
    now = datetime.now(VN).strftime("%H:%M %d/%m")
    v = r[tf]
    p = v["profile"]
    up = v["state"] == "above"
    name = "4h, vùng 30 ngày" if tf == "vp_4h" else "NGÀY, vùng 90 ngày"
    was = {"above": "trên vùng", "below": "dưới vùng", "inside": "trong vùng"}[previous]
    stat = ("Backtest 3 năm trên 4h: cách duy nhất có lãi cả 3 đồng, PF 1,2–1,7, sụt giảm 34–38%."
            if tf == "vp_4h" else "Backtest 6 năm trên 1D: PF 1,7–2,9, 24 tháng gần nhất tốt hơn cắt EMA.")
    return (
        f"{'🟢' if up else '🔻'} <b>THOÁT VÙNG GIÁ TRỊ {'LÊN' if up else 'XUỐNG'}</b> · {r['name']} · khung {name} · {now}\n"
        f"Nến đóng {_fmt_price(v['close'])}, {'trên VAH' if up else 'dưới VAL'} {_fmt_price(p['vah'] if up else p['val'])} (trước đó {was}). POC {_fmt_price(p['poc'])}.\n"
        f"{stat}\nGợi ý: theo hướng bung, thoát khi nến đóng quay qua POC {_fmt_price(p['poc'])}.\n\n"
        f"{coin_block(r)}\n\n<a href=\"{TV.format(sym=r['symbol'])}\">Mở biểu đồ</a>"
    )


def daily_squeeze_alert(r):
    now = datetime.now(VN).strftime("%H:%M %d/%m")
    d = r["daily"]
    up = d["squeeze_break"] > 0
    return (
        f"{'🟢' if up else '🔻'} <b>NÉN NGÀY RỒI BUNG {'LÊN' if up else 'XUỐNG'}</b> · {r['name']} · {now}\n"
        f"Bollinger ngày hẹp nhất 120 ngày và nến vừa đóng ngoài dải. Backtest: đúng hướng sau 4 tuần 62–75% ở ETH, SOL, hiếm (3 lần/năm).\n"
        f"Gợi ý giữ 4 tuần, dừng lỗ {_fmt_price(d['stop'])}.\n\n{coin_block(r)}\n\n<a href=\"{TV.format(sym=r['symbol'])}\">Mở biểu đồ</a>"
    )


def urgent_alert(r, sigs):
    now = datetime.now(VN).strftime("%H:%M %d/%m")
    body = "\n".join(f"🔴 {t}" for _, _, t in sigs)
    return f"🚨 <b>Cảnh báo {r['name']}</b> · {_fmt_price(r['price'])} · {now}\n{body}\n\nĐiểm biến động {r['score']} · <a href=\"{TV.format(sym=r['symbol'])}\">Mở biểu đồ</a>"
