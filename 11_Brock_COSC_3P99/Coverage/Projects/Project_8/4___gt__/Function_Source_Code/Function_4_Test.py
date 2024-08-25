# Function_4_Test.py

import unittest
from Function_4_Source import Card

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card(13, 4)
        self.card2 = Card(1, 1)

    def test_gt_method_valid(self):
        card1 = Card(5, 1)
        card2 = Card(3, 1)
        self.assertTrue(card1 > card2)

        card1 = Card(1, 4)
        card2 = Card(13, 4)
        self.assertTrue(card1 > card2)

        card1 = Card(4, 3)
        card2 = Card(4, 4)
        self.assertTrue(card1 < card2)

    def test_gt_method_invalid(self):
        with self.assertRaises(TypeError):
            self.card > None

        with self.assertRaises(TypeError):
            self.card > "j"

        with self.assertRaises(TypeError):
            self.card > 6

if __name__ == '__main__':
    unittest.main()
