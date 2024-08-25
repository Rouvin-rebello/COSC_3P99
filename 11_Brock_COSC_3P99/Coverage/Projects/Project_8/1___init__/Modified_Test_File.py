# File: Function_Test.py

import unittest
from Function_Core_Functionality import Card as CoreCard
from Function_Boundary_Conditions import Card as BoundaryCard
from Function_Error_Handling import Card as ErrorCard

class TestCardInit(unittest.TestCase):
    def setUp(self):
        # Core Functionality
        self.card_core = CoreCard(13, 4)
        self.card2_core = CoreCard(1, 1)

        # Boundary Conditions and Edge Cases
        self.card_boundary = BoundaryCard(13, 4)
        self.card2_boundary = BoundaryCard(1, 1)

        # Error Handling
        self.card_error = ErrorCard(13, 4)
        self.card2_error = ErrorCard(1, 1)

    # Testing Core Functionality
    def test_init_core_valid(self):
        self.assertEqual(self.card_core.card_value, 13)
        self.assertEqual(self.card_core.card_suit, 4)

    # Testing Boundary Conditions and Edge Cases
    def test_init_boundary_valid(self):
        self.assertEqual(self.card_boundary.card_value, 13)
        self.assertEqual(self.card_boundary.card_suit, 4)

    def test_init_boundary_invalid(self):
        with self.assertRaises(ValueError):
            BoundaryCard(14, 1)
        with self.assertRaises(ValueError):
            BoundaryCard(0, 1)
        with self.assertRaises(ValueError):
            BoundaryCard(4, 5)
        with self.assertRaises(ValueError):
            BoundaryCard(4, 0)

    # Testing Error Handling
    def test_init_error_invalid(self):
        with self.assertRaises(TypeError):
            ErrorCard("1", 1)
        with self.assertRaises(TypeError):
            ErrorCard(1, "1")
