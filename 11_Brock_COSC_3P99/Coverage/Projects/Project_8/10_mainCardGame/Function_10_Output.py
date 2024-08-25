def print_winner(game):
    winner = game.get_winner()
    if winner == game.player1.player_name:
        print(f"Player {game.player1.player_name} Won")
    elif winner == game.player2.player_name:
        print(f"Player {game.player2.player_name} Won")
    else:
        print("This is a tie :)")
