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


from unittest import TestCase
from Player import Player
from DeckOfCards import DeckOfCards
from Function_12_Core import get_card_core
from Function_12_Boundary import get_card_boundary
from Function_12_ErrorHandling import get_card_error_handling
from Function_12_Integration import get_card_integration

class TestPlayer(TestCase):
    def setUp(self):
        self.player2 = Player("Lev", 10)
        self.deck = DeckOfCards()
        self.player2.set_hand(self.deck)

    def test_get_card_core(self):
        # Test Core Functionality block
        chosen_card = get_card_core(self.player2)
        self.assertEqual(len(self.player2.card_deck), 9)
        self.assertNotIn(chosen_card, self.player2.card_deck)

    def test_get_card_boundary(self):
        # Test Boundary Conditions and Edge Cases block
        self.player2.card_deck.clear()  # Empty the deck to test boundary condition
        with self.assertRaises(ValueError):
            get_card_boundary(self.player2)

    def test_get_card_error_handling(self):
        # Test Error Handling block
        with self.assertRaises(TypeError):
            get_card_error_handling(None)
        with self.assertRaises(TypeError):
            get_card_error_handling(Player("Invalid", 10))

    def test_get_card_integration(self):
        # Test Integration block (full integration)
        chosen_card = get_card_integration(self.player2)
        self.assertEqual(len(self.player2.card_deck), 9)
        self.assertNotIn(chosen_card, self.player2.card_deck)
