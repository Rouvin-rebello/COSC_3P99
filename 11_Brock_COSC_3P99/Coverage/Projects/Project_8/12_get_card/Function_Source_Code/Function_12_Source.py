from random import randint
from DeckOfCards import DeckOfCards
from Card import Card


class Player:
    def __init__(self, player_name, number_of_card):
        if type(player_name) != str:
            raise TypeError("Name must be a string")
        if type(number_of_card) != int:
            raise TypeError("Number of card must be of type integer")

        self.player_name = player_name
        self.card_deck = []
        self.number_of_card = number_of_card

        if self.number_of_card < 10 or self.number_of_card > 26:
            self.number_of_card = 26

    def set_hand(self, deck: DeckOfCards):
        if type(deck) != DeckOfCards:
            raise TypeError("deck must be of class type DeckOfCards!")
        for i in range(self.number_of_card):
            if len(deck.deck_of_cards) == 0:
                raise ValueError("Deck is empty, can't give out any more cards")
            card = deck.deal_one()
            if card in self.card_deck:
                raise ValueError("Card cannot be duplicated")
            self.card_deck.append(card)

    def get_card(self):
        random_card_index = randint(0, len(self.card_deck) - 1)
        chosen_card = self.card_deck.pop(random_card_index)
        return chosen_card

    def add_card(self, card: Card):
        if type(card) != Card:
            raise TypeError("Deck type must be of type Card")
        if card not in self.card_deck:
            self.card_deck.append(card)
        else:
            raise ValueError("Card already in the deck")

    def __str__(self):
        return f"Player name: {self.player_name}, Player number of cards is {self.number_of_card}"

    def __repr__(self):
        return f"Player {self.player_name} with {self.number_of_card} cards"
