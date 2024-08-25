from unittest import TestCase
from Card import Card


class TestCard(TestCase):
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

    def test_gt_method_valid(self):
        # Create two cards and see if one is indeed greater than other
        card1 = Card(5, 1)
        card2 = Card(3, 1)
        self.assertTrue(card1 > card2)
        # Check if Ace is indeed the highest value card
        card1 = Card(1, 4)
        card2 = Card(13, 4)
        self.assertTrue(card1 > card2)
        # Check what happens if both of the cards values are equal, the card with the higher suit should be greater
        card1 = Card(4, 3)
        card2 = Card(4, 4)
        self.assertTrue(card1 < card2)

    def test_gt_method_invalid(self):
        # Checks if error raises when comparing card to type that is not of class:Card
        # comparing to type of None, expecting an error
        with self.assertRaises(TypeError):
            self.card > None
        # comparing to type of string, expecting an error
        with self.assertRaises(TypeError):
            self.card > "j"
        # comparing to type of int, expecting an error
        with self.assertRaises(TypeError):
            self.card > 6












