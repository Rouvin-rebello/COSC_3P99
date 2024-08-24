from DeckOfCards import DeckOfCards


def set_hand_error_handling(player, deck):
    if not isinstance(deck, DeckOfCards):
        raise TypeError("deck must be of class type DeckOfCards!")

    for i in range(player.number_of_card):
        card = deck.deal_one()
        if card in player.card_deck:
            raise ValueError("card cannot be duplicated")
        if card is None:
            raise ValueError("Cannot deal None as a card")
    return player
