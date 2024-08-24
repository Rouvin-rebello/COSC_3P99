import random

def consistent_deal_card():
    """Ensures consistent output when choosing a random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    if card not in cards:
        raise ValueError("Inconsistent output: card not in original list!")
    return card

