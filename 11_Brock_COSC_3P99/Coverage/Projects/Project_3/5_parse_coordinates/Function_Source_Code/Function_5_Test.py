# Function_5_Test.py
import unittest
from Function_5_Source import Board, parse_coordinates

class ParseCoordinatesTest(unittest.TestCase):

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
