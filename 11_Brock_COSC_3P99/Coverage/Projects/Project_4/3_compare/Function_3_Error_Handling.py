def error_handling_compare(player_hand, computer_hand):
    """Handles errors in comparing hands"""
    if not isinstance(player_hand, int) or not isinstance(computer_hand, int):
        raise TypeError("Compare function expects only integer values!")
