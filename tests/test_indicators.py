"""Kiểm thử chỉ báo trên dữ liệu giả lập (không cần mạng)."""
import json
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


def test_inside_bar_detection_and_alert():
    k = make_klines(300, drift=0.003, vol=0.004, seed=21)
    k[-3].update(o=100, h=110, l=90, c=105); k[-2].update(o=104, h=108, l=95, c=103); k[-1].update(o=103, h=115, l=102, c=112)
    ib = I.inside_bar(k, 100.0, 90.0)
    assert ib and ib["dir"] == 1 and ib["mother_high"] == 110
    assert I.inside_bar(k, 90.0, 100.0) is None  # ngược hướng EMA
    k[-2].update(h=111)
    assert I.inside_bar(k, 100.0, 90.0) is None  # không phải inside bar
    r = I.compute("ETHUSDT", make_data(), dvol=None)
    r["inside_4h"] = ib
    assert "INSIDE BAR 4h BUNG LÊN" in report.inside_alert(r)


def test_advisor_and_reviewer():
    from bot import advisor, reviewer
    r = I.compute("ETHUSDT", make_data(), dvol=None)
    r["daily"].update(regime="up", stop=r["price"] * 0.9, bars_in_regime=10)
    r["vp_1d"].update(state="above", confirmed=True)
    r["vp_4h"].update(state="above")
    r["trend"] = "up"; r["ichimoku_1d"] = "up"; r["weinstein_1d"] = "up"
    rec = advisor.recommend(r, None)
    assert rec["side"] == "LONG" and rec["stop"] == r["daily"]["stop"] and rec["confidence"] > 0.9
    stats = {"1d": {"ETH": {"ema_cross": {"trades": {"profit_factor": 3.0}}, "vp_rsi_vol": {"trades": {"profit_factor": 0.9}}}}}
    rv = reviewer.review(rec, r, None, stats)
    assert rv["verdict"] == "ĐỒNG Ý" and any("bỏ nguồn" in n for n in rv["notes"]) and rv["final"]["side"] == "LONG"
    # ngược khung ngày -> bác
    r["daily"]["regime"] = "down"; r["vp_1d"]["state"] = "above"; r["vp_4h"]["state"] = "above"; r["inside_4h"] = {"dir": 1, "mother_low": 1, "mother_high": 2, "close": 3, "t": 0}
    rec = advisor.recommend(r, None)
    if rec["side"] == "LONG":
        rv = reviewer.review(rec, r, None, {})
        assert rv["verdict"] == "BÁC" and rv["final"]["side"] == "NGOÀI"
    # long alt khi risk-off -> giữ lại
    r["daily"]["regime"] = "up"
    ana = {"regime": "risk_off", "text": "Tiền rút về stablecoin", "bias": "", "dirs": {}, "notes": []}
    rec = advisor.recommend(r, ana)
    rv = reviewer.review(rec, r, ana, {})
    assert rv["verdict"] in ("GIỮ LẠI", "ĐỒNG Ý")
    r["reco"] = rv
    text = report.hourly_digest([r])
    assert "🤖 Đề xuất" in text and "🧑‍⚖️ Review" in text
    assert "KHUYẾN NGHỊ MỚI" in report.reco_alert(r, "NGOÀI")


def test_ichimoku_and_weinstein_states():
    up = make_klines(120, drift=0.01, vol=0.002, seed=4)
    assert I.ichimoku_state(up) == "up" and I.weinstein_state([x["c"] for x in up]) == "up"
    dn = make_klines(120, drift=-0.01, vol=0.002, seed=4)
    assert I.ichimoku_state(dn) == "down" and I.weinstein_state([x["c"] for x in dn]) == "down"
    assert I.ichimoku_state(up[:50]) == "flat"
    r = I.compute("BTCUSDT", make_data(), dvol=None)
    assert r["ichimoku_1d"] in ("up", "down", "flat") and r["weinstein_1d"] in ("up", "down", "flat")


def test_vp_forecast_with_fake_study(tmp_path):
    from bot import vp_forecast
    k4 = make_klines(400, drift=0.002, vol=0.006, seed=31)
    k1d = make_klines(200, drift=0.002, vol=0.01, seed=32, step=86_400_000)
    k1h = make_klines(300, drift=0.001, vol=0.003, seed=33, step=3600_000)
    base = {"n": 500, "p_expand": 0.50, "ratio": 1.0, "range": 5.0, "p_up": 0.52}
    def grp(pe, pu, sig_e, sig_u, rng=5.0, cont=None):
        return {"n": 200, "p_expand": pe, "ratio": 1.0, "range": rng, "p_up": pu, "sig_expand": sig_e, "sig_up": sig_u, "continue": cont}
    study = {}
    for frame in ("1h", "4h", "1d"):
        study[frame] = {}
        for sym in ("BTC", "ETH", "SOL"):
            groups = {}
            for key, vals in (("state", ("trên VAH", "trong vùng", "dưới VAL")), ("width", ("hẹp", "vừa", "rộng")), ("shape", ("POC thấp (b)", "POC giữa (D)", "POC cao (P)")), ("node", ("LVN", "HVN", "bình thường")), ("dist", ("gần POC (<1 ATR)", "vừa", "xa POC (>3 ATR)"))):
                for v in vals:
                    groups[f"{key}={v}"] = grp(0.62 if key == "state" and v == "trên VAH" else 0.5, 0.60 if key == "node" and v == "LVN" else 0.52, key == "state" and v == "trên VAH", key == "node" and v == "LVN", 6.0)
            hz = {"24 giờ": {"base": base, "groups": groups}, "7 ngày": {"base": base, "groups": groups}, "3 ngày": {"base": base, "groups": groups}}
            study[frame][sym] = {**hz, "bars": 1000, "width_q": [0.02, 0.08]}
    path = tmp_path / "study.json"
    path.write_text(json.dumps(study))
    vp_forecast._cache.clear()
    vp_forecast.STUDY_PATH = str(path)
    st = vp_forecast.load_study(str(path))
    frames = {"1h": vp_forecast.live_features(k1h, "1h", "BTC", st), "4h": vp_forecast.live_features(k4, "4h", "BTC", st), "1d": vp_forecast.live_features(k1d, "1d", "BTC", st)}
    assert frames["4h"] and frames["4h"]["width"] in ("hẹp", "vừa", "rộng") and frames["1d"]
    fc = vp_forecast.forecast("BTC", frames, st)
    assert fc and "24 giờ tới" in fc and "7 ngày tới" in fc
    for v in fc.values():
        assert v["level"] in ("TĂNG", "GIẢM", "bình thường") and v["range"] > 0
    vf = {"features": {}, "forecast": fc}
    assert any("🔮 24 giờ tới" in x for x in vp_forecast.lines(vf))
    assert vp_forecast.lines(None) == []
    # không có thống kê -> không dự báo, bản tin vẫn chạy
    vp_forecast._cache.clear()
    vp_forecast.STUDY_PATH = str(tmp_path / "missing.json")
    r = I.compute("BTCUSDT", make_data(), dvol=None)
    assert r["vp_forecast"]["forecast"] is None and "🔮" not in report.hourly_digest([r])
