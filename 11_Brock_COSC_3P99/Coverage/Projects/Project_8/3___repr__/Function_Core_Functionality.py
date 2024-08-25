# File: Function_Core_Functionality.py

class Card:
    def __init__(self, card_value: int, card_suit: int):
        self.card_value = card_value
        self.card_suit = card_suit

    # Core functionality: developer-friendly string representation
    def __repr__(self):
        return f"Card(value={self.card_value}, suit={self.card_suit})"
