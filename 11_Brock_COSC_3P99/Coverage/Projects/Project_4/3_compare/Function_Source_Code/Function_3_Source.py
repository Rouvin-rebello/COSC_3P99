def compare(player_hand, computer_hand):
    if type(player_hand) != int or type(computer_hand) != int:
        raise TypeError("Compare function expects only integer values!")

    if player_hand == computer_hand:
        return "It's a draw"
    elif player_hand == 0:
        return "You win with a BlackJack"
    elif computer_hand == 0:
        return "Your opponent wins with a BlackJack"
    elif player_hand > 21:
        return "You went over. You lose!"
    elif computer_hand > 21:
        return "You win! Opponent went over."
    elif player_hand > computer_hand:
        return "You win"
    else:
        return "You lose"
