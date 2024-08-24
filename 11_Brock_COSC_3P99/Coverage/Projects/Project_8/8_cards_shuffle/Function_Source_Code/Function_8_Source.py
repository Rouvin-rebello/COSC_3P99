from random import shuffle

class DeckOfCards:
    def __init__(self, deck_of_cards):
        self.deck_of_cards = deck_of_cards

    # Shuffles the Deck of cards - Randoms the Places in the Deck (Type: List)
    def cards_shuffle(self):
        shuffle(self.deck_of_cards)
