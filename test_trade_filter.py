from trade_filter import evaluate_trade


decision, score, reasons = evaluate_trade(
    signal="BUY",
    ltq_direction="INCREASING",
    ltq_acceleration=1000,
    bid_qty=1200000,
    ask_qty=800000,
    smma20=250,
    smma120=249
)

print("Decision:", decision)
print("Score:", score)
print("Reasons:")

for reason in reasons:
    print("-", reason)