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

class TestCardEqMethod(unittest.TestCase):
    def setUp(self):
        # Core Functionality
        self.card_core = CoreCard(13, 4)
        self.card2_core = CoreCard(1, 1)
        self.card3_core = CoreCard(13, 4)

        # Boundary Conditions and Edge Cases
        self.card_boundary = BoundaryCard(13, 4)
        self.card2_boundary = BoundaryCard(1, 1)
        self.card3_boundary = BoundaryCard(13, 4)

        # Error Handling
        self.card_error = ErrorCard(13, 4)
        self.card2_error = ErrorCard(1, 1)

        # Output Consistency
        self.card_output = OutputCard(13, 4)
        self.card2_output = OutputCard(1, 1)
        self.card3_output = OutputCard(13, 4)

    # Testing Core Functionality
    def test_eq_core_functionality(self):
        # Test if two identical cards are equal
        self.assertTrue(self.card_core == self.card3_core)
        # Test if two different cards are not equal
        self.assertFalse(self.card_core == self.card2_core)

    # Testing Boundary Conditions and Edge Cases
    def test_eq_boundary_conditions(self):
        # Test if two identical cards are equal
        self.assertTrue(self.card_boundary == self.card3_boundary)
        # Test if two different cards are not equal
        self.assertFalse(self.card_boundary == self.card2_boundary)

    # Testing Error Handling
    def test_eq_error_handling(self):
        # Test if the equality method raises an error for a non-Card type
        with self.assertRaises(TypeError):
            self.card_error == "some string"
        with self.assertRaises(TypeError):
            self.card_error == 5

    # Testing Output Consistency
    def test_eq_output_consistency(self):
        # Test if two identical cards are equal (consistent result)
        self.assertTrue(self.card_output == self.card3_output)
        # Test if two different cards are not equal (consistent result)
        self.assertFalse(self.card_output == self.card2_output)

if __name__ == '__main__':
    unittest.main()
