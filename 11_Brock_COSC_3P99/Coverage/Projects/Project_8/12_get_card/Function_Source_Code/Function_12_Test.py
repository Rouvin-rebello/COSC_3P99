from unittest import TestCase
from Player import Player
from DeckOfCards import DeckOfCards
from Card import Card

class TestPlayer(TestCase):
    def setUp(self):
        self.player2 = Player("Lev", 10)
        self.deck = DeckOfCards()

    def test_get_card_valid(self):
        # Use the deck instance and set up a hand for player 2
        self.player2.set_hand(self.deck)
        # Verify that the initial deck length is 10
        self.assertEqual(len(self.player2.card_deck), 10)
        # Pick a card and confirm the deck now has 9 cards
        chosen_card = self.player2.get_card()
        self.assertEqual(len(self.player2.card_deck), 9)
        # Verify that the chosen card is not in the deck anymore
        self.assertNotIn(chosen_card, self.player2.card_deck)
