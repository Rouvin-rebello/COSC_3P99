def play_game_ui(game, rounds):
    for _ in range(rounds):
        card1 = game.player1.get_card()
        card2 = game.player2.get_card()
        print(f"Player {game.player1.player_name} Threw {card1}, Player {game.player2.player_name} Threw {card2}")

        if card1 > card2:
            print(f"Player {game.player1.player_name} Won this round")
        else:
            print(f"Player {game.player2.player_name} Won this round")

        print(f"Player {game.player1.player_name} has {len(game.player1.card_deck)} cards")
        print(f"Player {game.player2.player_name} has {len(game.player2.card_deck)} cards")
