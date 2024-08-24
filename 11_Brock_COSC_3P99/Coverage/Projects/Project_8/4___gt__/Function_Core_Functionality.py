# File: Function_Core_Functionality.py

class Card:
    def __init__(self, card_value: int, card_suit: int):
        self.card_value = card_value
        self.card_suit = card_suit

    # Core functionality: greater-than comparison based on card value and suit
    def __gt__(self, other):
        if self.card_value == 1 and other.card_value != 1:
            return True
        elif self.card_value != 1 and other.card_value == 1:
            return False
        elif self.card_value > other.card_value:
            return True
        elif self.card_value < other.card_value:
            return False
        elif self.card_value == other.card_value:
            return self.card_suit > other.card_suit
