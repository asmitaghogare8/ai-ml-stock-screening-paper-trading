from ltq_analysis import (
    calculate_ltq_change,
    calculate_ltq_acceleration,
    get_ltq_direction
)


older_ltq = 10000
previous_ltq = 12000
current_ltq = 15000

change = calculate_ltq_change(previous_ltq, current_ltq)

acceleration = calculate_ltq_acceleration(
    previous_ltq,
    current_ltq,
    older_ltq
)

direction = get_ltq_direction(
    previous_ltq,
    current_ltq
)

print("LTQ Change:", change)
print("LTQ Acceleration:", acceleration)
print("LTQ Direction:", direction)