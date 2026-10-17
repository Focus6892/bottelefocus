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
