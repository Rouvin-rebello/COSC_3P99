from unittest import TestCase
from Function_7_Source import CardGame

class MockPlayer:
    def __init__(self, player_name, card_deck):
        self.player_name = player_name
        self.card_deck = card_deck

class TestCardGame(TestCase):
    def setUp(self):
        self.player1 = MockPlayer("Yan", [1, 2, 3])
        self.player2 = MockPlayer("Lev", [4, 5, 6, 7])
        self.game = CardGame(self.player1, self.player2, None)

    def test_get_winner_valid_player1_won(self):
        self.player1.card_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.player2.card_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(self.game.get_winner(), "Yan")

    def test_get_winner_valid_player2_won(self):
        self.player1.card_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.player2.card_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(self.game.get_winner(), "Lev")

    def test_get_winner_valid_tie(self):
        self.player1.card_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.player2.card_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(self.game.get_winner(), None)
