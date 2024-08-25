from unittest import TestCase, mock
from CardGame import CardGame
from DeckOfCards import DeckOfCards
from Player import Player
from Card import Card
from unittest.mock import patch


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













