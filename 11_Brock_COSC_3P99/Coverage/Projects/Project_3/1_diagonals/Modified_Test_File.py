import unittest
from Core_Functionality import Board as BoardInit
from Output_Consistency import Board as BoardDiagonals

class TestDiagonals(unittest.TestCase):
    def test_board_diagonals(self):
        board = BoardDiagonals()
        board.rows = [['00', '01', '02'],
                      ['10', '11', '12'],
                      ['20', '21', '22']]
        expected_diagonals = [['00', '11', '22'], ['02', '11', '20']]
        self.assertEqual(expected_diagonals, board.diagonals)

    def test_update_board_diagonals(self):
        board = BoardDiagonals()
        board.rows = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
        expected_diagonals = [['X', 'X', 'X'], [' ', 'X', ' ']]
        self.assertEqual(expected_diagonals, board.diagonals)

if __name__ == '__main__':
    unittest.main()
