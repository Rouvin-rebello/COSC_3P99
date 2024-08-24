from Card import Card
from random import *


class DeckOfCards:
    # Gets 13 cards of Diamonds
    # Gets 13 cards of Spade
    # Gets 13 cards of Heart
    # Gets 13 cards of Club
    # appends/adds them to the Deck(self.deck_of_Cards) - means 52 Cards in the Deck(List)
    def __init__(self):
        self.deck_of_cards = []
        cards_diamond = [Card(i+1, 1) for i in range(13)]
        for cards in cards_diamond:
            self.deck_of_cards.append(cards)
        cards_spade = [Card(i+1, 2) for i in range(13)]
        for cards in cards_spade:
            self.deck_of_cards.append(cards)
        cards_heart = [Card(i+1, 3) for i in range(13)]
        for cards in cards_heart:
            self.deck_of_cards.append(cards)
        cards_club = [Card(i+1, 4) for i in range(13)]
        for cards in cards_club:
            self.deck_of_cards.append(cards)

    # Shuffles the Deck of cards - Randoms the Places in the Deck(Type: List)
    def cards_shuffle(self):
        shuffle(self.deck_of_cards)

    # Picks a random card in the Deck And Pops/Deletes it from the Deck(The List), Returns the Card - (Value and Suit)
    def deal_one(self):
        for cards in self.deck_of_cards:
            random_card = randint(0, len(self.deck_of_cards)-1)
            the_card = self.deck_of_cards[random_card]
            self.deck_of_cards.pop(random_card)
            return the_card








