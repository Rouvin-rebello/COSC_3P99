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
from unittest.mock import patch, MagicMock
from Function_10_Integration import initialize_game
from Function_10_Core import play_game_core
from Function_10_UI import play_game_ui
from Function_10_Output import print_winner
from CardGame import CardGame
from Card import Card

class TestPlayGameBlocks(TestCase):

    def setUp(self):
        self.player1_name = "Yan"
        self.player2_name = "Lev"
        self.rounds = 10
        self.game = initialize_game(self.player1_name, self.player2_name, self.rounds)

    def test_initialize_game(self):
        # Test Integration Points block (initialize_game function)
        game = initialize_game(self.player1_name, self.player2_name, self.rounds)
        self.assertEqual(game.player1.player_name, self.player1_name)
        self.assertEqual(game.player2.player_name, self.player2_name)

    def test_play_game_core(self):
        # Test Core Functionality block (play_game_core function)
        self.game.player1.get_card = MagicMock(side_effect=[Card(2, 1), Card(5, 1)])
        self.game.player2.get_card = MagicMock(side_effect=[Card(1, 2), Card(3, 2)])
        game = play_game_core(self.game, 2)
        self.assertEqual(len(game.player1.card_deck), 4)  # Cards won should reflect the rounds played
        self.assertEqual(len(game.player2.card_deck), 0)  # No cards won

    @patch('builtins.print')
    def test_play_game_ui(self, mock_print):
        # Test UI Interactions block (play_game_ui function)
        play_game_ui(self.game, 2)
        self.assertTrue(mock_print.called)
        self.assertEqual(mock_print.call_count, 8)  # Adjusted for prints in two rounds

    @patch('builtins.print')
    def test_print_winner(self, mock_print):
        # Test Output Consistency block (print_winner function)
        self.game.get_winner = MagicMock(return_value=self.player1_name)
        print_winner(self.game)
        mock_print.assert_called_with(f"Player {self.player1_name} Won")

    def test_validate_input(self):
        # Ensure CardGame or related setup correctly throws errors or handles input
        with self.assertRaises(TypeError):
            initialize_game(None, self.player2_name, self.rounds)
        with self.assertRaises(ValueError):
            initialize_game(self.player1_name, self.player2_name, -1)

