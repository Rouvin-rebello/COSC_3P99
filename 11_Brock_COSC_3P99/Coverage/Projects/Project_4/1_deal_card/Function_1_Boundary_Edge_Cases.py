import random

def boundary_deal_card():
    """Handles boundary conditions for choosing a random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    if not cards:
        raise ValueError("Card list is empty!")
    return random.choice(cards)
