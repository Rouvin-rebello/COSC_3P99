from CardGame import CardGame

def play_game_core(game, rounds):
    for _ in range(rounds):
        card1 = game.player1.get_card()
        card2 = game.player2.get_card()

        if card1 > card2:
            game.player1.card_deck.extend([card1, card2])
        else:
            game.player2.card_deck.extend([card1, card2])

    return game
