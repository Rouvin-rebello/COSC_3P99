from Card import Card


class Player:
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

    def add_card(self, card: Card):
        if type(card) != Card:
            raise TypeError("Deck type must be of type Card")
        if card not in self.card_deck:
            self.card_deck.append(card)
        else:
            raise ValueError("card already in the deck")
