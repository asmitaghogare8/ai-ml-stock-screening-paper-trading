def calculate_smma(prices, period):
    smma = []

    if len(prices) < period:
        return smma

    first_smma = sum(prices[:period]) / period
    smma.append(first_smma)

    for i in range(period, len(prices)):
        value = ((smma[-1] * (period - 1)) + prices[i]) / period
        smma.append(value)

    return smma