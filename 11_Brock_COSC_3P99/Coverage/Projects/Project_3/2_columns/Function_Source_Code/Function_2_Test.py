# Function_2_Test.py
import unittest
from Function_2_Source import Board

class TestBoardColumns(unittest.TestCase):

    def test_board_columns(self):
        board = Board()
        board.rows = [['00', '01', '02'],
                      ['10', '11', '12'],
                      ['20', '21', '22']]
        expected_columns = [['00', '10', '20'],
                            ['01', '11', '21'],
                            ['02', '12', '22']]
        self.assertEqual(expected_columns, board.columns)

if __name__ == '__main__':
    unittest.main()
