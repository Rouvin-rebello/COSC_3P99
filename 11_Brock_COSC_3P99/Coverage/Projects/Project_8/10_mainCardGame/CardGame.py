from random import *
from DeckOfCards import DeckOfCards
from Player import Player
class CardGame:
    # Gets the names and the number of cards in players decks of 2 players
    # Makes the Main Deck
    # Makes 2 players
    # Start a new game(method: New game), that gives each player his deck of cards
    # players names must be of type str!
    # and cant contain numbers or no letters
    # players numbers of cards must be type int!
    # palyers names cant be identical
    def __init__(self, player_name1: str, player_name2: str, player_cards: int):
        if type(player_name1) != str:
            raise TypeError("name must be a string")
        if type(player_name2) != str:
            raise TypeError("name must be a string")
        if not player_name1.isalpha():
            raise ValueError("name must have string in it ")
        if not player_name2.isalpha():
            raise ValueError("name must have string in it ")
        if player_name1.isnumeric():
            raise ValueError("name cant have numbers")
        if player_name2.isnumeric():
            raise ValueError("name cant have numbers")
        if player_name1 == player_name2:
            raise ValueError("names cant be identical")
        if type(player_cards) != int:
            raise TypeError("player cards must be int")
        self.deck = DeckOfCards()
        self.player1 = Player(player_name1, player_cards)
        self.player2 = Player(player_name2, player_cards)
        self.new_game()

    # If game is already started - gets error
    # starts a new game - shuffles the main deck and gives each player his cards
    def new_game(self):
        # If game is already started - gets error
        # starts a new game - shuffles the main deck and gives each player his cards
        if len(self.player1.card_deck) > 0 or len(self.player2.card_deck) > 0:
            raise ValueError("Cant start a new game, game is already started :(")
        self.deck.cards_shuffle()
        self.player1.set_hand(self.deck)
        self.player2.set_hand(self.deck)

    # Defines the winner of the game, returns the name of the winner, if tie returns None
    def get_winner(self):
        if len(self.player1.card_deck) > len(self.player2.card_deck):
            return self.player1.player_name
        elif len(self.player1.card_deck) < len(self.player2.card_deck):
            return self.player2.player_name
        elif len(self.player1.card_deck) == len(self.player2.card_deck):
            return None

    # str - returns players names and their cards in their decks
    def __str__(self):
        return f"{self.player1},{self.player1.card_deck}\n{self.player2},{self.player2.card_deck}"



# game = CardGame("Yan",10,"Lev",11)
# print(game.player1.card_deck)
# print(game.player2.card_deck)
# print(game.get_winner())
