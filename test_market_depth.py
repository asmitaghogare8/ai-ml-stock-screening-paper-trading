from market_depth import (
    calculate_imbalance,
    get_market_pressure,
    check_liquidity
)


bid_qty = 1200000
ask_qty = 800000

imbalance = calculate_imbalance(
    bid_qty,
    ask_qty
)

pressure = get_market_pressure(
    bid_qty,
    ask_qty
)

liquidity = check_liquidity(
    bid_qty,
    ask_qty
)

print("Bid Quantity:", bid_qty)
print("Ask Quantity:", ask_qty)
print("Bid/Ask Imbalance:", imbalance)
print("Market Pressure:", pressure)
print("Liquidity Requirement:", liquidity)