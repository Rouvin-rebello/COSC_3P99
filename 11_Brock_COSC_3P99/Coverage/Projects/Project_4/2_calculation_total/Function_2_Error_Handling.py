def error_handling_calculation_total(hand):
    """Handles errors in calculating total hand value"""
    if not isinstance(hand, list):
        raise TypeError("calculation_total expects only list!")
    if any(not isinstance(item, int) for item in hand):
        raise TypeError("The list you've passed to calculation_total should contain only integers!")
    return sum(hand)
