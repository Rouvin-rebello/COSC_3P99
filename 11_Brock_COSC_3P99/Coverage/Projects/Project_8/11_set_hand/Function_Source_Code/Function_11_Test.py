from unittest import TestCase, mock
from Player import Player
from DeckOfCards import DeckOfCards
from Card import Card


class TestPlayer(TestCase):
    def setUp(self):
        self.player1 = Player("Yan", 26)
        self.player2 = Player("Lev", 10)
        self.deck = DeckOfCards()

    def test_set_hand_valid_length(self):
        deck = DeckOfCards()
        self.player2.set_hand(deck)
        self.assertEqual(len(self.player2.card_deck), self.player2.number_of_card)

    def test_set_hand_valid_unique(self):
        deck = DeckOfCards()
        self.player1.set_hand(deck)
        for card in self.player1.card_deck:
            self.assertEqual(self.player1.card_deck.count(card), 1)

    def test_set_hand_invalid_TypeErrors(self):
        with self.assertRaises(TypeError):
            self.player1.set_hand(1, 2, 3)
        with self.assertRaises(TypeError):
            self.player1.set_hand("1, 2, 3")
        with self.assertRaises(TypeError):
            self.player1.set_hand(None)
        with self.assertRaises(TypeError):
            self.player1.set_hand()

    @mock.patch('DeckOfCards.DeckOfCards.deal_one', return_value=Card(3, 3))
    def test_set_hand_invalid_card_is_duplicated(self, mock_deal_one):
        with self.assertRaises(ValueError):
            self.player2.set_hand(self.deck)

    @mock.patch('DeckOfCards.DeckOfCards.deal_one', return_value=None)
    def test_set_hand_invalid_card_is_None(self, mock_deal_one):
        with self.assertRaises(ValueError):
            self.player2.set_hand(self.deck)

    def test_set_hand_deck_is_empty(self):
        player1 = Player("Yan", 26)
        player2 = Player("Yan", 11)
        player3 = Player("Yan", 16)
        with self.assertRaises(ValueError):
            player1.set_hand(self.deck)
            player2.set_hand(self.deck)
            player3.set_hand(self.deck)
