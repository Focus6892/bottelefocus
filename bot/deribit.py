"""DVOL (chỉ số biến động kỳ vọng từ quyền chọn) từ Deribit, công khai."""
import time
import requests

BASE = "https://www.deribit.com/api/v2/public"


def dvol(currency):
    """DVOL mới nhất (điểm % quy năm) hoặc None nếu không lấy được."""
    now = int(time.time() * 1000)
    try:
        r = requests.get(
            f"{BASE}/get_volatility_index_data",
            params={"currency": currency, "resolution": "3600", "start_timestamp": now - 3 * 3600_000, "end_timestamp": now},
            timeout=20,
        )
        r.raise_for_status()
        data = r.json()["result"]["data"]
        return float(data[-1][4]) if data else None  # [ts, open, high, low, close]
    except Exception:
        return None
