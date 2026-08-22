def calculate_imbalance(bid_qty, ask_qty):
    total = bid_qty + ask_qty

    if total == 0:
        return 0

    return (bid_qty - ask_qty) / total


def get_market_pressure(bid_qty, ask_qty):
    if bid_qty > ask_qty:
        return "BUYING PRESSURE"

    if ask_qty > bid_qty:
        return "SELLING PRESSURE"

    return "BALANCED"


def check_liquidity(bid_qty, ask_qty):
    if bid_qty > 1000000 and ask_qty > 1000000:
        return True

    return False