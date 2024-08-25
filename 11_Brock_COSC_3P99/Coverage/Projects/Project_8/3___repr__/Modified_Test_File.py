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
from Function_Core_Functionality import Card as CoreCard
from Function_Boundary_Conditions import Card as BoundaryCard
from Function_Output_Consistency import Card as OutputCard
from Function_Error_Handling import Card as ErrorCard

class TestCardReprMethod(unittest.TestCase):
    def setUp(self):
        # Core Functionality
        self.card_core = CoreCard(13, 4)  # King of Club
        self.card2_core = CoreCard(1, 1)  # Ace of Diamond

        # Boundary Conditions and Edge Cases
        self.card_boundary = BoundaryCard(13, 4)
        self.card2_boundary = BoundaryCard(1, 1)

        # Output Consistency
        self.card_output = OutputCard(13, 4)
        self.card2_output = OutputCard(1, 1)

        # Error Handling
        self.card_error = ErrorCard(13, 4)
        self.card2_error = ErrorCard(1, 1)

    # Testing Core Functionality
    def test_repr_core_functionality(self):
        self.assertEqual(repr(self.card_core), "Card(value=13, suit=4)")
        self.assertEqual(repr(self.card2_core), "Card(value=1, suit=1)")

    # Testing Boundary Conditions and Edge Cases
    def test_repr_boundary_conditions(self):
        self.assertEqual(repr(self.card_boundary), "King of Club")
        self.assertEqual(repr(self.card2_boundary), "Ace of Diamond")

    def test_repr_boundary_invalid(self):
        with self.assertRaises(ValueError):
            BoundaryCard(14, 5)

    # Testing Output Consistency
    def test_repr_output_consistency(self):
        self.assertEqual(repr(self.card_output), "King of Club")
        self.assertEqual(repr(self.card2_output), "Ace of Diamond")

    # Testing Error Handling
    def test_repr_error_handling(self):
        self.assertEqual(repr(self.card_error), "King of Club")
        self.assertEqual(repr(self.card2_error), "Ace of Diamond")

    def test_invalid_card_initialization(self):
        with self.assertRaises(TypeError):
            ErrorCard("King", "Club")
        with self.assertRaises(ValueError):
            ErrorCard(14, 5)

if __name__ == "__main__":
    unittest.main()
