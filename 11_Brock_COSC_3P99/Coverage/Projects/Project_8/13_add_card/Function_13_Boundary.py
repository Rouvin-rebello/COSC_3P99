def add_card_boundary(player, card):
    if card in player.card_deck:
        raise ValueError("Card already in the deck")
    return player
