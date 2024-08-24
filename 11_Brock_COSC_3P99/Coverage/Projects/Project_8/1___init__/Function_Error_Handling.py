# File: Function_Error_Handling.py

class Card:
    def __init__(self, card_value: int, card_suit: int):
        if type(card_value) != int:
            raise TypeError("card_value can only receive int")
        if type(card_suit) != int:
            raise TypeError("card_value can only receive int")
        self.card_value = card_value
        self.card_suit = card_suit
