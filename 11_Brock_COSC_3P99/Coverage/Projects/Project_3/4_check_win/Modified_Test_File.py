# Function_4_Test.py

import unittest
# from Function_4_Core import Board, check_win
# from Function_4_Boundary import Board, check_win
# from Function_4_ErrorHandling import Board, check_win
# from Function_4_Integration import Board, check_win
# from Function_4_Performance import Board, check_win
from Function_4_OutputConsistency import Board, check_win

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

    def test_no_win(self):
        board = Board()
        board.rows = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']]
        self.assertFalse(check_win(board))

if __name__ == '__main__':
    unittest.main()
