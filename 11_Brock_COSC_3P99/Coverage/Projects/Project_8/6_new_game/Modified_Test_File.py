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

class TestCardGame(unittest.TestCase):
    # Test Core Functionality
    def test_new_game_core_functionality(self):
        game = CoreCardGame("Yan", "Lev", 10)
        self.assertEqual(len(game.player1.card_deck), len(game.player2.card_deck))

    # Test Boundary Conditions and Edge Cases
    def test_new_game_boundary_conditions(self):
        game = BoundaryCardGame("Yan", "Lev", 10)
        with self.assertRaises(ValueError):
            game.new_game()

    # Test Error Handling
    def test_new_game_error_handling(self):
        with self.assertRaises(ValueError):
            ErrorCardGame("Yan123", "Lev", 10)
        with self.assertRaises(TypeError):
            ErrorCardGame("Yan", "Lev", "ten")
        with self.assertRaises(ValueError):
            ErrorCardGame("Yan", "Yan", 10)

    # Test Integration Points
    def test_new_game_integration_points(self):
        game = IntegrationCardGame("Yan", "Lev", 10)
        self.assertTrue(hasattr(game.deck, 'cards_shuffle'))
        self.assertTrue(hasattr(game.player1, 'set_hand'))

    # Test Output Consistency
    def test_new_game_output_consistency(self):
        game = OutputCardGame("Yan", "Lev", 10)
        self.assertEqual(len(game.player1.card_deck), 10)
        self.assertEqual(len(game.player2.card_deck), 10)

if __name__ == '__main__':
    unittest.main()
