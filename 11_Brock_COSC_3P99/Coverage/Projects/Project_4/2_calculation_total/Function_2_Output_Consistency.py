def consistent_calculation_total(hand):
    """Ensures consistent output when calculating total hand value"""
    total = sum(hand)
    if total > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
    return sum(hand)
