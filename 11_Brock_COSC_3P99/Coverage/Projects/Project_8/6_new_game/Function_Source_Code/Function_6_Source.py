from DeckOfCards import DeckOfCards
from Player import Player

class CardGame:
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

    # Starts a new game: shuffles the deck and gives each player their cards
    def new_game(self):
        if len(self.player1.card_deck) > 0 or len(self.player2.card_deck) > 0:
            raise ValueError("Cant start a new game, game is already started :(")
        self.deck.cards_shuffle()
        self.player1.set_hand(self.deck)
        self.player2.set_hand(self.deck)
