# File: Function_Test.py

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
from Function_Core_Functionality import CardGame as CoreCardGame
from Function_Boundary_Conditions import CardGame as BoundaryCardGame
from Function_Error_Handling import CardGame as ErrorCardGame
from Function_Integration_Points import CardGame as IntegrationCardGame
from Function_Output_Consistency import CardGame as OutputCardGame

class MockPlayer:
    def __init__(self, player_name, card_deck):
        self.player_name = player_name
        self.card_deck = card_deck

class TestCardGame(unittest.TestCase):
    # Test Core Functionality
    def test_get_winner_core_functionality(self):
        player1 = MockPlayer("Yan", [1, 2, 3])
        player2 = MockPlayer("Lev", [4, 5, 6, 7])
        game = CoreCardGame(player1, player2, None)
        self.assertEqual(game.get_winner(), "Lev")

    # Test Boundary Conditions and Edge Cases
    def test_get_winner_boundary_conditions(self):
        player1 = MockPlayer("Yan", [1, 2, 3, 4])
        player2 = MockPlayer("Lev", [4, 5, 6, 7])
        game = BoundaryCardGame(player1, player2, None)
        self.assertEqual(game.get_winner(), None)

    # Test Error Handling
    def test_get_winner_error_handling(self):
        with self.assertRaises(ValueError):
            ErrorCardGame(None, None, None)

    # Test Integration Points
    def test_get_winner_integration_points(self):
        player1 = MockPlayer("Yan", [1, 2, 3])
        player2 = MockPlayer("Lev", [4, 5, 6, 7])
        game = IntegrationCardGame(player1, player2, None)
        self.assertTrue(game.get_winner(), "Lev")

    # Test Output Consistency
    def test_get_winner_output_consistency(self):
        player1 = MockPlayer("Yan", [1, 2, 3, 4, 5])
        player2 = MockPlayer("Lev", [1, 2, 3])
        game = OutputCardGame(player1, player2, None)
        self.assertEqual(game.get_winner(), "Yan")

if __name__ == '__main__':
    unittest.main()
