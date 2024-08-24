# File: Function_Boundary_Conditions.py

from random import shuffle

class DeckOfCards:
    def __init__(self, deck_of_cards):
        self.deck_of_cards = deck_of_cards

    # Boundary conditions: Handle edge cases such as empty or single-card decks
    def cards_shuffle(self):
        if len(self.deck_of_cards) <= 1:
            return  # No need to shuffle if deck is empty or contains only one card
        shuffle(self.deck_of_cards)
