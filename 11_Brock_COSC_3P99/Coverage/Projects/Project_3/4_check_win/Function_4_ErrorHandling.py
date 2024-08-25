# Function_4_ErrorHandling.py

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


def check_win(board):
    try:
        lines = board.rows + board.columns + board.diagonals
        for line in lines:
            if (all(board_position == 'X' for board_position in line) or
               all(board_position == 'O' for board_position in line)):
                return True
    except Exception as e:
        raise RuntimeError("Error checking win condition") from e
    return False
