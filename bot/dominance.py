"""Tỷ trọng vốn hóa (dominance) BTC.D, USDT.D, OTHERS.D và đọc xu hướng thị trường chung.

Nguồn 1: TradingView scanner (công khai, không cần khóa) - đúng chỉ số CRYPTOCAP:BTC.D, USDT.D, OTHERS.D
         kèm EMA20/50, RSI14 khung ngày và % đổi ngày / tuần / tháng.
Nguồn 2 (dự phòng): CoinGecko /global - chỉ có giá trị hiện tại; OTHERS.D = 100 - tổng top 10.
Lịch sử tự tích lũy ở state/dominance.jsonl (mỗi ngày 1 dòng) để tính thay đổi khi nguồn 1 hỏng.
"""
import json
import os
from datetime import datetime, timezone

import requests

TV_URLS = ["https://scanner.tradingview.com/global/scan", "https://scanner.tradingview.com/crypto/scan", "https://scanner.tradingview.com/coin/scan"]
TV_SYMS = {"BTC.D": "CRYPTOCAP:BTC.D", "USDT.D": "CRYPTOCAP:USDT.D", "OTHERS.D": "CRYPTOCAP:OTHERS.D"}
TV_COLS = ["close", "change", "Perf.W", "Perf.1M", "EMA20", "EMA50", "RSI", "ADX", "Recommend.All"]
CG_URL = "https://api.coingecko.com/api/v3/global"
HISTORY = os.environ.get("DOMINANCE_HISTORY", "state/dominance.jsonl")
HEADERS = {"User-Agent": "Mozilla/5.0 (bottelefocus)", "Accept": "application/json"}


def _tv(cols=TV_COLS):
    body = {"symbols": {"tickers": list(TV_SYMS.values()), "query": {"types": []}}, "columns": cols}
    data = []
    for url in TV_URLS:
        r = requests.post(url, json=body, headers=HEADERS, timeout=20)
        if r.status_code == 200 and r.json().get("data"):
            data = r.json()["data"]
            break
    if len(data) < len(TV_SYMS):
        raise RuntimeError(f"scanner trả về {len(data)} dòng")
    out = {}
    for row in data:
        name = next(k for k, v in TV_SYMS.items() if v == row["s"])
        d = dict(zip(cols, row["d"]))
        out[name] = {
            "value": d["close"],
            "chg_1d": d.get("change"),          # % thay đổi so với nến ngày trước (tương đối)
            "chg_1w": d.get("Perf.W"),
            "chg_1m": d.get("Perf.1M"),
            "ema20": d.get("EMA20"),
            "ema50": d.get("EMA50"),
            "rsi": d.get("RSI"),
            "adx": d.get("ADX"),
            "rating": d.get("Recommend.All"),  # -1..1, đánh giá kỹ thuật tổng hợp của TradingView
        }
    return out


def _coingecko():
    r = requests.get(CG_URL, headers=HEADERS, timeout=20)
    r.raise_for_status()
    g = r.json()["data"]
    pct = g["market_cap_percentage"]
    others = 100 - sum(pct.values())
    base = lambda v: {"value": v, "chg_1d": None, "chg_1w": None, "chg_1m": None, "ema20": None, "ema50": None, "rsi": None, "adx": None, "rating": None}
    return {"BTC.D": base(pct.get("btc")), "USDT.D": base(pct.get("usdt")), "OTHERS.D": base(others)}


def _load_history():
    try:
        with open(HISTORY) as f:
            return [json.loads(x) for x in f if x.strip()]
    except FileNotFoundError:
        return []


def _append_history(dom):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    hist = _load_history()
    if hist and hist[-1]["date"] == today:
        return
    os.makedirs(os.path.dirname(HISTORY) or ".", exist_ok=True)
    with open(HISTORY, "a") as f:
        f.write(json.dumps({"date": today, **{k: v["value"] for k, v in dom.items()}}) + "\n")


def _fill_from_history(dom):
    """Khi thiếu % đổi từ nguồn 1: lấy từ lịch sử tự lưu (chênh lệch tương đối %)."""
    hist = _load_history()
    for name, d in dom.items():
        for key, n in (("chg_1d", 1), ("chg_1w", 7), ("chg_1m", 30)):
            if d.get(key) is None and len(hist) > n and hist[-1 - n].get(name):
                d[key] = (d["value"] / hist[-1 - n][name] - 1) * 100
        if d.get("ema20") is None and len(hist) >= 20:
            vals = [h[name] for h in hist[-50:] if h.get(name)]
            d["ema20"] = _ema(vals, 20)
            d["ema50"] = _ema(vals, 50) if len(vals) >= 50 else None


def _ema(v, n):
    k = 2 / (n + 1)
    e = v[0]
    for x in v[1:]:
        e = x * k + e * (1 - k)
    return e


def fetch():
    """Trả về {name: {...}} với source = 'tradingview' | 'coingecko', hoặc None nếu cả hai hỏng."""
    dom, source = None, None
    try:
        dom, source = _tv(), "tradingview"
    except Exception as e:
        print(f"[dominance] TradingView lỗi: {e}", flush=True)
        try:
            dom, source = _coingecko(), "coingecko"
        except Exception as e2:
            print(f"[dominance] CoinGecko lỗi: {e2}", flush=True)
            return None
    _append_history(dom)
    _fill_from_history(dom)
    dom["source"] = source
    return dom


def _dir(d):
    """Hướng khung ngày của một chỉ số: up / down / flat."""
    v, e20, e50, w = d.get("value"), d.get("ema20"), d.get("ema50"), d.get("chg_1w")
    if v is None:
        return "flat"
    if e20 is not None and e50 is not None:
        if v > e20 > e50:
            return "up"
        if v < e20 < e50:
            return "down"
        if v > e20 and (w or 0) > 0:
            return "up"
        if v < e20 and (w or 0) < 0:
            return "down"
        return "flat"
    if w is not None:  # chỉ có lịch sử tự lưu
        return "up" if w > 1 else "down" if w < -1 else "flat"
    return "flat"


def analyze(dom):
    """Đọc xu hướng thị trường chung từ 3 chỉ số dominance. Quy tắc chuẩn, chưa backtest."""
    if not dom or any(k not in dom for k in ("BTC.D", "USDT.D", "OTHERS.D")):
        return None
    b, u, o = (_dir(dom[k]) for k in ("BTC.D", "USDT.D", "OTHERS.D"))
    if u == "up" and b == "up":
        regime, text, bias = "risk_off_alt", "Tiền rút về stablecoin, altcoin bị bán mạnh hơn BTC", "Tránh long alt; nếu giữ lệnh thì BTC trụ tốt hơn ETH/SOL"
    elif u == "up":
        regime, text, bias = "risk_off", "Tiền rút về stablecoin, thị trường giảm hoặc chờ", "Ưu tiên đứng ngoài hoặc short theo tín hiệu khung ngày; long cần xác nhận mạnh"
    elif u == "down" and b == "down" and o == "up":
        regime, text, bias = "alt_season", "Tiền rời stablecoin và BTC, chảy vào altcoin", "Ưu tiên long ETH/SOL, hạn chế short"
    elif u == "down" and b == "down":
        regime, text, bias = "risk_on_large", "Tiền rời stablecoin, vào ETH và vốn hóa lớn, BTC mất tỷ trọng", "Ưu tiên long ETH; SOL theo sau nếu OTHERS.D bật lên"
    elif u == "down" and b == "up":
        regime, text, bias = "btc_season", "Tiền vào BTC là chính, altcoin tăng yếu hơn hoặc giảm so với BTC", "Ưu tiên long BTC; alt chỉ long khi có tín hiệu riêng"
    elif b == "down" and o == "up":
        regime, text, bias = "alt_rotation", "Dòng tiền xoay từ BTC sang altcoin, stablecoin đứng yên", "Cân nhắc long alt mạnh hơn BTC"
    elif b == "up":
        regime, text, bias = "btc_strength", "BTC mạnh hơn altcoin, stablecoin đứng yên", "Long BTC thuận hơn long alt"
    else:
        regime, text, bias = "neutral", "Dòng tiền chưa rõ, các chỉ số đi ngang", "Theo tín hiệu từng đồng, không thiên lệch"
    notes = []
    ru = dom["USDT.D"].get("rsi")
    if ru is not None and ru >= 70:
        notes.append("USDT.D quá mua (RSI ≥ 70): đợt bán tháo có thể sắp cạn, canh đảo chiều hồi")
    elif ru is not None and ru <= 30:
        notes.append("USDT.D quá bán (RSI ≤ 30): thị trường hưng phấn, cẩn trọng điều chỉnh")
    rb = dom["BTC.D"].get("rsi")
    if rb is not None and rb >= 70:
        notes.append("BTC.D quá mua: alt có thể bật hồi so với BTC")
    elif rb is not None and rb <= 30:
        notes.append("BTC.D quá bán: dòng tiền có thể quay lại BTC")
    return {"regime": regime, "text": text, "bias": bias, "dirs": {"BTC.D": b, "USDT.D": u, "OTHERS.D": o}, "notes": notes}


if __name__ == "__main__":
    d = fetch()
    print(json.dumps(d, indent=1, ensure_ascii=False))
    print(json.dumps(analyze(d), indent=1, ensure_ascii=False))
