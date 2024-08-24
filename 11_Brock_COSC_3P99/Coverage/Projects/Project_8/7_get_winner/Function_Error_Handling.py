# File: Function_Error_Handling.py

class CardGame:
    def __init__(self, player1, player2, deck):
        if not hasattr(player1, 'card_deck') or not hasattr(player2, 'card_deck'):
            raise ValueError("Invalid player data")
        self.player1 = player1
        self.player2 = player2
        self.deck = deck

    # Error handling: Validate input data before determining the winner
    def get_winner(self):
        if len(self.player1.card_deck) > len(self.player2.card_deck):
            return self.player1.player_name
        elif len(self.player1.card_deck) < len(self.player2.card_deck):
            return self.player2.player_name
        else:
            return None
