import itertools

class Board(object):
    def __init__(self):
        self.rows = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    @property
    def diagonals(self):
        return [[self.rows[0][0], self.rows[1][1], self.rows[2][2]],
                [self.rows[0][2], self.rows[1][1], self.rows[2][0]]]

    @property
    def columns(self):
        return list(map(list, zip(*self.rows)))

    def __str__(self):
        return "  a b c\n0 {}\n1 {}\n2 {}".format(' '.join(self.rows[0]),
                                                  ' '.join(self.rows[1]),
                                                  ' '.join(self.rows[2]))

def update_board(board, player, coordinates):
    board.rows[coordinates[0]][coordinates[1]] = player

def check_win(board):
    lines = board.rows + board.columns + board.diagonals

    for line in lines:
        if (all(board_position == 'X' for board_position in line) or
           all(board_position == 'O' for board_position in line)):
            return True

def parse_coordinates(input_coordinates, board):
    letters_to_numbers = {'a': 0, 'b': 1, 'c': 2}

    try:
        coordinates = (int(input_coordinates[0]),
                       letters_to_numbers[input_coordinates[1]])
    except (ValueError, KeyError):
        coordinates = (int(input_coordinates[1]),
                       letters_to_numbers[input_coordinates[0]])

    if (coordinates[0] > (len(board.rows) - 1)):
        raise ValueError('Out of bound coordinates')

    if board.rows[coordinates[0]][coordinates[1]] != ' ':
        raise ValueError('Duplicate coordinates')

    return coordinates

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

        if x > 5:
            if check_win(board):
                print('Player-{} won!'.format(player))
                return

    print('The game ended in a draw')

if __name__ == '__main__':
    play()
