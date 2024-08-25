def consistent_compare(player_hand, computer_hand):
    """Ensures consistent output when comparing hands"""
    if player_hand == computer_hand:
        return "It's a draw"
    return "Result is consistent"
