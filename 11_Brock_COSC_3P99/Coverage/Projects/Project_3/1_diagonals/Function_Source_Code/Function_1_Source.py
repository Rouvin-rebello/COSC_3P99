class Board(object):
    def __init__(self):
        self.rows = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    @property
    def diagonals(self):
        return [[self.rows[0][0], self.rows[1][1], self.rows[2][2]],
                [self.rows[0][2], self.rows[1][1], self.rows[2][0]]]
