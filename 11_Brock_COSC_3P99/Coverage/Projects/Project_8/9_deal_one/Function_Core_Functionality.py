# File: Function_Core_Functionality.py

from random import randint

class DeckOfCards:
    def __init__(self, deck_of_cards):
        self.deck_of_cards = deck_of_cards

    # Core functionality: Deal one random card from the deck
    def deal_one(self):
        random_card = randint(0, len(self.deck_of_cards) - 1)
        the_card = self.deck_of_cards.pop(random_card)
        return the_card
