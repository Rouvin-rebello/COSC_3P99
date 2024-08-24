try:
    import os
    import sys

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                ''
            )
        )
    )
except:
    raise



from unittest import TestCase, mock
from Player import Player
from DeckOfCards import DeckOfCards
from Card import Card
from Function_11_Core import set_hand_core
from Function_11_Boundary import set_hand_boundary
from Function_11_ErrorHandling import set_hand_error_handling
from Function_11_Integration import set_hand_integration

class TestPlayer(TestCase):
    def setUp(self):
        self.player1 = Player("Yan", 26)
        self.player2 = Player("Lev", 10)
        self.deck = DeckOfCards()

    def test_set_hand_core(self):
        # Test Core Functionality block
        set_hand_core(self.player2, self.deck)
        self.assertEqual(len(self.player2.card_deck), self.player2.number_of_card)

    def test_set_hand_boundary(self):
        # Test Boundary Conditions and Edge Cases block
        deck = DeckOfCards()
        player = Player("Test", 100)
        with self.assertRaises(ValueError):
            set_hand_boundary(player, deck)

    def test_set_hand_error_handling(self):
        # Test Error Handling block
        with self.assertRaises(TypeError):
            set_hand_error_handling(self.player1, "Not a DeckOfCards")
        self.deck.deck_of_cards = []
        with self.assertRaises(ValueError):
            set_hand_error_handling(self.player1, self.deck)

    @mock.patch('DeckOfCards.DeckOfCards.deal_one', return_value=Card(3, 3))
    def test_set_hand_integration_invalid_card_is_duplicated(self, mock_deal_one):
        with self.assertRaises(ValueError):
            set_hand_integration(self.player2, self.deck)

    @mock.patch('DeckOfCards.DeckOfCards.deal_one', return_value=None)
    def test_set_hand_integration_invalid_card_is_None(self, mock_deal_one):
        with self.assertRaises(ValueError):
            set_hand_integration(self.player2, self.deck)

    def test_set_hand_integration(self):
        # Test Integration block (full integration)
        deck = DeckOfCards()
        set_hand_integration(self.player1, deck)
        self.assertEqual(len(self.player1.card_deck), self.player1.number_of_card)

