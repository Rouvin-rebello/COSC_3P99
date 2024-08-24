# Function_6_UI.py

import itertools
from Function_6_Core import Board, parse_coordinates, update_board, check_win

def play():
    board = Board()
    players = itertools.cycle(['X', 'O'])
    for x in range(9):
        player = next(players)
        print(board)
        print('Player-{} please enter the coordinates for your move'.format(player))
        while True:
            try:
                input_coordinates = input()
                coordinates = parse_coordinates(input_coordinates, board)
            except (ValueError, IndexError, KeyError):
                print('The coordinates you entered are not valid. Re-enter.')
                continue
            break
        update_board(board, player, coordinates)
        if x > 5 and check_win(board):
            print('Player-{} won!'.format(player))
            return
    print('The game ended in a draw')

if __name__ == '__main__':
    play()
