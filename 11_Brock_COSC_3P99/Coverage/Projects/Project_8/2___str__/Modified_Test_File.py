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

class TestCardStrMethod(unittest.TestCase):
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

    # Testing Core Functionality
    def test_str_core_functionality(self):
        self.assertEqual(str(self.card_core), "13 of 4")
        self.assertEqual(str(self.card2_core), "1 of 1")

    # Testing Boundary Conditions and Edge Cases
    def test_str_boundary_conditions(self):
        self.assertEqual(str(self.card_boundary), "King of Club")
        self.assertEqual(str(self.card2_boundary), "Ace of Diamond")

    def test_str_boundary_invalid(self):
        with self.assertRaises(ValueError):
            BoundaryCard(14, 5)

    # Testing Output Consistency
    def test_str_output_consistency(self):
        self.assertEqual(str(self.card_output), "King of Club")
        self.assertEqual(str(self.card2_output), "Ace of Diamond")

if __name__ == "__main__":
    unittest.main()
