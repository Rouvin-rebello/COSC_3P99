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
from Function_Error_Handling import Card as ErrorCard
from Function_Output_Consistency import Card as OutputCard

class TestCardGtMethod(unittest.TestCase):
    def setUp(self):
        # Core Functionality
        self.card_core = CoreCard(13, 4)  # King of Club
        self.card2_core = CoreCard(1, 1)  # Ace of Diamond

        # Boundary Conditions and Edge Cases
        self.card_boundary = BoundaryCard(13, 4)
        self.card2_boundary = BoundaryCard(1, 1)

        # Error Handling
        self.card_error = ErrorCard(13, 4)
        self.card2_error = ErrorCard(1, 1)

        # Output Consistency
        self.card_output = OutputCard(13, 4)
        self.card2_output = OutputCard(1, 1)

    # Testing Core Functionality
    def test_gt_core_functionality(self):
        card1 = CoreCard(5, 1)
        card2 = CoreCard(3, 1)
        self.assertTrue(card1 > card2)

    # Testing Boundary Conditions and Edge Cases
    def test_gt_boundary_conditions(self):
        card1 = BoundaryCard(1, 4)
        card2 = BoundaryCard(13, 4)
        self.assertTrue(card1 > card2)

        card1 = BoundaryCard(4, 3)
        card2 = BoundaryCard(4, 4)
        self.assertTrue(card1 < card2)

    # Testing Error Handling
    def test_gt_error_handling(self):
        with self.assertRaises(TypeError):
            self.card_error > None

        with self.assertRaises(TypeError):
            self.card_error > "j"

    # Testing Output Consistency
    def test_gt_output_consistency(self):
        card1 = OutputCard(4, 3)
        card2 = OutputCard(4, 4)
        self.assertFalse(card1 > card2)

if __name__ == '__main__':
    unittest.main()
