def boundary_calculation_total(hand):
    """Handles boundary conditions for calculating total hand value"""
    total = sum(hand)
    if total == 21 and len(hand) == 2:
        return 0
    if 11 in hand and total > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)
