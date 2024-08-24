# File: Function_Core_Functionality.py

from random import shuffle

class DeckOfCards:
    def __init__(self, deck_of_cards):
        self.deck_of_cards = deck_of_cards

    # Core functionality: Shuffling the deck of cards
    def cards_shuffle(self):
        shuffle(self.deck_of_cards)
