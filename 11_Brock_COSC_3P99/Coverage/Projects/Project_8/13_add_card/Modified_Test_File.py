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
from Card import Card
from Function_13_Core import add_card_core
from Function_13_Boundary import add_card_boundary
from Function_13_ErrorHandling import add_card_error_handling
from Function_13_Integration import add_card_integration


class TestPlayerAddCard(TestCase):
    def setUp(self):
        self.player = Player("Lev", 10)

    def test_add_card_core(self):
        card = Card(13, 4)
        add_card_core(self.player, card)
        self.assertEqual(len(self.player.card_deck), 1)
        self.assertIn(card, self.player.card_deck)

    def test_add_card_boundary(self):
        card = Card(13, 4)
        add_card_core(self.player, card)
        with self.assertRaises(ValueError):
            add_card_boundary(self.player, card)

    def test_add_card_error_handling(self):
        with self.assertRaises(TypeError):
            add_card_error_handling(self.player, "abc")
        with self.assertRaises(TypeError):
            add_card_error_handling(self.player, 123)
        with self.assertRaises(TypeError):
            add_card_error_handling(self.player, None)

    def test_add_card_integration(self):
        card = Card(13, 4)
        add_card_integration(self.player, card)
        self.assertEqual(len(self.player.card_deck), 1)
        self.assertIn(card, self.player.card_deck)
        with self.assertRaises(ValueError):
            add_card_integration(self.player, card)
