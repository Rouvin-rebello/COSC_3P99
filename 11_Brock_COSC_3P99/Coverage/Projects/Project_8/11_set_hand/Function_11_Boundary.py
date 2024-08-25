from DeckOfCards import DeckOfCards

def set_hand_boundary(player, deck):
    for i in range(player.number_of_card):
        if len(deck.deck_of_cards) == 0:
            raise ValueError("Deck is empty, can't give out any more cards")
    return player
