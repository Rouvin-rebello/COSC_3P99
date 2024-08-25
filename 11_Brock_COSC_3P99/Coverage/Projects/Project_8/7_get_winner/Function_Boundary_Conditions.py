# File: Function_Boundary_Conditions.py

class CardGame:
    def __init__(self, player1, player2, deck):
        self.player1 = player1
        self.player2 = player2
        self.deck = deck

    # Boundary conditions: handle the case where both players have the same number of cards (tie)
    def get_winner(self):
        if len(self.player1.card_deck) == len(self.player2.card_deck):
            return None
        elif len(self.player1.card_deck) > len(self.player2.card_deck):
            return self.player1.player_name
        else:
            return self.player2.player_name
