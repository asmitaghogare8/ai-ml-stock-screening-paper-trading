def evaluate_trade(
    signal,
    ltq_direction,
    ltq_acceleration,
    bid_qty,
    ask_qty,
    smma20,
    smma120
):
    reasons = []
    score = 0

    # No crossover
    if signal == "HOLD":
        return "AVOID", score, ["No SMMA crossover"]

    # LTQ analysis
    if ltq_direction == "INCREASING":
        score += 1
        reasons.append("LTQ is increasing")
    else:
        score -= 1
        reasons.append("LTQ is not increasing")

    # LTQ acceleration
    if ltq_acceleration > 0:
        score += 1
        reasons.append("LTQ acceleration is positive")
    else:
        score -= 1
        reasons.append("LTQ acceleration is weak")

    # Bid/Ask analysis
    if signal == "BUY":
        if bid_qty > ask_qty:
            score += 1
            reasons.append("Strong bid support")
        else:
            score -= 1
            reasons.append("Weak bid support")

    elif signal == "SELL":
        if ask_qty > bid_qty:
            score += 1
            reasons.append("Strong ask pressure")
        else:
            score -= 1
            reasons.append("Weak ask pressure")

    # SMMA direction
    if signal == "BUY" and smma20 > smma120:
        score += 1
        reasons.append("SMMA 20 is above SMMA 120")

    elif signal == "SELL" and smma20 < smma120:
        score += 1
        reasons.append("SMMA 20 is below SMMA 120")

    else:
        score -= 1
        reasons.append("SMMA direction is weak")

    # Final decision
    if score >= 3:
        decision = "ACCEPT"
    else:
        decision = "AVOID"

    return decision, score, reasons