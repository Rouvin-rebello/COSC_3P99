# File: Function_Boundary_Conditions.py

class Card:
    def __init__(self, card_value: int, card_suit: int):
        self.card_value = card_value
        self.card_suit = card_suit

    # Boundary conditions: ensure card equality is only based on value and suit
    def __eq__(self, other):
        return self.card_value == other.card_value and self.card_suit == other.card_suit
