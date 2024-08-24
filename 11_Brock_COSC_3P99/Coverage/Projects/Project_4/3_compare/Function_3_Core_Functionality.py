def core_compare(player_hand, computer_hand):
    """Core functionality to compare player and computer hands"""
    if player_hand > computer_hand:
        return "You win"
    else:
        return "You lose"
