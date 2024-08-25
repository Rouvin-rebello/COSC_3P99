# Import necessary functions
from Function_4_Core_Functionality import calculation_total, deal_card

def error_handling_game_play(get_user_input=input):
    print("Error Handling Test")

    player_hand = []
    computer_hand = []

    for _ in range(2):
        player_hand.append(deal_card())
        computer_hand.append(deal_card())

    is_game_over = False
    while not is_game_over:
        try:
            total_player = calculation_total(player_hand)
            total_computer = calculation_total(computer_hand)
        except TypeError:
            raise ValueError("Error in calculation_total function")

        print(f"    Your hand: {player_hand} Total score: {total_player}.")
        print(f"    Computer's first card: {computer_hand[0]}")

        if total_player == 0 or total_computer == 0 or total_player > 21:
            is_game_over = True
        else:
            user_input = get_user_input("Do you want to take another card? Type 'y' or 'n'.")
            if user_input not in ['y', 'n']:
                raise ValueError("Invalid input provided")
            if user_input == 'y':
                player_hand.append(deal_card())
            else:
                is_game_over = True

    while total_computer <= 17 and total_computer != 0:
        computer_hand.append(deal_card())
        total_computer = calculation_total(computer_hand)

    print(f"    Your final hand is: {player_hand} Total score: {total_player}")
    print(f"    Computer's final score: {computer_hand} Total score: {total_computer}")

    return total_player, total_computer
