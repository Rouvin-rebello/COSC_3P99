# File: Function_Output_Consistency.py

from random import shuffle

class DeckOfCards:
    def __init__(self, deck_of_cards):
        self.deck_of_cards = deck_of_cards

    # Output consistency: Maintain deck length and structure after shuffling
    def cards_shuffle(self):
        original_length = len(self.deck_of_cards)
        shuffle(self.deck_of_cards)
        assert len(self.deck_of_cards) == original_length  # Ensure the deck size is consistent
