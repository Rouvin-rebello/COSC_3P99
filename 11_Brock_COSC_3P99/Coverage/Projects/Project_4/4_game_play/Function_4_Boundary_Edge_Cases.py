# Import the necessary functions from their respective modules
from Function_4_Core_Functionality import calculation_total
from Function_4_Core_Functionality import deal_card


def boundary_game_play(calc_total_fn=calculation_total, deal_card_fn=deal_card, player_hand=None, computer_hand=None):
    if player_hand is None:
        player_hand = []
    if computer_hand is None:
        computer_hand = []

    total_player = calc_total_fn(player_hand)
    total_computer = calc_total_fn(computer_hand)

    while total_computer <= 17 and total_computer != 0:
        computer_hand.append(deal_card_fn())
        total_computer = calc_total_fn(computer_hand)

    return total_player, total_computer
