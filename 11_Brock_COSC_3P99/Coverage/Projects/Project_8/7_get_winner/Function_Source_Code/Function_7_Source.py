class CardGame:
    def __init__(self, player1, player2, deck):
        self.player1 = player1
        self.player2 = player2
        self.deck = deck

    # Defines the winner of the game, returns the name of the winner, if tie returns None
    def get_winner(self):
        if len(self.player1.card_deck) > len(self.player2.card_deck):
            return self.player1.player_name
        elif len(self.player1.card_deck) < len(self.player2.card_deck):
            return self.player2.player_name
        elif len(self.player1.card_deck) == len(self.player2.card_deck):
            return None
