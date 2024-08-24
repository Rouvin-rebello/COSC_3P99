# Function_3_Performance.py

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
    # Performance: ensure the function is O(1) for updating the board
