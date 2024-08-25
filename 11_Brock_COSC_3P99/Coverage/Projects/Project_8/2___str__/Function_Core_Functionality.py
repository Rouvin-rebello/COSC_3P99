# File: Function_Core_Functionality.py

class Card:
    def __init__(self, card_value: int, card_suit: int):
        self.card_value = card_value
        self.card_suit = card_suit

    # Core functionality: string representation of the card
    def __str__(self):
        return f"{self.card_value} of {self.card_suit}"
