def get_card_boundary(player):
    if len(player.card_deck) == 0:
        raise ValueError("Player's deck is empty, cannot draw a card.")
    return player
