# Function_4_Test.py

import unittest
from Function_4_Source import Board, check_win

class CheckWinTest(unittest.TestCase):

    def test_check_column_win(self):
        board = Board()
        board.rows = [['X', ' ', ' '], ['X', ' ', ' '], ['X', ' ', ' ']]
        self.assertTrue(check_win(board))

    def test_check_row_win(self):
        board = Board()
        board.rows = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertTrue(check_win(board))

    def test_check_first_diagonal_win(self):
        board = Board()
        board.rows = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
        self.assertTrue(check_win(board))

    def test_check_second_diagonal_win(self):
        board = Board()
        board.rows = [[' ', ' ', 'X'], [' ', 'X', ' '], ['X', ' ', ' ']]
        self.assertTrue(check_win(board))

if __name__ == '__main__':
    unittest.main()
