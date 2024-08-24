from CardGame import CardGame


def play_game(name1, name2, rounds):
    game = CardGame(name1, name2, rounds)
    print(game)
    print()

    for i in range(rounds):
        card1 = game.player1.get_card()
        card2 = game.player2.get_card()
        if card1 > card2:
            game.player1.card_deck.append(card1)
            game.player1.card_deck.append(card2)
            print(f"Player {game.player1.player_name} Threw {card1}, Player {game.player2.player_name} Threw {card2}\n"
                  f"Player {game.player1.player_name} Won this round")
        else:
            game.player2.card_deck.append(card1)
            game.player2.card_deck.append(card2)
            print(f"Player {game.player1.player_name} Threw {card1}, Player {game.player2.player_name} Threw {card2}\n"
                  f"Player {game.player2.player_name} Won this round")

        print(f"Player {game.player1.player_name} with {len(game.player1.card_deck)} cards")
        print(f"Player {game.player2.player_name} with {len(game.player2.card_deck)} cards\n")

    winner = game.get_winner()
    if winner == game.player1.player_name:
        print(f"Player {game.player1.player_name} Won")
    elif winner == game.player2.player_name:
        print(f"Player {game.player2.player_name} Won")
    else:
        print("This is a tie :)")
