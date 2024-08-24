# File: Function_Output_Consistency.py

class Card:
    def __init__(self, card_value: int, card_suit: int):
        self.card_value = card_value
        self.card_suit = card_suit

    # Output consistency: consistent string formatting
    def __repr__(self):
        values = {1: "Ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "Jack", 12: "Queen", 13: "King"}
        suits = {1: "Diamond", 2: "Spade", 3: "Heart", 4: "Club"}
        return f"{values[self.card_value]} of {suits[self.card_suit]}"

