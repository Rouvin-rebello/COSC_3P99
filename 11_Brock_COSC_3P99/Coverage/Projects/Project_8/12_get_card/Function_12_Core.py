import random

def get_card_core(player):
    random_card_index = random.randint(0, len(player.card_deck) - 1)
    chosen_card = player.card_deck.pop(random_card_index)
    return chosen_card
