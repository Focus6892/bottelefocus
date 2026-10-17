"""Tải lịch sử nến 4h và 1D từ OKX (công khai) về backtest/data/*.json."""
import json
import os
import sys
import time

import requests

BASE = "https://www.okx.com/api/v5"
OUT = os.path.join(os.path.dirname(__file__), "data")
SYMBOLS = ["BTC-USDT-SWAP", "ETH-USDT-SWAP", "SOL-USDT-SWAP"]
BARS = {"1H": 3600_000, "4H": 4 * 3600_000, "1Dutc": 86_400_000, "1Wutc": 7 * 86_400_000, "15m": 15 * 60_000, "30m": 30 * 60_000}


def fetch(inst, bar, days):
    """Nến từ cũ đến mới, mỗi phần tử dict t,o,h,l,c,v. Chỉ lấy nến đã đóng."""
    stop = int(time.time() * 1000) - days * 86_400_000
    after = None
    rows = []
    for _ in range(1500):
        params = {"instId": inst, "bar": bar, "limit": 100}
        if after:
            params["after"] = after
        for attempt in range(4):
            r = requests.get(f"{BASE}/market/history-candles", params=params, timeout=20)
            if r.status_code == 200 and r.json().get("code") == "0":
                break
            time.sleep(1 + attempt)
        data = r.json()["data"]
        if not data:
            break
        for k in data:
            if k[8] == "1":  # confirm = nến đã đóng
                rows.append({"t": int(k[0]), "o": float(k[1]), "h": float(k[2]), "l": float(k[3]), "c": float(k[4]), "v": float(k[5])})
        after = data[-1][0]
        if int(after) < stop:
            break
        time.sleep(0.2)  # 3 luồng x 5 lượt/s < giới hạn 20 lượt / 2s
    rows = sorted({r["t"]: r for r in rows}.values(), key=lambda x: x["t"])
    return [r for r in rows if r["t"] >= stop]


def _one(inst, bar, days):
    rows = fetch(inst, bar, days)
    path = os.path.join(OUT, f"{inst.split('-')[0]}_{bar}.json")
    with open(path, "w") as f:
        json.dump(rows, f)
    print(f"{inst} {bar}: {len(rows)} nến, từ {time.strftime('%Y-%m-%d', time.gmtime(rows[0]['t']/1000)) if rows else '-'}", flush=True)


def main(days=1095, bars=None):
    """Tải song song 3 đồng (3 luồng, vẫn dưới giới hạn 20 lượt / 2 giây của OKX)."""
    from concurrent.futures import ThreadPoolExecutor
    os.makedirs(OUT, exist_ok=True)
    jobs = [(inst, bar) for bar in (bars or BARS) for inst in SYMBOLS]
    with ThreadPoolExecutor(max_workers=3) as ex:
        list(ex.map(lambda j: _one(j[0], j[1], days), jobs))


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 1095, sys.argv[2].split(",") if len(sys.argv) > 2 else None)
