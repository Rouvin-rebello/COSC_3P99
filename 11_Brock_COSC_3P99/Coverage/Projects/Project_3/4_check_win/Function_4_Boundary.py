# Function_4_Boundary.py

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
    lines = board.rows + board.columns + board.diagonals
    for line in lines:
        if len(set(line)) == 1 and line[0] != ' ':
            return True
    return False
