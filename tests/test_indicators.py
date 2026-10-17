"""Kiểm thử chỉ báo trên dữ liệu giả lập (không cần mạng)."""
import math
import random

from bot import indicators as I, config as C, report


def make_klines(n, start=100.0, drift=0.0, vol=0.01, seed=1, t0=0, step=4 * 3600_000):
    rnd = random.Random(seed)
    out, p = [], start
    for i in range(n):
        o = p
        c = o * math.exp(drift + rnd.gauss(0, vol))
        h = max(o, c) * (1 + abs(rnd.gauss(0, vol / 2)))
        l = min(o, c) * (1 - abs(rnd.gauss(0, vol / 2)))
        out.append({"t": t0 + i * step, "o": o, "h": h, "l": l, "c": c, "v": 1000 + rnd.random() * 100})
        p = c
    return out


def make_data(drift=0.0, vol=0.01, oi_growth=0.0, funding=0.0001, ls=1.0, seed=1):
    oi = [{"t": i, "oi": 1000 * (1 + oi_growth) ** i, "oi_usd": 1e9} for i in range(30)]
    return {
        "k_main": make_klines(200, drift=drift, vol=vol, seed=seed),
        "k_high": make_klines(120, drift=drift * 6, vol=vol * 2.4, seed=seed + 1, step=86_400_000),
        "premium": {"mark": 100.0, "funding": funding},
        "oi": oi,
        "ls_accounts": ls,
        "ls_top": ls,
        "taker": 1.0,
    }


def test_flat_market_has_no_trend_and_mid_score():
    r = I.compute("BTCUSDT", make_data())
    assert r["trend"] == "flat"
    assert 20 <= r["score"] <= 80
    assert all(k in r for k in ("atr_pct", "rv_24h", "bbw", "oi_chg_4h", "funding"))


def test_strong_uptrend_detected():
    r = I.compute("ETHUSDT", make_data(drift=0.008, vol=0.004, seed=3))
    assert r["trend_4h"] == "up"
    assert r["trend_1d"] == "up"
    assert r["trend"] == "up"
    assert any(code == "trend" for code, _, _ in r["signals"])


def test_long_hot_signal():
    d = make_data(drift=0.008, vol=0.004, oi_growth=0.02, funding=0.001, ls=3.0, seed=3)
    r = I.compute("SOLUSDT", d)
    assert r["oi_chg_4h"] >= C.OI_CHANGE_4H
    assert any(code == "long_hot" for code, _, _ in r["signals"])


def test_score_rises_with_volatility():
    calm = I.compute("BTCUSDT", make_data(vol=0.003, seed=5))
    # 30 nến cuối biến động mạnh gấp 5 lần
    d = make_data(vol=0.003, seed=5)
    wild = make_klines(30, start=d["k_main"][-31]["c"], vol=0.02, seed=9, t0=d["k_main"][-31]["t"])
    d["k_main"] = d["k_main"][:-30] + wild
    stormy = I.compute("BTCUSDT", d)
    assert stormy["score"] > calm["score"]
    assert stormy["atr_ratio"] > 1.5


def test_report_renders():
    r = I.compute("BTCUSDT", make_data(), dvol=55.0)
    text = report.hourly_digest([r])
    assert "BTC" in text and "biến động <b>" in text
    assert "DVOL 55" in text
    assert "Mở biểu đồ" in report.trend_alert(r, "up")


def test_daily_signals_cross_and_stop():
    d = make_data(drift=0.004, vol=0.004, seed=3)
    r = I.compute("ETHUSDT", d)
    dd = r["daily"]
    assert dd["regime"] in ("up", "down") and dd["stop"] is not None
    assert isinstance(dd["crossed"], bool) and dd["bars_in_regime"] >= 1
    assert "Ngày:" in report.hourly_digest([r])
    assert "KHUNG NGÀY" in report.daily_trend_alert(r, "down")


def test_volume_profile_in_compute_and_alert():
    r = I.compute("BTCUSDT", make_data(seed=4))
    for tf in ("vp_4h", "vp_1d"):
        p = r[tf]["profile"]
        assert p and p["val"] <= p["poc"] <= p["vah"]
        assert r[tf]["state"] in ("above", "below", "inside")
    assert "VP 30 ngày" in report.hourly_digest([r]) and "VP 90 ngày" in report.hourly_digest([r])
    r["vp_4h"]["state"] = "above"
    assert "THOÁT VÙNG GIÁ TRỊ LÊN" in report.vp_alert(r, "vp_4h", "inside")


def test_daily_vp_confirmation_fields():
    r = I.compute("ETHUSDT", make_data(seed=6))
    v = r["vp_1d"]
    assert v["rsi"] is None or 0 <= v["rsi"] <= 100
    assert v["vol_ratio"] is None or v["vol_ratio"] > 0
    assert isinstance(v["confirmed"], bool)
    v["state"], v["rsi"], v["vol_ratio"], v["confirmed"] = "above", 62.0, 2.1, True
    assert "Có xác nhận RSI" in report.vp_alert(r, "vp_1d", "inside")
    v["confirmed"] = False
    assert "Chưa xác nhận" in report.vp_alert(r, "vp_1d", "inside")


def test_market_block_and_regimes():
    from bot import dominance
    base = lambda v, e20, e50, w: {"value": v, "ema20": e20, "ema50": e50, "chg_1w": w, "chg_1d": None, "chg_1m": None, "rsi": 75, "adx": None, "rating": None}
    dom = {"BTC.D": base(55, 56, 57, -1.0), "USDT.D": base(4.0, 4.2, 4.4, -3.0), "OTHERS.D": base(10, 9.5, 9.0, 2.0)}
    ana = dominance.analyze(dom)
    assert ana["regime"] == "alt_season" and ana["dirs"] == {"BTC.D": "down", "USDT.D": "down", "OTHERS.D": "up"}
    dom["USDT.D"] = base(5.0, 4.8, 4.6, 3.0); dom["BTC.D"] = base(58, 57, 56, 1.0)
    ana = dominance.analyze(dom)
    assert ana["regime"] == "risk_off_alt" and any("quá mua" in n for n in ana["notes"])
    text = report.market_block(dom, ana)
    assert "BTC.D <b>58.0%</b>" in text and "Tiền rút về stablecoin" in text
    assert "Chưa lấy được" in report.market_block(None, None)
    assert "DÒNG TIỀN THỊ TRƯỜNG ĐỔI" in report.market_alert(dom, ana, "trước")
