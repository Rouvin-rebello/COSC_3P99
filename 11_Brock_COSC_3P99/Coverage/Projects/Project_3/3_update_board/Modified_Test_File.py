# Function_3_Test.py

import unittest
from Function_3_Core import Board, update_board
# or from Function_3_Boundary import Board, update_board
# or from Function_3_ErrorHandling import Board, update_board
# or from Function_3_Integration import Board, update_board
# or from Function_3_Performance import Board, update_board
# or from Function_3_OutputConsistency import Board, update_board


class TicTacTest(unittest.TestCase):

    def test_update_board(self):
        board = Board()
        update_board(board, 'X', (1, 1))
        expected_rows_columns = [[' ', ' ', ' '],
                                 [' ', 'X', ' '],
                                 [' ', ' ', ' ']]
        expected_diagonals = [[' ', 'X', ' '], [' ', 'X', ' ']]
        self.assertEqual(expected_rows_columns, board.columns)
        self.assertEqual(expected_rows_columns, board.rows)
        self.assertEqual(expected_diagonals, board.diagonals)


if __name__ == '__main__':
    unittest.main()
