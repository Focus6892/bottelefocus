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


def coin_block(r):
    lines = [
        f"<b>{r['name']}</b> {_fmt_price(r['price'])}  {_arrow(r['chg_4h'])}{r['chg_4h']:+.1f}% 4h  {r['chg_24h']:+.1f}% 24h",
        f"Xu hướng: {_trend_word(r)} (ADX {r['adx']:.0f}) · Điểm biến động {r['score']} ({_score_word(r['score'])})",
        f"ATR {r['atr_pct']:.2f}% · RV24h {r['rv_24h']:.0f}%" + (f" · DVOL {r['dvol']:.0f}" if r.get("dvol") else "") + (" · <b>nén</b>" if r.get("bbw_squeeze") else ""),
        f"OI {r['oi_chg_4h']:+.1f}% 4h / {r['oi_chg_24h']:+.1f}% 24h · Funding {r['funding']*100:+.3f}% · L/S {r['ls_accounts']:.2f} (top {r['ls_top']:.2f}) · Taker {r['taker']:.2f}",
    ]
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


def urgent_alert(r, sigs):
    now = datetime.now(VN).strftime("%H:%M %d/%m")
    body = "\n".join(f"🔴 {t}" for _, _, t in sigs)
    return f"🚨 <b>Cảnh báo {r['name']}</b> · {_fmt_price(r['price'])} · {now}\n{body}\n\nĐiểm biến động {r['score']} · <a href=\"{TV.format(sym=r['symbol'])}\">Mở biểu đồ</a>"
