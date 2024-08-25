import unittest
from Function_3_Source import compare

class CompareFunctionTests(unittest.TestCase):
    def test_compare_function(self):
        self.assertEqual(compare(12, 12), "It's a draw")
        self.assertEqual(compare(0, 13), "You win with a BlackJack")
        self.assertEqual(compare(19, 0), "Your opponent wins with a BlackJack")
        self.assertEqual(compare(22, 17), "You went over. You lose!")
        self.assertEqual(compare(18, 25), "You win! Opponent went over.")
        self.assertEqual(compare(20, 17), "You win")
        self.assertEqual(compare(16, 19), "You lose")

    def test_compare_type_error(self):
        with self.assertRaises(TypeError):
            compare("Dsa", 2)

if __name__ == '__main__':
    unittest.main()
