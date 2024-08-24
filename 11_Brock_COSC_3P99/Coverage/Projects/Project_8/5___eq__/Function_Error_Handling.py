# File: Function_Error_Handling.py

class Card:
    def __init__(self, card_value: int, card_suit: int):
        self.card_value = card_value
        self.card_suit = card_suit

    # Error handling: ensure equality comparison is with another Card object
    def __eq__(self, other):
        if not isinstance(other, Card):
            raise TypeError("other must be of type Card")
        return False  # Placeholder for testing type-checking
