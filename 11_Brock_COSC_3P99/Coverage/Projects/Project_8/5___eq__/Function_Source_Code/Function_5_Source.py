class Card:
    def __init__(self, card_value: int, card_suit: int):
        if type(card_value) != int:
            raise TypeError("card_value can only receive int")
        if type(card_suit) != int:
            raise TypeError("card_value can only receive int")
        if card_value > 13 or card_value < 1:
            raise ValueError("Card value must be between 1-13.")
        if card_suit > 4 or card_suit < 1:
            raise ValueError("card suit must be between 1-4.")
        self.card_value = card_value
        self.card_suit = card_suit

    def __eq__(self, other):
        if type(other) != Card:
            raise TypeError("other must be of type Card")
        elif self.card_value == other.card_value and self.card_suit == other.card_suit:
            return True
        else:
            return False
