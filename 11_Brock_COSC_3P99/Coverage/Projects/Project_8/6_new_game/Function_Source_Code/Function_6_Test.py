import unittest
from CardGame import CardGame
from unittest import mock
from unittest.mock import patch

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.game = CardGame("Yan", "Lev", 10)

    def test_new_game_valid(self):
        # Assure that the length of both players' decks is equal
        self.assertEqual(len(self.game.player1.card_deck), len(self.game.player2.card_deck))

    def test_new_game_invalid(self):
        # Expect an error when trying to start a new game after a game has already started
        with self.assertRaises(ValueError):
            self.game.new_game()

if __name__ == '__main__':
    unittest.main()
