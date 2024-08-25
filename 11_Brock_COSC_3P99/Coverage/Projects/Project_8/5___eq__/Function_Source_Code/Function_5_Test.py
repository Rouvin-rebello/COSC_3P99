import unittest
from Function_5_Source import Card

class TestCardEqMethod(unittest.TestCase):
    def setUp(self):
        self.card1 = Card(13, 4)
        self.card2 = Card(1, 1)
        self.card3 = Card(13, 4)

    def test_eq_method_valid(self):
        # Test if two identical cards are equal
        self.assertTrue(self.card1 == self.card3)
        # Test if two different cards are not equal
        self.assertFalse(self.card1 == self.card2)

    def test_eq_method_invalid(self):
        # Test if the equality method raises an error for a non-Card type
        with self.assertRaises(TypeError):
            self.card1 == "some string"
        with self.assertRaises(TypeError):
            self.card1 == 5

if __name__ == '__main__':
    unittest.main()
