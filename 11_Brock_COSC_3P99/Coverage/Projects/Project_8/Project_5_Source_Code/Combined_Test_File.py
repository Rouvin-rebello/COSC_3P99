from unittest import TestCase, mock
from Combined_Source_File import *



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



class TestCardGame(TestCase):
    def setUp(self):
        self.game = CardGame("Yan", "Lev", 10)
        self.deck = DeckOfCards()

    def test_card_game_init_valid(self):
        # Checks that the player names are according to the setUp method.
        self.assertEqual(self.game.player1.player_name, "Yan")
        self.assertEqual(self.game.player2.player_name, "Lev")
        # Checks that the player's number of cards are as we defined in the setUp method, also checks the smallest possible number.
        self.assertEqual(self.game.player1.number_of_card, 10)
        self.assertEqual(self.game.player2.number_of_card, 10)
        # Check the biggest possible number of cards in a player's deck.
        game = CardGame("Yan", "Lev", 26)
        self.assertEqual(game.player1.number_of_card, 26)
        self.assertEqual(game.player2.number_of_card, 26)
        # Check that a value lower than 26 is being converted automatically to 26.
        game = CardGame("Yan", "Lev", 9)
        self.assertEqual(game.player1.number_of_card, 26)
        self.assertEqual(game.player2.number_of_card, 26)
        # Check that a value higher than 26 is being converted automatically to 26.
        game = CardGame("Yan", "Lev", 27)
        self.assertEqual(game.player1.number_of_card, 26)
        self.assertEqual(game.player2.number_of_card, 26)
        # Check what happens when number of player's cards in deck is negative.
        game = CardGame("Yan", "Lev", -300)
        self.assertEqual(game.player1.number_of_card, 26)
        self.assertEqual(game.player2.number_of_card, 26)

    def test_card_game_init_invalid(self):
        # Assure that player name1 cant get numbers
        with self.assertRaises(TypeError):
            game = CardGame(123, "Lev", 10)
        # Assure that player name2 cant get numbers
        with self.assertRaises(TypeError):
            game = CardGame("Yan", 123, 10)
        # Assure that error is expected when name1 is blank
        with self.assertRaises(ValueError):
            game = CardGame(" ", "Lev", 10)
        # Assure that error is expected when name2 is blank
        with self.assertRaises(ValueError):
            game = CardGame("Lev", " ", 10)
        # Assure that we get an error if number of cards is not int
        with self.assertRaises(TypeError):
            game = CardGame("Lev", "Yan", "10")
        # Assure that we get an error if number of cards is left empty
        with self.assertRaises(TypeError):
            game = CardGame("Lev", "Yan",)
        # Assure that we get an error if name1 is left empty
        with self.assertRaises(TypeError):
            game = CardGame("Yan",10)
        # Assure that we get an error if name2 is left empty
        with self.assertRaises(TypeError):
            game = CardGame("Yan", 10)
        # Expect an error if name1 is type None
        with self.assertRaises(TypeError):
            game = CardGame(None, "Yan", 10)
        # Expect an error if name2 is type None
        with self.assertRaises(TypeError):
            game = CardGame("Yan", None, 10)
        # Assure that names cannot be identical to each other
        with self.assertRaises(ValueError):
            game = CardGame("Lev", "Lev", 10)
        # Get an error if a string with numbers is defined in name1
        with self.assertRaises(ValueError):
            game = CardGame("123", "Lev", 10)
        # Get an error if a string with numbers is defined in name2
        with self.assertRaises(ValueError):
            game = CardGame("Yan", "123", 10)


    def test_new_game_valid(self):
        # Assure that the length of the players deck, should be equal
        self.assertEqual(len(self.game.player1.card_deck), len(self.game.player2.card_deck))


    # Checks if error raises when trying to start a new game, after a game was started, Expecting an Error
    def test_new_game_invalid(self):
        with self.assertRaises(ValueError):
            self.game.new_game()

    def test_get_winner_valid_player1_won(self):
        self.game.player1.card_deck = (Card(1,1),Card(2,1),Card(3,1),Card(4,1),Card(5,1),Card(6,1),Card(7,1),Card(8,1),Card(9,1),Card(10,1))
        self.game.player2.card_deck = (Card(1,2),Card(2,2),Card(3,3),Card(4,2),Card(5,2),Card(6,2),Card(7,2),Card(8,2),Card(9,2))
        self.assertEqual(self.game.get_winner(), "Yan")

    def test_get_winner_valid_player2_won(self):
        self.game.player2.card_deck = (Card(1,1),Card(2,1),Card(3,1),Card(4,1),Card(5,1),Card(6,1),Card(7,1),Card(8,1),Card(9,1),Card(10,1))
        self.game.player1.card_deck = (Card(1,2),Card(2,2),Card(3,3),Card(4,2),Card(5,2),Card(6,2),Card(7,2),Card(8,2),Card(9,2))
        self.assertEqual(self.game.get_winner(), "Lev")

    def test_get_winner_valid_tie(self):
        self.game.player2.card_deck = (Card(1,1),Card(2,1),Card(3,1),Card(4,1),Card(5,1),Card(6,1),Card(7,1),Card(8,1),Card(9,1),Card(10,1))
        self.game.player1.card_deck = (Card(1,2),Card(2,2),Card(3,3),Card(4,2),Card(5,2),Card(6,2),Card(7,2),Card(8,2),Card(9,2),Card(8,4))
        self.assertEqual(self.game.get_winner(), None)

    # def test_get_winner_valid_player2_won(self):
    #     with patch('CardGame.CardGame.get_winner') as mock_player1_deck:
    #         with patch('CardGame.CardGame.get_winner') as mock_player2_deck:
    #             mock_player1_deck.return_value = 19
    #             mock_player2_deck.return_value = 20
    #             self.assertEqual(self.game.get_winner(), "Yan")
    #
    # def test_get_winner_valid_tie(self):
    #     with patch('CardGame.CardGame.get_winner') as mock_player1_deck:
    #         with patch('CardGame.CardGame.get_winner') as mock_player2_deck:
    #             mock_player1_deck.return_value = 20
    #             mock_player2_deck.return_value = 20
    #             self.game.get_winner()
    #


class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck1 = DeckOfCards()
        self.deck2 = DeckOfCards()

    def test_deck_valid(self):
        # check if there are 52 cards in the deck, we compare the length to 52
        self.assertEqual(len(self.deck1.deck_of_cards), 52)
        self.assertEqual(len(self.deck2.deck_of_cards), 52)

    def test_cards_shuffle(self):
        # create two decks and compare their values, assure that the decks are unique
        self.deck2.cards_shuffle()
        print(self.deck1.deck_of_cards)
        print(self.deck2.deck_of_cards)
        for i in range(len(self.deck1.deck_of_cards)):
            # print(self.deck1.deck_of_cards[i])
            # print(self.deck2.deck_of_cards[i])
            if self.assertNotEqual(self.deck1.deck_of_cards[0], self.deck2.deck_of_cards[0]) == AssertionError:
                self.assertNotEqual(self.deck1.deck_of_cards[1], self.deck2.deck_of_cards[1])

    def test_deal_one_valid(self):
        card = self.deck1.deal_one()
        # deal a card, assure that a card is removed from the main deck after calling the method.
        self.assertEqual(len(self.deck1.deck_of_cards), 51)
        # assure that the card that we removed is not in the deck anymore
        self.assertNotIn(card, self.deck1.deck_of_cards)
        # and second time assure that the card is removed
        self.deck1.deal_one()
        self.assertEqual(len(self.deck1.deck_of_cards), 50)
        print(len(self.deck1.deck_of_cards))



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


















