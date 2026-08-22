def calculate_ltq_change(previous_ltq, current_ltq):
    return current_ltq - previous_ltq


def calculate_ltq_acceleration(previous_ltq, current_ltq, older_ltq):
    previous_change = previous_ltq - older_ltq
    current_change = current_ltq - previous_ltq

    return current_change - previous_change


def get_ltq_direction(previous_ltq, current_ltq):
    if current_ltq > previous_ltq:
        return "INCREASING"

    if current_ltq < previous_ltq:
        return "DECREASING"

    return "STABLE"