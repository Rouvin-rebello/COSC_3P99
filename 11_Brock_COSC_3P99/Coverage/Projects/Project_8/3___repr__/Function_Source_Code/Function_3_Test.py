import unittest
from Function_3_Source import Card

class TestCardRepr(unittest.TestCase):
    def setUp(self):
        self.card1 = Card(13, 4)  # King of Club
        self.card2 = Card(1, 1)   # Ace of Diamond

    def test_repr_method(self):
        # Test if __repr__ returns the correct string for card1
        self.assertEqual(repr(self.card1), "King of Club")
        # Test if __repr__ returns the correct string for card2
        self.assertEqual(repr(self.card2), "Ace of Diamond")

if __name__ == '__main__':
    unittest.main()
