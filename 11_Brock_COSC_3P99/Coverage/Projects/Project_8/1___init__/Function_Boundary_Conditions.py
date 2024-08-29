# File: Function_Boundary_Conditions.py

class Card:
    def __init__(self, card_value: int, card_suit: int):
        if card_value > 13 or card_value < 1:
            raise ValueError("Card value must be between 1-13.")
        if card_suit > 4 or card_suit < 1:
            raise ValueError("Card suit must be between 1-4.")
        self.card_value = card_value
        self.card_suit = card_suit