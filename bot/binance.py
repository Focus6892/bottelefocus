"""Lấy dữ liệu công khai từ Binance USDT-M Futures (không cần khóa API)."""
import time
import requests

BASE = "https://fapi.binance.com"
_session = requests.Session()
_session.headers["User-Agent"] = "bottelefocus/1.0"


def _get(path, **params):
    last = None
    for attempt in range(3):
        try:
            r = _session.get(BASE + path, params=params, timeout=20)
            if r.status_code == 429:
                time.sleep(2 * (attempt + 1))
                continue
            r.raise_for_status()
            return r.json()
        except requests.RequestException as e:  # mạng chập chờn: thử lại
            last = e
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"Binance {path} lỗi: {last}")


def klines(symbol, interval, limit=200):
    """Trả về list dict: open_time, open, high, low, close, volume (nến đã đóng + nến đang chạy)."""
    raw = _get("/fapi/v1/klines", symbol=symbol, interval=interval, limit=limit)
    return [
        {
            "t": int(k[0]),
            "o": float(k[1]),
            "h": float(k[2]),
            "l": float(k[3]),
            "c": float(k[4]),
            "v": float(k[5]),
        }
        for k in raw
    ]


def premium_index(symbol):
    """Giá mark, funding rate hiện tại (theo chu kỳ 8h)."""
    d = _get("/fapi/v1/premiumIndex", symbol=symbol)
    return {"mark": float(d["markPrice"]), "funding": float(d["lastFundingRate"])}


def open_interest_hist(symbol, period="1h", limit=30):
    raw = _get("/futures/data/openInterestHist", symbol=symbol, period=period, limit=limit)
    return [{"t": int(x["timestamp"]), "oi": float(x["sumOpenInterest"]), "oi_usd": float(x["sumOpenInterestValue"])} for x in raw]


def long_short_accounts(symbol, period="1h", limit=1):
    raw = _get("/futures/data/globalLongShortAccountRatio", symbol=symbol, period=period, limit=limit)
    return float(raw[-1]["longShortRatio"]) if raw else None


def long_short_top_positions(symbol, period="1h", limit=1):
    raw = _get("/futures/data/topLongShortPositionRatio", symbol=symbol, period=period, limit=limit)
    return float(raw[-1]["longShortRatio"]) if raw else None


def taker_ratio(symbol, period="1h", limit=1):
    raw = _get("/futures/data/takerlongshortRatio", symbol=symbol, period=period, limit=limit)
    return float(raw[-1]["buySellRatio"]) if raw else None


def fetch_all(symbol, main_tf, higher_tf, limit):
    return {
        "k_main": klines(symbol, main_tf, limit),
        "k_high": klines(symbol, higher_tf, 120),
        "premium": premium_index(symbol),
        "oi": open_interest_hist(symbol, "1h", 30),
        "ls_accounts": long_short_accounts(symbol),
        "ls_top": long_short_top_positions(symbol),
        "taker": taker_ratio(symbol),
    }
