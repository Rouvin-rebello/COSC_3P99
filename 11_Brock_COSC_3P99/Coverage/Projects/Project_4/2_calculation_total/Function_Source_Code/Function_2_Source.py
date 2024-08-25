def calculation_total(hand):
    if type(hand) != list:
        raise TypeError("calculation_total expects only list!")
    if any(type(item) is not int for item in hand):
        raise TypeError("The list you've passed to calculation_total should contain only integers!")

    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)
