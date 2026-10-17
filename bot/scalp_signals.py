"""Tín hiệu scalp 1h, dùng lại đúng mã của backtest/scalp.py để bot và backtest không lệch nhau.

Chỉ giữ hai cách còn lãi NGOÀI MẪU (11 tháng cuối, sau khi tối ưu tham số trên 70% đầu của 3 năm):
  - vp_limit: lệnh chờ tại VAL/VAH của profile 7 ngày khi giá trong vùng và cách mép dưới 1 ATR
              (ETH PF 1,32 +28%, SOL 1,35 +41%, BTC 0,99 -> bỏ BTC). TP 1 ATR, SL 1,5 ATR, hủy sau 4 giờ, đóng sau 8 giờ.
  - squeeze_1d: Bollinger hẹp nhất 48 giờ rồi bung với khối lượng 1,5x, cùng chiều EMA20/50 ngày
              (BTC 1,18 +5%, ETH 1,45 +16%, SOL 1,35 +13%; chỉ ~0,2 lệnh/ngày). TP 3 ATR, SL 1,5 ATR, đóng sau 8 giờ.
Giả định của backtest: lệnh chờ khớp ngay khi giá chạm mức (thực tế có thể không khớp), phí maker 0,02% / taker 0,05%.
"""
from backtest import scalp as S

SETUPS = {
    "vp_limit": dict(label="Lệnh chờ tại mép vùng giá trị 7 ngày", fn=S.sig_vp_limit, use_regime=False, tp=1.0, sl=1.5, hold=8, wait=4,
                     symbols=("ETHUSDT", "SOLUSDT"), stats="ngoài mẫu 11 tháng: ETH PF 1,32 (+28%), SOL 1,35 (+41%); BTC hòa nên bỏ"),
    "squeeze_1d": dict(label="Nén Bollinger 48 giờ rồi bung, cùng chiều ngày", fn=S.sig_squeeze, use_regime=True, tp=3.0, sl=1.5, hold=8, wait=0,
                       symbols=("BTCUSDT", "ETHUSDT", "SOLUSDT"), stats="ngoài mẫu 11 tháng: BTC PF 1,18 (+5%), ETH 1,45 (+16%), SOL 1,35 (+13%)"),
}


def detect(symbol, k1h, k4h, k1d):
    """k*: nến ĐÃ ĐÓNG. Trả về danh sách setup vừa xuất hiện ở nến 1h cuối cùng."""
    if not k1h or len(k1h) < S.FRAMES["1h"]["vp_window"] + 20:
        return []
    ctx = S.context(k1h, S.FRAMES["1h"], {"1d": k1d, "4h": k4h})
    last = len(k1h) - 1
    a = ctx["atr"][last]
    out = []
    for key, cfg in SETUPS.items():
        if symbol not in cfg["symbols"] or not a:
            continue
        sigs = [s for s in cfg["fn"](k1h, ctx, cfg["use_regime"]) if s[0] == last]
        for _, d, limit, _, _ in sigs:
            entry = limit if limit is not None else k1h[last]["c"]
            out.append({
                "key": key, "label": cfg["label"], "dir": d, "entry": entry, "limit": limit is not None,
                "tp": entry + d * cfg["tp"] * a, "sl": entry - d * cfg["sl"] * a, "tp_atr": cfg["tp"], "sl_atr": cfg["sl"],
                "hold": cfg["hold"], "wait": cfg["wait"], "atr": a, "t": k1h[last]["t"], "stats": cfg["stats"],
                "poc": ctx["prof"][last]["poc"] if ctx["prof"][last] else None,
            })
    return out
