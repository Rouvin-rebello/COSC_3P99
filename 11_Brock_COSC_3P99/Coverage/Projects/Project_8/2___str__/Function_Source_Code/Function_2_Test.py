# Function_1_Test.py

import unittest
from Function_2_Source import Card

class TestCardStrMethod(unittest.TestCase):
    def setUp(self):
        self.card1 = Card(13, 4)  # King of Club
        self.card2 = Card(1, 1)   # Ace of Diamond

    def test_str_method(self):
        # Check if the string representation is correct
        self.assertEqual(str(self.card1), "King of Club")
        self.assertEqual(str(self.card2), "Ace of Diamond")

    def test_str_method_invalid(self):
        # Test invalid initialization to ensure str is not executed
        with self.assertRaises(ValueError):
            Card(14, 5)

if __name__ == "__main__":
    unittest.main()
