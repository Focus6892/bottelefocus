"""Nguồn dự phòng: OKX (công khai, không chặn máy chạy GitHub Actions ở Mỹ như Binance)."""
import time
import requests

BASE = "https://www.okx.com"
_session = requests.Session()
_session.headers["User-Agent"] = "bottelefocus/1.0"
BAR = {"4h": "4H", "1d": "1Dutc", "1h": "1H"}


def _get(path, **params):
    last = None
    for attempt in range(3):
        try:
            r = _session.get(BASE + path, params=params, timeout=20)
            r.raise_for_status()
            j = r.json()
            if j.get("code") not in ("0", 0):
                raise RuntimeError(j.get("msg", "lỗi OKX"))
            return j["data"]
        except (requests.RequestException, RuntimeError) as e:
            last = e
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"OKX {path} lỗi: {last}")


def _inst(symbol):  # BTCUSDT -> BTC-USDT-SWAP
    return symbol[:-4] + "-USDT-SWAP"


def _ccy(symbol):
    return symbol[:-4]


def klines(symbol, interval, limit=200):
    raw = _get("/api/v5/market/candles", instId=_inst(symbol), bar=BAR[interval], limit=min(limit, 300))
    out = [{"t": int(k[0]), "o": float(k[1]), "h": float(k[2]), "l": float(k[3]), "c": float(k[4]), "v": float(k[5])} for k in raw]
    return sorted(out, key=lambda x: x["t"])  # OKX trả mới nhất trước


def premium_index(symbol):
    d = _get("/api/v5/public/funding-rate", instId=_inst(symbol))[0]
    return {"mark": 0.0, "funding": float(d["fundingRate"])}


def open_interest_hist(symbol, period="1H", limit=30):
    raw = _get("/api/v5/rubik/stat/contracts/open-interest-volume", ccy=_ccy(symbol), period=period)
    rows = sorted(([int(x[0]), float(x[1])] for x in raw), key=lambda x: x[0])[-limit:]
    return [{"t": t, "oi": oi, "oi_usd": oi} for t, oi in rows]


def long_short_accounts(symbol):
    raw = _get("/api/v5/rubik/stat/contracts/long-short-account-ratio", ccy=_ccy(symbol), period="1H")
    return float(max(raw, key=lambda x: int(x[0]))[1]) if raw else None


def long_short_top_positions(symbol):
    try:
        raw = _get("/api/v5/rubik/stat/contracts/long-short-account-ratio-contract-top-trader", instId=_inst(symbol), period="1H")
        return float(max(raw, key=lambda x: int(x[0]))[1]) if raw else None
    except Exception:
        return None


def taker_ratio(symbol):
    raw = _get("/api/v5/rubik/stat/taker-volume", ccy=_ccy(symbol), instType="CONTRACTS", period="1H")
    if not raw:
        return None
    ts, sell, buy = max(raw, key=lambda x: int(x[0]))
    return float(buy) / float(sell) if float(sell) else None


def fetch_all(symbol, main_tf, higher_tf, limit):
    return {
        "k_main": klines(symbol, main_tf, limit),
        "k_high": klines(symbol, higher_tf, 200),
        "premium": premium_index(symbol),
        "oi": open_interest_hist(symbol),
        "ls_accounts": long_short_accounts(symbol),
        "ls_top": long_short_top_positions(symbol),
        "taker": taker_ratio(symbol),
    }
