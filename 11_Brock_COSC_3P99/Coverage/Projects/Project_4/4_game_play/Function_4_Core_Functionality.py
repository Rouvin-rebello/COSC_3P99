# Import necessary functions
from Function_4_Source import deal_card
from Function_4_Test import calculation_total

def core_game_play(get_user_input=input, deal_card_fn=deal_card, calc_total_fn=calculation_total):
    player_hand = []
    computer_hand = []

    for _ in range(2):
        player_hand.append(deal_card_fn())
        computer_hand.append(deal_card_fn())

    is_game_over = False
    while not is_game_over:
        total_player = calc_total_fn(player_hand)
        total_computer = calc_total_fn(computer_hand)
        print(f"    Your hand: {player_hand} Total score: {total_player}.")
        print(f"    Computer's first card: {computer_hand[0]}")

        if total_player == 0 or total_computer == 0 or total_player > 21:
            is_game_over = True
        else:
            user_input = get_user_input("Do you want to take another card? Type 'y' or 'n'.")
            if user_input not in ['y', 'n']:
                raise ValueError("Invalid input provided")
            if user_input == 'y':
                player_hand.append(deal_card_fn())
            else:
                is_game_over = True

    while total_computer <= 17 and total_computer != 0:
        computer_hand.append(deal_card_fn())
        total_computer = calc_total_fn(computer_hand)

    print(f"    Your final hand is: {player_hand} Total score: {total_player}")
    print(f"    Computer's final score: {computer_hand} Total score: {total_computer}")

    # Return the correct number of values
    return player_hand, total_player, computer_hand, total_computer
