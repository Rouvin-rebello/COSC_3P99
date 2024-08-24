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

import unittest
from Function_4_Core_Functionality import core_game_play
from Function_4_Boundary_Edge_Cases import boundary_game_play
from Function_4_Error_Handling import error_handling_game_play
from Function_4_Integration import integration_game_play
from Function_4_UI_Interactions import ui_game_play

class GamePlayTests(unittest.TestCase):
    def test_core_game_play(self):
        inputs = iter(['y', 'n'])
        player_hand, total_player, computer_hand, total_computer = core_game_play(lambda _: next(inputs))

        # You can add assertions here to validate the values
        self.assertIsInstance(player_hand, list)
        self.assertIsInstance(computer_hand, list)
        self.assertIsInstance(total_player, int)
        self.assertIsInstance(total_computer, int)

    def test_boundary_game_play(self):
        player_hand = [11, 10]  # BlackJack case
        computer_hand = [5, 6]
        total_player, total_computer = boundary_game_play(player_hand=player_hand, computer_hand=computer_hand)
        self.assertEqual(total_player, 0)  # BlackJack check

    def test_error_handling_game_play(self):
        with self.assertRaises(ValueError):
            error_handling_game_play(lambda _: 'invalid_input')

    def test_integration_game_play(self):
        result = integration_game_play(total_player=21, total_computer=17)
        self.assertEqual(result, "You win")

    def test_ui_game_play(self):
        logo = "BlackJack Test"
        ui_game_play(logo, [5, 7], [10, 9], 12, 19)

if __name__ == '__main__':
    unittest.main()
