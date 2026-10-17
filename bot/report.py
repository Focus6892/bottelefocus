"""Soạn nội dung tin nhắn Telegram (HTML). Bố cục: mỗi dòng một ý, biểu tượng đầu dòng, số quan trọng in đậm."""
from datetime import datetime, timezone, timedelta

VN = timezone(timedelta(hours=7))
TV = "https://www.tradingview.com/chart/?symbol=BINANCE%3A{sym}.P"
TV_CAP = "https://www.tradingview.com/chart/?symbol=CRYPTOCAP%3A{sym}"
ICON = {"BTC": "🟠", "ETH": "🔷", "SOL": "🟣"}
SEP = "━━━━━━━━━━━━━━━━"


def _fmt_price(p):
    return f"{p:,.0f}" if p >= 1000 else f"{p:,.2f}"


def _arrow(x):
    return "▲" if x > 0 else "▼" if x < 0 else "•"


def _pct(x, d=1):
    return "-" if x is None else f"{x:+.{d}f}%"


def _now():
    return datetime.now(VN).strftime("%H:%M · %d/%m")


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
        return "📅 Ngày: chưa đủ dữ liệu"
    word = "🟢 TĂNG" if d["regime"] == "up" else "🔻 GIẢM"
    return f"📅 Ngày: <b>{word}</b> {d['bars_in_regime']} ngày (EMA20/50) · dừng lỗ <b>{_fmt_price(d['stop'])}</b>"


def _vp_lines(r):
    out = []
    for tf, name in (("vp_4h", "30 ngày"), ("vp_1d", "90 ngày")):
        v = r.get(tf) or {}
        p = v.get("profile")
        if not p:
            continue
        pos = {"above": "🟢 TRÊN vùng", "below": "🔻 DƯỚI vùng", "inside": "trong vùng"}[v["state"]]
        out.append(f"📦 VP {name}: {pos} {_fmt_price(p['val'])}–{_fmt_price(p['vah'])} · POC {_fmt_price(p['poc'])}")
    return out


def coin_block(r):
    name = r["name"]
    lines = [
        f"{ICON.get(name, '•')} <b>{name}  {_fmt_price(r['price'])}</b>   {_arrow(r['chg_4h'])} {_pct(r['chg_4h'])} 4h · {_pct(r['chg_24h'])} 24h",
        _daily_line(r),
        f"⏱ 4h: {_trend_word(r)} · ADX {r['adx']:.0f} · biến động <b>{r['score']}</b>/100 ({_score_word(r['score'])})"
        + (" · <b>đang nén</b>" if r.get("bbw_squeeze") else ""),
    ]
    lines += _vp_lines(r)
    lines.append(
        f"🧲 OI {_pct(r['oi_chg_4h'])} 4h / {_pct(r['oi_chg_24h'])} 24h · Funding {r['funding']*100:+.3f}% · L/S {r['ls_accounts']:.2f} · Taker {r['taker']:.2f}"
    )
    lines.append(f"📐 ATR {r['atr_pct']:.2f}% · RV24h {r['rv_24h']:.0f}%" + (f" · DVOL {r['dvol']:.0f}" if r.get("dvol") else ""))
    for code, level, text in r["signals"]:
        mark = "🔴" if level == "high" else "🟡" if level == "medium" else "⚪"
        lines.append(f"{mark} {text}")
    return "\n".join(lines)


def market_block(dom, ana):
    """Khối thị trường chung từ dominance. dom/ana có thể None."""
    if not dom or not ana:
        return "🌐 <b>Thị trường chung</b>\nChưa lấy được dữ liệu dominance."
    dirs = ana["dirs"]
    mark = {"up": "▲", "down": "▼", "flat": "•"}
    row = "  ·  ".join(f"{k} <b>{dom[k]['value']:.1f}%</b> {mark[dirs[k]]}" for k in ("BTC.D", "USDT.D", "OTHERS.D"))
    week = " · ".join(_pct(dom[k].get("chg_1w")) for k in ("BTC.D", "USDT.D", "OTHERS.D"))
    lines = ["🌐 <b>Thị trường chung</b> (khung ngày)", row, f"Tuần qua: {week}", f"→ {ana['text']}", f"💡 {ana['bias']}"]
    lines += [f"⚠️ {n}" for n in ana["notes"]]
    return "\n".join(lines)


def hourly_digest(results, dom=None, ana=None):
    parts = [f"📊 <b>BẢN TIN {_now()}</b> (giờ VN)", market_block(dom, ana)]
    for r in results:
        parts.append(SEP + "\n" + coin_block(r))
    links = " · ".join(f"<a href=\"{TV.format(sym=r['symbol'])}\">{r['name']}</a>" for r in results)
    links += " · " + " · ".join(f"<a href=\"{TV_CAP.format(sym=k)}\">{k}</a>" for k in ("BTC.D", "USDT.D", "OTHERS.D"))
    parts.append("📈 Biểu đồ: " + links)
    return "\n\n".join(parts)


def _alert(title, r, body_lines):
    return "\n".join([title, *body_lines, "", SEP, coin_block(r), "", f"📈 <a href=\"{TV.format(sym=r['symbol'])}\">Mở biểu đồ {r['name']}</a>"])


def trend_alert(r, previous):
    head = {
        "up": "🟢 <b>XU HƯỚNG TĂNG RÕ</b>",
        "down": "🔻 <b>XU HƯỚNG GIẢM RÕ</b>",
        "flat": "⚪ <b>Xu hướng kết thúc, về đi ngang</b>",
    }[r["trend"]]
    was = {"up": "tăng", "down": "giảm", "flat": "đi ngang"}[previous]
    return _alert(f"{head} · {r['name']} · {_now()}", r, [f"Trước đó: {was}"])


def daily_trend_alert(r, previous):
    d = r["daily"]
    up = d["regime"] == "up"
    head = "🟢 <b>EMA20 CẮT LÊN EMA50 · KHUNG NGÀY</b>" if up else "🔻 <b>EMA20 CẮT XUỐNG EMA50 · KHUNG NGÀY</b>"
    was = "tăng" if previous == "up" else "giảm"
    side = "LONG" if up else "SHORT"
    return _alert(
        f"{head}\n{ICON.get(r['name'], '•')} <b>{r['name']}</b> · {_now()}", r,
        [
            f"Xu hướng ngày đổi từ {was} sang {'tăng' if up else 'giảm'}.",
            f"🎯 Gợi ý <b>{side}</b> quanh <b>{_fmt_price(d['close'])}</b>",
            f"🛑 Dừng lỗ <b>{_fmt_price(d['stop'])}</b> (3,5 ATR ngày ≈ {d['atr']/d['close']*100*3.5:.1f}%)",
            "📚 Backtest 6 năm: tín hiệu swing ổn định nhất, profit factor 2,4–3,2, chỉ 4/10 lệnh thắng, lãi từ các đợt dài.",
        ],
    )


def vp_alert(r, tf, previous):
    v = r[tf]
    p = v["profile"]
    up = v["state"] == "above"
    name = "4h · vùng 30 ngày" if tf == "vp_4h" else "NGÀY · vùng 90 ngày"
    was = {"above": "trên vùng", "below": "dưới vùng", "inside": "trong vùng"}[previous]
    body = [
        f"Nến đóng <b>{_fmt_price(v['close'])}</b>, {'trên VAH' if up else 'dưới VAL'} {_fmt_price(p['vah'] if up else p['val'])} (trước đó {was}).",
        f"🎯 Gợi ý <b>{'LONG' if up else 'SHORT'}</b> theo hướng bung · 🛑 thoát khi nến đóng quay qua POC <b>{_fmt_price(p['poc'])}</b>",
    ]
    if tf == "vp_4h":
        body.append("📚 Backtest 3 năm trên 4h: cách duy nhất có lãi cả 3 đồng, PF 1,2–1,7, sụt giảm 34–38%.")
    else:
        rs, vr = v.get("rsi"), v.get("vol_ratio")
        detail = f"RSI14 {rs:.0f} · khối lượng {vr:.1f}x TB 20 ngày" if rs is not None and vr is not None else "thiếu RSI/khối lượng"
        if v.get("confirmed"):
            body.append(f"✅ <b>Có xác nhận RSI + khối lượng</b> ({detail})")
            body.append("📚 Backtest 6 năm: tổ hợp tốt nhất trên 1D, PF 2,0–3,9, 49–57% lệnh thắng ở BTC/ETH, sụt giảm 35–37%.")
        else:
            body.append(f"⚠️ <b>Chưa xác nhận</b> ({detail}; cần RSI > 55 hoặc < 45 và khối lượng ≥ 1,5x)")
            body.append("📚 VP thuần trên 1D: PF 1,7–2,9, 31–47% lệnh thắng.")
    head = f"{'🟢' if up else '🔻'} <b>THOÁT VÙNG GIÁ TRỊ {'LÊN' if up else 'XUỐNG'}</b> · khung {name}\n{ICON.get(r['name'], '•')} <b>{r['name']}</b> · {_now()}"
    return _alert(head, r, body)


def daily_squeeze_alert(r):
    d = r["daily"]
    up = d["squeeze_break"] > 0
    head = f"{'🟢' if up else '🔻'} <b>NÉN NGÀY RỒI BUNG {'LÊN' if up else 'XUỐNG'}</b>\n{ICON.get(r['name'], '•')} <b>{r['name']}</b> · {_now()}"
    return _alert(head, r, [
        "Bollinger ngày hẹp nhất 120 ngày và nến vừa đóng ngoài dải.",
        f"🎯 Giữ 4 tuần · 🛑 dừng lỗ <b>{_fmt_price(d['stop'])}</b>",
        "📚 Backtest: đúng hướng sau 4 tuần 62–75% ở ETH, SOL; hiếm (3 lần/năm).",
    ])


def inside_alert(r):
    ib = r["inside_4h"]
    up = ib["dir"] == 1
    head = f"{'🟢' if up else '🔻'} <b>INSIDE BAR 4h BUNG {'LÊN' if up else 'XUỐNG'}</b> · theo hướng EMA20/50\n{ICON.get(r['name'], '•')} <b>{r['name']}</b> · {_now()}"
    return _alert(head, r, [
        f"Nến 4h đóng <b>{_fmt_price(ib['close'])}</b>, {'trên đỉnh' if up else 'dưới đáy'} nến mẹ {_fmt_price(ib['mother_high'] if up else ib['mother_low'])}.",
        f"🎯 Gợi ý <b>{'LONG' if up else 'SHORT'}</b> · 🛑 thoát khi nến đóng {'dưới đáy' if up else 'trên đỉnh'} nến mẹ <b>{_fmt_price(ib['mother_low'] if up else ib['mother_high'])}</b> hoặc EMA20/50 4h đổi chiều",
        "📚 Backtest 3 năm trên 4h: PF 1,7 BTC · 1,7 ETH · 1,4 SOL, sụt giảm 27–47%, 3 lệnh/10 thắng, lãi từ các đợt chạy dài.",
    ])


def urgent_alert(r, sigs):
    body = "\n".join(f"🔴 {t}" for _, _, t in sigs)
    return (
        f"🚨 <b>CẢNH BÁO {r['name']}</b> · <b>{_fmt_price(r['price'])}</b> · {_now()}\n{body}\n\n"
        f"Điểm biến động <b>{r['score']}</b>/100 · 📈 <a href=\"{TV.format(sym=r['symbol'])}\">Mở biểu đồ</a>"
    )


def market_alert(dom, ana, previous_text):
    """Dòng tiền thị trường chung đổi trạng thái."""
    return "\n".join([
        f"🌐 <b>DÒNG TIỀN THỊ TRƯỜNG ĐỔI</b> · {_now()}",
        f"Trước đó: {previous_text}",
        "",
        market_block(dom, ana),
        "",
        "📈 " + " · ".join(f"<a href=\"{TV_CAP.format(sym=k)}\">{k}</a>" for k in ("BTC.D", "USDT.D", "OTHERS.D")),
    ])
