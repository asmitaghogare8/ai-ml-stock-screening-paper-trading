from feature_engineering import calculate_features


features = calculate_features(
    ltp=250.50,
    ltq=15000,
    bid_qty=1200000,
    ask_qty=800000,
    volume=5000000,
    smma20=249.80,
    smma120=248.90
)

print("Stock Features:")
print(features)