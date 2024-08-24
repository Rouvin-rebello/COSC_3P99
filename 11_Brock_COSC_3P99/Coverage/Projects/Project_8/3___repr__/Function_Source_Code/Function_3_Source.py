class Card:
    def __init__(self, card_value: int, card_suit: int):
        if type(card_value) != int:
            raise TypeError("card_value can only receive int")
        if type(card_suit) != int:
            raise TypeError("card_suit can only receive int")
        if card_value > 13 or card_value < 1:
            raise ValueError("Card value must be between 1-13.")
        if card_suit > 4 or card_suit < 1:
            raise ValueError("card suit must be between 1-4.")
        self.card_value = card_value
        self.card_suit = card_suit

    def __repr__(self):
        values = {1: "Ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "Jack",
                  12: "Queen", 13: "King"}
        suit = {1: "Diamond", 2: "Spade", 3: "Heart", 4: "Club"}
        return f"{values[self.card_value]} of {suit[self.card_suit]}"
