
# File: Function_Output_Consistency.py

class CardGame:
    def __init__(self, player1, player2, deck):
        self.player1 = player1
        self.player2 = player2
        self.deck = deck

    # Output consistency: Ensure consistent results in determining the winner
    def get_winner(self):
        if len(self.player1.card_deck) > len(self.player2.card_deck):
            return self.player1.player_name
        elif len(self.player1.card_deck) < len(self.player2.card_deck):
            return self.player2.player_name
        else:
            return None
