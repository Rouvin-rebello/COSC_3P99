# File: Function_Output_Consistency.py

class Card:
    def __init__(self, card_value: int, card_suit: int):
        self.card_value = card_value
        self.card_suit = card_suit

    # Output consistency: ensuring consistent comparison of cards with the same value
    def __gt__(self, other):
        if self.card_value == other.card_value:
            return self.card_suit > other.card_suit
        return self.card_value > other.card_value
