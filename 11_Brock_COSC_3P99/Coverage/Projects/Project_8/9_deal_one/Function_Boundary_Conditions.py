# File: Function_Boundary_Conditions.py

from random import randint

class DeckOfCards:
    def __init__(self, deck_of_cards):
        self.deck_of_cards = deck_of_cards

    # Boundary conditions: Deal from a non-empty deck, handle empty deck scenario
    def deal_one(self):
        if len(self.deck_of_cards) == 0:
            raise ValueError("Cannot deal from an empty deck")
        random_card = randint(0, len(self.deck_of_cards) - 1)
        the_card = self.deck_of_cards.pop(random_card)
        return the_card
