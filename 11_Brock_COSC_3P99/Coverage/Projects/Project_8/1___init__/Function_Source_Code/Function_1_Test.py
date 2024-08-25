import unittest
from Function_1_Source import Card

class TestCardInit(unittest.TestCase):
    def setUp(self):
        self.card = Card(13, 4)
        self.card2 = Card(1, 1)

    def test_init_valid(self):
        # check if card value is indeed 13 in self.card
        self.assertEqual(self.card.card_value, 13)
        # check if card suit is indeed 4 in self.card
        self.assertEqual(self.card.card_suit, 4)
        # check if card value is indeed 1 in self.card2
        self.assertEqual(self.card2.card_value, 1)
        # check if card suit is indeed 1 in self.card2
        self.assertEqual(self.card2.card_suit, 1)

    def test_init_invalid(self):
        # check if card value can get type that is not int
        with self.assertRaises(TypeError):
            card1 = Card("1", 1)
        # check if card suit get type that is not int
        with self.assertRaises(TypeError):
            card1 = Card(1, "1")
        # check if card value can be greater than 13
        with self.assertRaises(ValueError):
            card1 = Card(14, 1)
        # check if card value can be lower than 1
        with self.assertRaises(ValueError):
            card1 = Card(0, 1)
        # check if card suit can be higher than 4
        with self.assertRaises(ValueError):
            card1 = Card(4, 5)
        # check if card suit can be lower than 1
        with self.assertRaises(ValueError):
            card1 = Card(4, 0)

if __name__ == "__main__":
    unittest.main()
