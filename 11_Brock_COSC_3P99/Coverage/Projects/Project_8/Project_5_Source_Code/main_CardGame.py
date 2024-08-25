from CardGame import CardGame
from Player import Player
name1 = input("Enter name of the first player: ")
name2 = input("Enter name of the second player: ")
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
