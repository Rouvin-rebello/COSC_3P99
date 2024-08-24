from unittest import TestCase
from Function_9_Source import DeckOfCards

class MockCard:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck = [MockCard(i + 1, 1) for i in range(13)]  # Create a mock deck of 13 cards
        self.deck_of_cards = DeckOfCards(self.deck)

    def test_deal_one_valid(self):
        card = self.deck_of_cards.deal_one()
        # Assure that one card is removed from the deck
        self.assertEqual(len(self.deck_of_cards.deck_of_cards), 12)
        # Assure that the card dealt is not in the deck anymore
        self.assertNotIn(card, self.deck_of_cards.deck_of_cards)

        # Deal another card and check the updated deck size
        self.deck_of_cards.deal_one()
        self.assertEqual(len(self.deck_of_cards.deck_of_cards), 11)
