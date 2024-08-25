# File: Function_Boundary_Conditions.py

from DeckOfCards import DeckOfCards
from Player import Player

class CardGame:
    def __init__(self, player_name1: str, player_name2: str, player_cards: int):
        self.deck = DeckOfCards()
        self.player1 = Player(player_name1, player_cards)
        self.player2 = Player(player_name2, player_cards)
        self.new_game()

    # Boundary conditions: check if a new game is already in progress
    def new_game(self):
        if len(self.player1.card_deck) > 0 or len(self.player2.card_deck) > 0:
            raise ValueError("Can't start a new game, game is already started :(")
        self.deck.cards_shuffle()
        self.player1.set_hand(self.deck)
        self.player2.set_hand(self.deck)
