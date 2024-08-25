from random import *


class Card:
    # Card value is "Ace, 2,3,4,5..."Jack", "Queen", "King"
    # Card Suit is "Diamond","Spade","Heart","Club"...
    # When Card value and card suit is not type(int) - Error
    # When Card value higher than 13 or lower than 1 - Error
    # When Card Suit higher than 4 and lower than 1 - Error
    def __init__(self, card_value: int, card_suit: int):
        # when card value and/or card suit is not integer, error will appear
        if type(card_value) != int:
            raise TypeError("card_value can only receive int")
        if type(card_suit) != int:
            raise TypeError("card_value can only receive int")
        if card_value > 13 or card_value < 1:
            raise ValueError("Card value must be between 1-13.")
        if card_suit > 4 or card_suit < 1:
            raise ValueError("card suit must be between 1-4.")
        self.card_value = card_value
        self.card_suit = card_suit

    # Str - shows the value and the suit of the card
    def __str__(self):
        values = {1: "Ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "Jack",
                    12: "Queen", 13: "King"}
        suit = {1: "Diamond", 2: "Spade", 3: "Heart", 4: "Club"}
        return f"{values[self.card_value]} of {suit[self.card_suit]}"

    # repr - shows the value and the suit of the card
    def __repr__(self):
        values = {1: "Ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "Jack",
                  12: "Queen", 13: "King"}
        suit = {1: "Diamond", 2: "Spade", 3: "Heart", 4: "Club"}
        return f"{values[self.card_value]} of {suit[self.card_suit]}"

    # gt - True means Self.card_value and/or self.card_suit is higher than other.card_value and/or other.card_suit
    # gt - False means Self.card_value and/or self.card_suit is Lower than other.card_value and/or other.card_suit
    # Ace(1) is the highest value of them all
    # Means if self is Ace and other is Ace, the method checks The suits of the cards
    # If the cards have different values the card with the highest value wins
    # If the Cards have the same Values, The Method checks the cards suits, and the highest suit wins
    def __gt__(self, other):
        if type(other) != Card:
            raise TypeError("other must be of type Card")
        if self.card_value == 1 and other.card_value != 1:
            return True
        elif self.card_value != 1 and other.card_value == 1:
            return False
        elif self.card_value > other.card_value:
            return True
        elif self.card_value < other.card_value:
            return False
        elif self.card_value == other.card_value:
            if self.card_suit > other.card_suit:
                return True
            else:
                return False

    def __eq__(self, other):
        if type(other) != Card:
            raise TypeError("other must be of type Card")
        elif self.card_value == other.card_value and self.card_suit == other.card_suit:
            return True
        else:
            return False


class CardGame:
    # Gets the names and the number of cards in players decks of 2 players
    # Makes the Main Deck
    # Makes 2 players
    # Start a new game(method: New game), that gives each player his deck of cards
    # players names must be of type str!
    # and cant contain numbers or no letters
    # players numbers of cards must be type int!
    # palyers names cant be identical
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

    # If game is already started - gets error
    # starts a new game - shuffles the main deck and gives each player his cards
    def new_game(self):
        # If game is already started - gets error
        # starts a new game - shuffles the main deck and gives each player his cards
        if len(self.player1.card_deck) > 0 or len(self.player2.card_deck) > 0:
            raise ValueError("Cant start a new game, game is already started :(")
        self.deck.cards_shuffle()
        self.player1.set_hand(self.deck)
        self.player2.set_hand(self.deck)

    # Defines the winner of the game, returns the name of the winner, if tie returns None
    def get_winner(self):
        if len(self.player1.card_deck) > len(self.player2.card_deck):
            return self.player1.player_name
        elif len(self.player1.card_deck) < len(self.player2.card_deck):
            return self.player2.player_name
        elif len(self.player1.card_deck) == len(self.player2.card_deck):
            return None

    # str - returns players names and their cards in their decks
    def __str__(self):
        return f"{self.player1},{self.player1.card_deck}\n{self.player2},{self.player2.card_deck}"




class DeckOfCards:
    # Gets 13 cards of Diamonds
    # Gets 13 cards of Spade
    # Gets 13 cards of Heart
    # Gets 13 cards of Club
    # appends/adds them to the Deck(self.deck_of_Cards) - means 52 Cards in the Deck(List)
    def __init__(self):
        self.deck_of_cards = []
        cards_diamond = [Card(i+1, 1) for i in range(13)]
        for cards in cards_diamond:
            self.deck_of_cards.append(cards)
        cards_spade = [Card(i+1, 2) for i in range(13)]
        for cards in cards_spade:
            self.deck_of_cards.append(cards)
        cards_heart = [Card(i+1, 3) for i in range(13)]
        for cards in cards_heart:
            self.deck_of_cards.append(cards)
        cards_club = [Card(i+1, 4) for i in range(13)]
        for cards in cards_club:
            self.deck_of_cards.append(cards)

    # Shuffles the Deck of cards - Randoms the Places in the Deck(Type: List)
    def cards_shuffle(self):
        shuffle(self.deck_of_cards)

    # Picks a random card in the Deck And Pops/Deletes it from the Deck(The List), Returns the Card - (Value and Suit)
    def deal_one(self):
        for cards in self.deck_of_cards:
            random_card = randint(0, len(self.deck_of_cards)-1)
            the_card = self.deck_of_cards[random_card]
            self.deck_of_cards.pop(random_card)
            return the_card

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



name1 = "Bob"
name2 = "Stuart"
game = CardGame(name1, name2, 10)
print(game)
print()
for i in range(10):
    card1 = game.player1.get_card()
    card2 = game.player2.get_card()
    if card1 > card2:
        game.player1.card_deck.append(card1)
        game.player1.card_deck.append(card2)
        print(f"Player {game.player1.player_name} Threw {card1}, Player {game.player2.player_name} Threw {card2}\n"
              f"Player {game.player1.player_name} Won this round")
        print(f"Player {game.player1.player_name} with {len(game.player1.card_deck)} cards")
        print(f"Player {game.player2.player_name} with {len(game.player2.card_deck)} cards\n")


    else:
        game.player2.card_deck.append(card1)
        game.player2.card_deck.append(card2)
        print(f"Player {game.player1.player_name} Threw {card1}, Player {game.player2.player_name} Threw {card2}\n"
              f"Player {game.player2.player_name} Won this round")
        print(f"Player {game.player1.player_name} with {len(game.player1.card_deck)} cards")
        print(f"Player {game.player2.player_name} with {len(game.player2.card_deck)} cards\n")

print()
if game.get_winner() == game.player1.player_name:
    print(f"Player {game.player1.player_name} Won")
elif game.get_winner() == game.player2.player_name:
    print(f"Player {game.player2.player_name} Won")
elif game.get_winner() == None:
    print(f"This is a tie :)")