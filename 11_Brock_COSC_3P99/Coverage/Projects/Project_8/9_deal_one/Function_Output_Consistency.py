# File: Function_Output_Consistency.py

from random import randint

class DeckOfCards:
    def __init__(self, deck_of_cards):
        self.deck_of_cards = deck_of_cards

    # Output consistency: Ensure deck length is consistent after dealing
    def deal_one(self):
        original_length = len(self.deck_of_cards)
        random_card = randint(0, original_length - 1)
        the_card = self.deck_of_cards.pop(random_card)
        assert len(self.deck_of_cards) == original_length - 1  # Ensure deck size is consistent
        return the_card
