# File: Function_Error_Handling.py

from random import shuffle

class DeckOfCards:
    def __init__(self, deck_of_cards):
        if not isinstance(deck_of_cards, list):
            raise TypeError("Deck must be a list of cards")
        self.deck_of_cards = deck_of_cards

    # Error handling: Ensure the deck is valid before shuffling
    def cards_shuffle(self):
        shuffle(self.deck_of_cards)
