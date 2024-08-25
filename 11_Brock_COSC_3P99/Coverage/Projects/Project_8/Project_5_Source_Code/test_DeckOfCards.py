from unittest import TestCase
from DeckOfCards import DeckOfCards

class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck1 = DeckOfCards()
        self.deck2 = DeckOfCards()

    def test_deck_valid(self):
        # check if there are 52 cards in the deck, we compare the length to 52
        self.assertEqual(len(self.deck1.deck_of_cards), 52)
        self.assertEqual(len(self.deck2.deck_of_cards), 52)

    def test_cards_shuffle(self):
        # create two decks and compare their values, assure that the decks are unique
        self.deck2.cards_shuffle()
        print(self.deck1.deck_of_cards)
        print(self.deck2.deck_of_cards)
        for i in range(len(self.deck1.deck_of_cards)):
            # print(self.deck1.deck_of_cards[i])
            # print(self.deck2.deck_of_cards[i])
            if self.assertNotEqual(self.deck1.deck_of_cards[0], self.deck2.deck_of_cards[0]) == AssertionError:
                self.assertNotEqual(self.deck1.deck_of_cards[1], self.deck2.deck_of_cards[1])

    def test_deal_one_valid(self):
        card = self.deck1.deal_one()
        # deal a card, assure that a card is removed from the main deck after calling the method.
        self.assertEqual(len(self.deck1.deck_of_cards), 51)
        # assure that the card that we removed is not in the deck anymore
        self.assertNotIn(card, self.deck1.deck_of_cards)
        # and second time assure that the card is removed
        self.deck1.deal_one()
        self.assertEqual(len(self.deck1.deck_of_cards), 50)
        print(len(self.deck1.deck_of_cards))




























