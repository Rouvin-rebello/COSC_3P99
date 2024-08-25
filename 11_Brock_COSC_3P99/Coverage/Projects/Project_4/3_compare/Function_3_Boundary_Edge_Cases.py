def boundary_compare(player_hand, computer_hand):
    """Handles boundary conditions for comparing hands"""
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
    return None  # To indicate no boundary condition met
