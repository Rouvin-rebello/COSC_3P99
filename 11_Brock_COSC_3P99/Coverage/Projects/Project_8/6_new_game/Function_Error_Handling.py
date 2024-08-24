# File: Function_Error_Handling.py

from DeckOfCards import DeckOfCards
from Player import Player

class CardGame:
    def __init__(self, player_name1: str, player_name2: str, player_cards: int):
        if type(player_name1) != str:
            raise TypeError("name must be a string")
        if type(player_name2) != str:
            raise TypeError("name must be a string")
        if not player_name1.isalpha():
            raise ValueError("name must have string in it")
        if not player_name2.isalpha():
            raise ValueError("name must have string in it")
        if player_name1 == player_name2:
            raise ValueError("names can't be identical")
        if type(player_cards) != int:
            raise TypeError("player cards must be int")
        self.deck = DeckOfCards()
        self.player1 = Player(player_name1, player_cards)
        self.player2 = Player(player_name2, player_cards)
        self.new_game()
