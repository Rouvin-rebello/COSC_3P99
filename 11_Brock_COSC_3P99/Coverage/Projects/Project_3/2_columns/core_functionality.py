# Core_Functionality.py

class Board(object):
    def __init__(self):
        self.rows = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    @property
    def columns(self):
        return list(map(list, zip(*self.rows)))
