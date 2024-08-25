# File: Function_Error_Handling.py

from random import randint

class DeckOfCards:
    def __init__(self, deck_of_cards):
        if not isinstance(deck_of_cards, list):
            raise TypeError("Deck must be a list of cards")
        if not all(isinstance(card, MockCard) for card in deck_of_cards):
            raise TypeError("All elements in deck must be instances of MockCard")
        self.deck_of_cards = deck_of_cards

    # Error handling: Ensure valid deck and elements before dealing
    def deal_one(self):
        random_card = randint(0, len(self.deck_of_cards) - 1)
        the_card = self.deck_of_cards.pop(random_card)
        return the_card
