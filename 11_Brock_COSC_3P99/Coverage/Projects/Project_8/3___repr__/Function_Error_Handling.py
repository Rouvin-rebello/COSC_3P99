# File: Function_Error_Handling.py

class Card:
    def __init__(self, card_value: int, card_suit: int):
        if not isinstance(card_value, int):
            raise TypeError("card_value must be an integer")
        if not isinstance(card_suit, int):
            raise TypeError("card_suit must be an integer")
        if card_value > 13 or card_value < 1:
            raise ValueError("Card value must be between 1-13.")
        if card_suit > 4 or card_suit < 1:
            raise ValueError("Card suit must be between 1-4.")
        self.card_value = card_value
        self.card_suit = card_suit

    # Error handling: correct representation based on input validity
    def __repr__(self):
        values = {1: "Ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "Jack", 12: "Queen", 13: "King"}
        suits = {1: "Diamond", 2: "Spade", 3: "Heart", 4: "Club"}
        return f"{values[self.card_value]} of {suits[self.card_suit]}"