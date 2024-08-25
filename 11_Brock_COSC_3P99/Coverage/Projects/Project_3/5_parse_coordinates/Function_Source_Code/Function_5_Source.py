# Function_5_Source.py

class Board(object):
    def __init__(self):
        self.rows = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

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
