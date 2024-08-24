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



class TestPlayerAddCard(TestCase):
    def setUp(self):
        self.player = Player("Lev", 10)

    def test_add_card_valid(self):
        card = Card(13, 4)
        self.player.add_card(card)
        self.assertEqual(len(self.player.card_deck), 1)
        self.assertIn(card, self.player.card_deck)

    def test_add_card_valid_multiple(self):
        card1 = Card(1, 3)
        card2 = Card(3, 1)
        self.player.add_card(card1)
        self.player.add_card(card2)
        self.assertEqual(len(self.player.card_deck), 2)
        self.assertIn(card1, self.player.card_deck)
        self.assertIn(card2, self.player.card_deck)

    def test_add_card_invalid_type(self):
        with self.assertRaises(TypeError):
            self.player.add_card("abc")
        with self.assertRaises(TypeError):
            self.player.add_card(123)
        with self.assertRaises(TypeError):
            self.player.add_card(None)

    def test_add_card_duplicate(self):
        card = Card(13, 4)
        self.player.add_card(card)
        with self.assertRaises(ValueError):
            self.player.add_card(card)
