from unittest import TestCase, mock
from Player import Player
from DeckOfCards import DeckOfCards
from Card import Card


class TestPlayer(TestCase):
    def setUp(self):
        self.player1 = Player("Yan", 26)
        self.player2 = Player("Lev", 10)
        self.deck = DeckOfCards()

    def test_player_init_valid(self):
        # Assure that player name is "Yan" as we defined in the setUp method
        self.assertEqual(self.player1.player_name, "Yan")
        # Assure that player number of cards is as we defined in the
        # setUp method, 26 cards, testing the biggest valid number.
        self.assertEqual(self.player1.number_of_card, 26)
        # Assure that player number of cards is as we defined in the setUp method
        # , 10 cards, testing the smallest valid number.
        self.assertEqual(self.player2.number_of_card, 10)
        # Assure that the player's deck is empty.
        self.assertEqual(self.player1.card_deck, [])
        # Assure that if player cards = 9, default number we defined is triggered and the number should be 26.
        player1 = Player("Yan", 9)
        self.assertEqual(self.player1.number_of_card, 26)
        # Assure that if player cards = 27, default number we defined is triggered and the number should be 26.
        player1 = Player("Yan", 27)
        self.assertEqual(player1.number_of_card, 26)
        # Assure that if player cards is a negative number, number is automatic 26.
        player1 = Player("Yan", -500)
        self.assertEqual(player1.number_of_card, 26)


    def test_player_init_invalid(self):
        # Assure that player_name type can only get string as a type
        with self.assertRaises(TypeError):
            player1 = Player(123, 10)
        # Assure that player number of cards can only get integer
        with self.assertRaises(TypeError):
            player1 = Player("Yan", "26")

    def test_set_hand_valid_length(self):
        # Create deck object
        deck = DeckOfCards()
        # Call the set_hand method and set the deck object in it
        self.player2.set_hand(deck)
        # Assert that the length of the players card deck is as we defined = 10
        self.assertEqual(len(self.player2.card_deck), self.player2.number_of_card)

    def test_set_hand_valid_unique(self):
        # Assure that each card is unique
        deck = DeckOfCards()
        self.player1.set_hand(deck)
        for card in self.player1.card_deck:
            self.assertEqual(self.player1.card_deck.count(card), 1)

    def test_set_hand_invalid_TypeErrors(self):
        # Check to see that set_hand can only get DeckOfCards as a type in the parameter, testing with integer.
        with self.assertRaises(TypeError):
            self.player1.set_hand(1,2,3)
        # Check to see that set_hand can only get DeckOfCards as a type in the parameter, testing with string.
        with self.assertRaises(TypeError):
            self.player1.set_hand("1,2,3")
        # Check to see that set_hand can only get DeckOfCards as a type in the parameter, testing with None.
        with self.assertRaises(TypeError):
            self.player1.set_hand(None)
        # Check to see that set_hand can only get DeckOfCards as a type in the parameter, testing with empty parameter.
        with self.assertRaises(TypeError):
            self.player1.set_hand()

    @mock.patch('DeckOfCards.DeckOfCards.deal_one', return_value=Card(3, 3))
    def test_set_hand_invalid_card_is_duplicated(self, mock_deal_one):
        # Check if cards can be duplicated, expecting an error.
        with self.assertRaises(ValueError):
            self.player2.set_hand(self.deck)


    @mock.patch('DeckOfCards.DeckOfCards.deal_one', return_value=None)
    def test_set_hand_invalid_card_is_None(self, mock_deal_one):
        # Check if cards can be Type None, expecting an error.
        with self.assertRaises(ValueError):
            self.player2.set_hand(self.deck)

    def test_set_hand_deck_is_empty(self):
        # Creating 3 players, when giving out cards to the third person,
        # the cards in deck should be empty before finishing
        player1 = Player("Yan", 26)
        player2 = Player("Yan", 11)
        player3 = Player("Yan", 16)
        with self.assertRaises(ValueError):
            print(len(self.deck.deck_of_cards))
            player1.set_hand(self.deck)
            print(len(self.deck.deck_of_cards))
            player2.set_hand(self.deck)
            print(len(self.deck.deck_of_cards))
            player3.set_hand(self.deck)
            print(len(self.deck.deck_of_cards))


    def test_get_card_valid(self):
        # Use the deck instance from the setUp method
        self.player2.set_hand(self.deck)
        # First, assure that the deck length is 10 as we defined at setUp.
        self.assertEqual(len(self.player2.card_deck), 10)
        # Secondly, we use get card method that pops one card out of the player's deck,
        # and we assure that the length is 9.
        chosen_card = self.player2.get_card()
        self.assertEqual(len(self.player2.card_deck), 9)
        # Assert that the card that was popped is not in the deck anymore.
        self.assertNotIn(chosen_card, self.player2.card_deck)

    def test_add_card_valid(self):
        # Use the deck instance from the setUp method, Player 2 will have 10 cards in his deck.
        self.player2.set_hand(self.deck)
        # Activate the add card method, one card is added to the player's deck
        self.player2.add_card(Card(13, 4))
        # Check that the player's number of cards in the deck is up by 1, cards in deck = 11.
        self.assertEqual(len(self.player2.card_deck), 11)

    def test_add_card_valid_2(self):
        # Use the deck instance from the setUp method
        self.player2.card_deck = []  # Player 2 will have 0 cards in his deck
        # Activate the add card method, with made up card
        card = Card(1, 3)
        self.player2.add_card(card)  # Player 2 will receive 1 card.
        # Check that the players number of cards in the deck is up by 1, 1 card in his deck.
        self.assertEqual(len(self.player2.card_deck), 1)
        self.assertIn(card, self.player2.card_deck)
        # add another card
        card2 = Card(3, 1)
        self.player2.add_card(card2)
        # Check that the players number of cards in the deck is up by 1, 2 card in his deck.
        self.assertEqual(len(self.player2.card_deck), 2)
        self.assertIn(card2, self.player2.card_deck)


    def test_add_card_invalid(self):
        # Activate the add method, with a string, expected result = Error massage
        with self.assertRaises(TypeError):
            self.player2.add_card("abc")
        # Activate the add method, with a Int, expected result = Error massage
        with self.assertRaises(TypeError):
            self.player2.add_card(123)
        # Activate the add method, with a None, expected result = Error massage
        with self.assertRaises(TypeError):
            self.player2.add_card(None)






















