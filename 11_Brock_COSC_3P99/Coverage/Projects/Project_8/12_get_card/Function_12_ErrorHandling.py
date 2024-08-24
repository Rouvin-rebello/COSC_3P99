def get_card_error_handling(player):
    if player is None or player.card_deck is None:
        raise TypeError("Player or player's deck is not properly initialized.")
    return player
