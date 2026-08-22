def calculate_features(ltp, ltq, bid_qty, ask_qty, volume, smma20, smma120):
    total_quantity = bid_qty + ask_qty

    if total_quantity == 0:
        imbalance = 0
    else:
        imbalance = (bid_qty - ask_qty) / total_quantity

    features = {
        "ltp": ltp,
        "ltq": ltq,
        "bid_qty": bid_qty,
        "ask_qty": ask_qty,
        "volume": volume,
        "smma20": smma20,
        "smma120": smma120,
        "smma_spread": smma20 - smma120,
        "bid_ask_imbalance": imbalance
    }

    return features