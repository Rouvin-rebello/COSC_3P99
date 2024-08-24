try:
    import os
    import sys

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                ''
            )
        )
    )
except:
    raise

from random import *
from DeckOfCards import DeckOfCards
from Card import Card


class Player:
    # Gets the player name - Type(str)
    # Gets the number of cards that the player have in his deck - Type(int)
    # The Player Deck is empty at the beginning
    # If number_of_cards is higher than 26 the default value is 26
    # If number_of_cards is lower than 10 the default values is 26
    # If number_of_cards is between 10 and 26, the values stays as we defined
    def __init__(self, player_name, number_of_card):
        if type(player_name) != str:
            raise TypeError("Name must be a string")
        if type(number_of_card) != int:
            raise TypeError("number of card must be of type integer")
        self.player_name = player_name
        self.card_deck = []
        self.number_of_card = number_of_card
        if 10 > self.number_of_card:
            self.number_of_card = 26
        if 26 < self.number_of_card:
            self.number_of_card = 26

    # gets The Main Deck as class:DeckOfCards, and appends/adds the cards to the players deck
    # by the method deal_one from the DeckOfCard class
    # The amount of cards that the players receives is the amount we defined at the number_of_cards in this class
    def set_hand(self, deck: DeckOfCards):
        if type(deck) != DeckOfCards:
            raise TypeError("deck must be of class type DeckOfCards!")
        for i in range(self.number_of_card):
            if len(deck.deck_of_cards) == 0:
                raise ValueError("Deck is empty, cant give out anymore cards")
            card = deck.deal_one()
            if card in self.card_deck:
                raise ValueError("card cannot be duplicated")
            # if card == None:
            #     raise TypeError("Chosen card cant be of type None")
            self.card_deck.append(card)


    # Picks a card from the players deck, Returns its Value and suit, and pops/deletes the card from the players deck
    def get_card(self):
        for cards in self.card_deck:
            random_card1 = randint(0, len(self.card_deck) - 1)
            the_card1 = self.card_deck[random_card1]
            self.card_deck.pop(random_card1)
            return the_card1

    # Adds a card from the Main Deck to the players Deck
    def add_card(self, card: Card):
        if type(card) != Card:
            raise TypeError("Deck type must be of type Card")
        if card not in self.card_deck:
            self.card_deck.append(card)
        else:
            raise ValueError("card already in the deck")

    # str - returns players name and his number of cards
    def __str__(self):
        return f"Player name: {self.player_name}, Player number of cards is {self.number_of_card}"

    # repr - returns players name and his number of cards
    def __repr__(self):
        return f"Player {self.player_name} with {self.number_of_card} cards"
