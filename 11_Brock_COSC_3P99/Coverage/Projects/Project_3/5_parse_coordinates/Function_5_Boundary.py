# Function_5_Boundary.py

class Board(object):
    def __init__(self):
        self.rows = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def parse_coordinates(input_coordinates, board):
    letters_to_numbers = {'a': 0, 'b': 1, 'c': 2}

    try:
        coordinates = (int(input_coordinates[0]), letters_to_numbers[input_coordinates[1]])
    except (ValueError, KeyError):
        coordinates = (int(input_coordinates[1]), letters_to_numbers[input_coordinates[0]])

    return coordinates
