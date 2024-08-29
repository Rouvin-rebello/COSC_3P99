# File: Function_Integration_Points.py

from DeckOfCards import DeckOfCards
from Player import Player

class CardGame:
    def __init__(self, player_name1: str, player_name2: str, player_cards: int):
        self.deck = DeckOfCards()
        self.player1 = Player(player_name1, player_cards)
        self.player2 = Player(player_name2, player_cards)
        self.new_game()

    # Integration points: shuffle and distribute cards to players
    def new_game(self):
        self.deck.cards_shuffle()
        self.player1.set_hand(self.deck)
        self.player2.set_hand(self.deck)