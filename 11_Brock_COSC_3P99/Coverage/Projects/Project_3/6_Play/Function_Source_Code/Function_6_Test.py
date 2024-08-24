import unittest
from Function_6_Source import Board, update_board, check_win, parse_coordinates

class TicTacTest(unittest.TestCase):

    def test_board_columns(self):
        board = Board()
        board.rows = [['00', '01', '02'],
                      ['10', '11', '12'],
                      ['20', '21', '22']]
        expected_columns = [['00', '10', '20'],
                            ['01', '11', '21'],
                            ['02', '12', '22']]
        self.assertEqual(expected_columns, board.columns)

    def test_board_diagonals(self):
        board = Board()
        board.rows = [['00', '01', '02'],
                      ['10', '11', '12'],
                      ['20', '21', '22']]
        expected_diagonals = [['00', '11', '22'], ['02', '11', '20']]
        self.assertEqual(expected_diagonals, board.diagonals)

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

    def test_parse_coordinates(self):
        board = Board()
        input_coordinates_1 = '1b'
        input_coordinates_2 = 'b1'
        expected_parsed_coordinates = (1, 1)
        self.assertEqual(expected_parsed_coordinates,
                         parse_coordinates(input_coordinates_1, board))
        self.assertEqual(expected_parsed_coordinates,
                         parse_coordinates(input_coordinates_2, board))

    def test_parse_duplicate_coordinates(self):
        board = Board()
        board.rows = [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertRaises(ValueError, parse_coordinates, '0a', board)

    def test_parse_outofbound_coordinates(self):
        board = Board()
        self.assertRaises(ValueError, parse_coordinates, '0d', board)

if __name__ == '__main__':
    unittest.main()
