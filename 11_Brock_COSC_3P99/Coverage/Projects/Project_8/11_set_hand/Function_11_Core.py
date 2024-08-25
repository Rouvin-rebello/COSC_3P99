from DeckOfCards import DeckOfCards

def set_hand_core(player, deck):
    for i in range(player.number_of_card):
        card = deck.deal_one()
        player.card_deck.append(card)
    return player
