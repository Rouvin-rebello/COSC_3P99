from Card import Card

def add_card_error_handling(player, card):
    if not isinstance(card, Card):
        raise TypeError("Deck type must be of type Card")
    return player
