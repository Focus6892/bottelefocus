"""Điểm vào. Chạy mỗi 15 phút bằng GitHub Actions.

- Đúng đầu giờ (giờ chưa gửi bản tin): gửi bản tin tổng hợp 3 đồng.
- Mỗi lần chạy: nếu xu hướng đổi (ngang -> tăng/giảm, hoặc ngược lại) hoặc có tín hiệu
  mức cao mới, gửi cảnh báo ngay. Cùng tín hiệu không lặp lại trong ALERT_COOLDOWN_MIN phút.
Trạng thái lưu ở state/state.json và được workflow commit lại.
"""
import json
import os
import sys
import time
from datetime import datetime, timezone

from . import binance, config as C, deribit, indicators, okx, report, telegram

STATE_PATH = os.environ.get("STATE_PATH", "state/state.json")


def load_state():
    try:
        with open(STATE_PATH) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"trend": {}, "alerts": {}, "last_digest_hour": None}


def save_state(st):
    os.makedirs(os.path.dirname(STATE_PATH) or ".", exist_ok=True)
    with open(STATE_PATH, "w") as f:
        json.dump(st, f, indent=1, ensure_ascii=False)


def collect():
    results = []
    source = os.environ.get("DATA_SOURCE", "auto")
    for sym in C.SYMBOLS:
        if source == "okx":
            d = okx.fetch_all(sym, C.MAIN_TF, C.HIGHER_TF, C.KLINE_LIMIT)
        else:
            try:
                d = binance.fetch_all(sym, C.MAIN_TF, C.HIGHER_TF, C.KLINE_LIMIT)
            except Exception as e:  # Binance chặn IP Mỹ (HTTP 451) -> dùng OKX
                print(f"[{sym}] Binance lỗi ({e}); chuyển sang OKX", flush=True)
                source = "okx"
                d = okx.fetch_all(sym, C.MAIN_TF, C.HIGHER_TF, C.KLINE_LIMIT)
        print(f"[{sym}] nguồn: {source if source != 'auto' else 'binance'}", flush=True)
        dv = deribit.dvol(C.DVOL_CURRENCIES[sym]) if sym in C.DVOL_CURRENCIES else None
        results.append(indicators.compute(sym, d, dv))
    return results


def run(force_digest=False, dry=False):
    st = load_state()
    results = collect()
    now = time.time()
    hour_key = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H")
    sent = []

    # 1. Cảnh báo xu hướng khung ngày đổi (cắt EMA20/50), nén ngày rồi bung, và tín hiệu khẩn
    st.setdefault("trend_1d", {})
    for r in results:
        d = r["daily"]
        prev = st["trend_1d"].get(r["symbol"])
        if prev is None:
            st["trend_1d"][r["symbol"]] = d["regime"]  # lần đầu: ghi nhận, không báo
        elif d["regime"] != prev:
            sent.append(report.daily_trend_alert(r, prev))
            st["trend_1d"][r["symbol"]] = d["regime"]
        st["trend"][r["symbol"]] = r["trend"]  # pha 4h chỉ ghi nhận, không báo riêng
        # Thoát vùng giá trị volume profile (4h: 30 ngày, 1D: 90 ngày)
        st.setdefault("vp", {})
        for tf in ("vp_4h", "vp_1d"):
            key = f"{r['symbol']}:{tf}"
            cur = r[tf]["state"]
            prev_vp = st["vp"].get(key)
            if cur == "none":
                continue
            if prev_vp is None:
                st["vp"][key] = cur
            elif cur != prev_vp:
                if cur in ("above", "below"):
                    sent.append(report.vp_alert(r, tf, prev_vp))
                st["vp"][key] = cur
        if d["squeeze_break"]:
            key = f"{r['symbol']}:squeeze_1d:{d['squeeze_break']}"
            if now - st["alerts"].get(key, 0) >= 7 * 86400:
                sent.append(report.daily_squeeze_alert(r))
                st["alerts"][key] = now
        urgent = []
        for code, level, text in r["signals"]:
            if level != "high" or code == "trend":
                continue
            key = f"{r['symbol']}:{code}"
            if now - st["alerts"].get(key, 0) >= C.ALERT_COOLDOWN_MIN * 60:
                urgent.append((code, level, text))
                st["alerts"][key] = now
        if urgent:
            sent.append(report.urgent_alert(r, urgent))

    # 2. Bản tin mỗi giờ
    if force_digest or st.get("last_digest_hour") != hour_key:
        sent.append(report.hourly_digest(results))
        st["last_digest_hour"] = hour_key

    for msg in sent:
        if dry:
            print(msg + "\n" + "-" * 40)
        else:
            telegram.send(msg)
    if not dry:
        save_state(st)
    # lưu snapshot chỉ báo để backtest ngưỡng sau này
    snap_dir = os.environ.get("SNAPSHOT_DIR", "state/history")
    if not dry:
        os.makedirs(snap_dir, exist_ok=True)
        with open(os.path.join(snap_dir, datetime.now(timezone.utc).strftime("%Y-%m-%d") + ".jsonl"), "a") as f:
            for r in results:
                f.write(json.dumps({k: v for k, v in r.items() if k != "signals"}, ensure_ascii=False) + "\n")
    return results, sent


if __name__ == "__main__":
    args = set(sys.argv[1:])
    run(force_digest="--digest" in args, dry="--dry" in args)
