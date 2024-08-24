class Card:
    # Card value is "Ace, 2,3,4,5..."Jack", "Queen", "King"
    # Card Suit is "Diamond","Spade","Heart","Club"...
    # When Card value and card suit is not type(int) - Error
    # When Card value higher than 13 or lower than 1 - Error
    # When Card Suit higher than 4 and lower than 1 - Error
    def __init__(self, card_value: int, card_suit: int):
        # when card value and/or card suit is not integer, error will appear
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

    # Str - shows the value and the suit of the card
    def __str__(self):
        values = {1: "Ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "Jack",
                    12: "Queen", 13: "King"}
        suit = {1: "Diamond", 2: "Spade", 3: "Heart", 4: "Club"}
        return f"{values[self.card_value]} of {suit[self.card_suit]}"

    # repr - shows the value and the suit of the card
    def __repr__(self):
        values = {1: "Ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "Jack",
                  12: "Queen", 13: "King"}
        suit = {1: "Diamond", 2: "Spade", 3: "Heart", 4: "Club"}
        return f"{values[self.card_value]} of {suit[self.card_suit]}"

    # gt - True means Self.card_value and/or self.card_suit is higher than other.card_value and/or other.card_suit
    # gt - False means Self.card_value and/or self.card_suit is Lower than other.card_value and/or other.card_suit
    # Ace(1) is the highest value of them all
    # Means if self is Ace and other is Ace, the method checks The suits of the cards
    # If the cards have different values the card with the highest value wins
    # If the Cards have the same Values, The Method checks the cards suits, and the highest suit wins
    def __gt__(self, other):
        if type(other) != Card:
            raise TypeError("other must be of type Card")
        if self.card_value == 1 and other.card_value != 1:
            return True
        elif self.card_value != 1 and other.card_value == 1:
            return False
        elif self.card_value > other.card_value:
            return True
        elif self.card_value < other.card_value:
            return False
        elif self.card_value == other.card_value:
            if self.card_suit > other.card_suit:
                return True
            else:
                return False

    def __eq__(self, other):
        if type(other) != Card:
            raise TypeError("other must be of type Card")
        elif self.card_value == other.card_value and self.card_suit == other.card_suit:
            return True
        else:
            return False