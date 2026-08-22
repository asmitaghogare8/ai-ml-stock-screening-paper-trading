import numpy as np

from ml_model import train_model, predict_probability


# Sample training data
# Features:
# LTQ, LTQ change, LTQ acceleration,
# Bid quantity, Ask quantity,
# Bid/Ask imbalance, Price change,
# Volume, SMMA spread

X = np.array([
    [15000, 3000, 1000, 1200000, 800000, 0.20, 0.010, 5000000, 0.90],
    [12000, 2000, 500, 1100000, 900000, 0.10, 0.008, 4500000, 0.70],
    [8000, -2000, -1000, 700000, 1300000, -0.30, -0.010, 3000000, -0.50],
    [6000, -3000, -500, 600000, 1400000, -0.40, -0.012, 2800000, -0.70],
    [18000, 4000, 1500, 1500000, 700000, 0.36, 0.015, 6000000, 1.20],
    [7000, -1000, -500, 800000, 1200000, -0.20, -0.008, 3200000, -0.40],
    [16000, 3500, 1000, 1300000, 750000, 0.27, 0.012, 5500000, 1.00],
    [5000, -2500, -1000, 500000, 1500000, -0.50, -0.015, 2500000, -0.80],
    [14000, 2500, 800, 1250000, 850000, 0.19, 0.009, 4800000, 0.80],
    [6500, -1500, -700, 650000, 1350000, -0.35, -0.011, 2900000, -0.60]
])


# 1 = profitable trade
# 0 = losing trade

y = np.array([
    1,
    1,
    0,
    0,
    1,
    0,
    1,
    0,
    1,
    0
])


model, accuracy = train_model(X, y)

print("Model trained successfully.")
print("Model accuracy:", accuracy)


# Test one new trade
new_trade = np.array([
    [15000, 3000, 1000, 1200000, 800000, 0.20, 0.010, 5000000, 0.90]
])

probability = predict_probability(
    model,
    new_trade
)

print("Probability of profitable trade:", probability[0])