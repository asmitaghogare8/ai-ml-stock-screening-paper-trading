def detect_signal(smma20, smma120):
    if smma20[-2] <= smma120[-2] and smma20[-1] > smma120[-1]:
        return "BUY"

    if smma20[-2] >= smma120[-2] and smma20[-1] < smma120[-1]:
        return "SELL"

    return "HOLD"