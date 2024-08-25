import random

def error_handling_deal_card():
    """Handles errors in choosing a random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    if not isinstance(cards, list):
        raise TypeError("Cards must be in a list!")
    return random.choice(cards)
