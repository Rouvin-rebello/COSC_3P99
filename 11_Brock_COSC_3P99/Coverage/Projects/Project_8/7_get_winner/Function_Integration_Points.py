# File: Function_Integration_Points.py
from Player import Player

class CardGame:
    def __init__(self, player1, player2, deck):
        self.player1 = player1
        self.player2 = player2
        self.deck = deck

    # Integration points: make sure player objects have valid card decks
    def get_winner(self):
        if isinstance(self.player1, Player) and isinstance(self.player2, Player):
            if len(self.player1.card_deck) > len(self.player2.card_deck):
                return self.player1.player_name
            elif len(self.player1.card_deck) < len(self.player2.card_deck):
                return self.player2.player_name
            else:
                return None
