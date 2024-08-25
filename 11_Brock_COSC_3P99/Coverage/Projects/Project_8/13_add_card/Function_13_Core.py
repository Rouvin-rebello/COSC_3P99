def add_card_core(player, card):
    if card not in player.card_deck:
        player.card_deck.append(card)
    return player
