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
from unittest.mock import patch
from Function_10_Source import play_game
from CardGame import CardGame
from Card import Card

class TestCardGame(TestCase):
    def setUp(self):
        self.game = CardGame("Yan", "Lev", 10)

    @patch('builtins.input', side_effect=["Yan", "Lev"])
    @patch('Function_10_Source.CardGame')
    def test_game_rounds(self, mock_game, mock_input):
        mock_game_instance = mock_game.return_value
        mock_game_instance.player1.get_card.side_effect = [Card(2, 1), Card(5, 1)]
        mock_game_instance.player2.get_card.side_effect = [Card(1, 2), Card(3, 2)]
        mock_game_instance.get_winner.return_value = "Yan"

        play_game("Yan", "Lev", 2)

        mock_game_instance.player1.get_card.assert_called()
        mock_game_instance.player2.get_card.assert_called()
        self.assertEqual(mock_game_instance.get_winner(), "Yan")

    def test_card_game_init_valid(self):
        self.assertEqual(self.game.player1.player_name, "Yan")
        self.assertEqual(self.game.player2.player_name, "Lev")
        self.assertEqual(self.game.player1.number_of_card, 10)
        self.assertEqual(self.game.player2.number_of_card, 10)

    def test_get_winner_valid(self):
        self.game.player1.card_deck = [Card(1,1), Card(2,1)]
        self.game.player2.card_deck = [Card(1,2)]
        self.assertEqual(self.game.get_winner(), "Yan")
