"""Kiểm thử backtest trên dữ liệu giả lập."""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from backtest import run as B
from tests.test_indicators import make_klines


def _data(drift, seed):
    k4 = make_klines(1500, drift=drift, vol=0.008, seed=seed)
    # nến 1D gộp từ 6 nến 4h
    k1 = []
    for i in range(0, len(k4) - 5, 6):
        w = k4[i : i + 6]
        k1.append({"t": w[0]["t"], "o": w[0]["o"], "h": max(x["h"] for x in w), "l": min(x["l"] for x in w), "c": w[-1]["c"], "v": sum(x["v"] for x in w)})
    return k4, k1


def test_strategies_produce_signals_and_metrics():
    k4, k1 = _data(0.002, 7)
    for key, (_, fn) in B.STRATS.items():
        sig = fn(k4, k1)
        assert len(sig) == len(k4)
        assert set(sig) <= {-1, 0, 1}
    d = B.directional(k4, B.strat_trend(k4, k1))
    assert d["7d"]["n"] > 0 and 0 <= d["7d"]["hit"] <= 1
    t = B.trade_sim(k4, B.strat_donchian(k4, k1))
    assert t["n"] > 0 and "profit_factor" in t


def test_uptrend_favors_long_signals():
    k4, k1 = _data(0.004, 11)
    sig = B.strat_ema_cross(k4, k1)
    assert sig.count(1) > sig.count(-1)
    t = B.trade_sim(k4, sig)
    assert t["total_return"] > 0


def test_volume_profile_shape_and_vp_strategies():
    k4, k1 = _data(0.001, 5)
    B.CFG = B.TF["4h"]
    vp = B.volume_profile(k4, 60)
    assert len(vp) == len(k4) and vp[10] is None and vp[-1] is not None
    p = vp[-1]
    assert p["val"] <= p["poc"] <= p["vah"]
    lo = min(x["l"] for x in k4[-61:-1]); hi = max(x["h"] for x in k4[-61:-1])
    assert lo * 0.99 <= p["val"] and p["vah"] <= hi * 1.01
    for fn in (B.strat_vp_breakout, B.strat_vp_revert, B.strat_vp_ema):
        sig = fn(k4, k1)
        assert len(sig) == len(k4) and set(sig) <= {-1, 0, 1} and any(sig)


def test_rsi_and_combo_strategies():
    k4, k1 = _data(0.001, 9)
    B.CFG = B.TF["4h"]
    r = B.rsi_series([x["c"] for x in k4])
    assert r[13] is None and all(0 <= v <= 100 for v in r[14:])
    for key in ("rsi50", "vp_rsi", "vp_rsi_vol", "vp_rsi_adx", "vp_rsi_revert", "confluence", "vp_rsi_vol_ema", "vp_rsi_vol_ema_x"):
        sig = B.STRATS[key][1](k4, k1)
        assert len(sig) == len(k4) and set(sig) <= {-1, 0, 1}, key


def test_smc_and_price_action_strategies():
    from backtest import smc
    k4, k1 = _data(0.002, 13)
    B.CFG = B.TF["4h"]
    lh, ll, highs, lows = smc.swings(k4, 5)
    assert highs and lows and all(conf == j + 5 for j, _, conf in highs)
    st, breaks = smc.structure(k4, 5)
    assert set(st) <= {-1, 0, 1} and breaks
    for key in smc.STRATS:
        sig = B.STRATS[key][1](k4, k1)
        assert len(sig) == len(k4) and set(sig) <= {-1, 0, 1} and any(sig), key
    assert B.trade_sim(k4, B.STRATS["smc_bos"][1](k4, k1))["n"] > 0


def test_stock_market_strategies():
    from backtest import stock
    k4, k1 = _data(0.002, 17)
    B.CFG = B.TF["4h"]
    hi = stock.high_index(k4, k1, B.CFG)
    assert all(hi[i] < 0 or k1[hi[i]]["t"] + B.CFG["high_ms"] <= k4[i]["t"] for i in range(len(k4)))
    for key in stock.STRATS:
        sig = B.STRATS[key][1](k4, k1)
        assert len(sig) == len(k4) and set(sig) <= {-1, 0, 1}, key
        if key not in ("st_orb", "st_vwap", "st_base", "st_darvas", "st_pct_b"):  # st_base cần co biên + khối lượng, dữ liệu giả lập hiếm có
            assert any(sig), key
    B.CFG = B.TF["1h"]
    k1h = make_klines(2000, drift=0.001, vol=0.004, seed=3)
    for i, x in enumerate(k1h):
        x["t"] = 1_700_000_000_000 + i * 3600_000
    for key in ("st_orb", "st_vwap"):
        sig = stock.STRATS[key][1](k1h, k1, B.CFG)
        assert len(sig) == len(k1h) and any(sig), key
    B.CFG = B.TF["4h"]


def test_trade_sim_no_reentry_on_stop_bar_and_gap_fill():
    k = [{"t": i * 4 * 3600_000, "o": 100.0, "h": 101.0, "l": 99.0, "c": 100.0, "v": 1.0} for i in range(40)]
    k[30].update(o=70.0, h=96.0, l=60.0, c=95.0)  # mở gap qua dừng lỗ
    B.CFG = B.TF["4h"]
    t = B.trade_sim(k, [1] * 40)
    assert t["n"] == 1 and t["total_return"] < -25  # khớp ở giá mở 70, không vào lại cùng nến
    assert t["max_drawdown"] > 25
    from backtest import stock
    assert abs(stock.wilder(list(range(1, 15)) + [100], 14)[13] - 7.5) < 1e-9


def test_scalp_simulator_semantics():
    from backtest import scalp
    k = [{"t": i * 900_000, "o": 100.0, "h": 100.5, "l": 99.5, "c": 100.0, "v": 1.0} for i in range(60)]
    atr = [1.0] * 60
    # 1. cùng nến chạm cả TP (102) lẫn SL (99): tính là SL
    k2 = [dict(x) for x in k]; k2[11].update(h=103.0, l=98.0)
    tr = scalp.simulate(k2, atr, [(10, 1, None, None, None)], 2.0, 1.0, 16, scalp.TAKER)
    assert len(tr) == 1 and abs(tr[0][3] - (99.0 / 100.0 - 1 - 0.001)) < 1e-9
    # 2. nến mở qua SL: khớp ở giá mở
    k3 = [dict(x) for x in k]; k3[12].update(o=97.0, h=97.5, l=96.0, c=97.0)
    tr = scalp.simulate(k3, atr, [(10, 1, None, None, None)], 2.0, 1.0, 16, scalp.TAKER)
    assert abs(tr[0][3] - (97.0 / 100.0 - 1 - 0.001)) < 1e-9 and tr[0][2] == 12
    # 3. hết thời gian: đóng ở close nến thứ hold sau khi vào
    tr = scalp.simulate(k, atr, [(10, 1, None, None, None)], 2.0, 1.0, 16, scalp.TAKER)
    assert tr[0][1] == 11 and tr[0][2] == 27 and abs(tr[0][3] + 0.001) < 1e-9
    # 4. lệnh chờ: không chạm trong 4 nến thì bỏ; chạm thì khớp tại mức, phí maker
    tr = scalp.simulate(k, atr, [(10, 1, 99.0, None, None)], 2.0, 1.0, 16, scalp.MAKER)
    assert tr == []
    k4 = [dict(x) for x in k]; k4[13].update(l=98.8); k4[20].update(h=101.2)
    tr = scalp.simulate(k4, atr, [(10, 1, 99.0, None, None)], 2.0, 1.0, 16, scalp.MAKER)
    assert tr[0][1] == 13 and tr[0][2] == 20 and abs(tr[0][3] - (101.0 / 99.0 - 1 - 0.0007)) < 1e-9
    # 5. một lệnh một lúc: tín hiệu trong lúc đang giữ bị bỏ qua
    tr = scalp.simulate(k, atr, [(10, 1, None, None, None), (12, 1, None, None, None)], 2.0, 1.0, 16, scalp.TAKER)
    assert len(tr) == 1
    m = scalp.metrics(tr, 60, 96)
    assert m["n"] == 1 and m["per_day"] > 0


def test_vp_vol_profiles_and_features():
    from backtest import vp_vol
    k4, _ = _data(0.001, 8)
    prof = vp_vol.profiles(k4, 180)
    p = prof[-1]
    assert prof[100] is None and p["val"] <= p["poc"] <= p["vah"] and 0 <= p["poc_pos"] <= 1 and p["node"] >= 0
    feats = vp_vol.features(k4, vp_vol.FRAMES["4h"])
    f = feats[-1]
    assert f["state"] in ("trên VAH", "trong vùng", "dưới VAL") and f["shape"].startswith("POC")
    assert vp_vol.targets(k4, len(k4) - 1, 6, 42) is None  # không đủ nến tới
    t = vp_vol.targets(k4, 1000, 6, 42)
    assert t and t["ratio"] > 0 and t["range"] > 0
