try:
    import os
    import sys

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                ''
            )
        )
    )
except:
    raise

import unittest
from Function_3_Core_Functionality import core_compare
from Function_3_Boundary_Edge_Cases import boundary_compare
from Function_3_Error_Handling import error_handling_compare
from Function_3_Integration import integration_compare
from Function_3_Output_Consistency import consistent_compare

class CompareFunctionTests(unittest.TestCase):
    def test_core_compare(self):
        self.assertEqual(core_compare(20, 17), "You win")
        self.assertEqual(core_compare(16, 19), "You lose")

    def test_boundary_compare(self):
        self.assertEqual(boundary_compare(12, 12), "It's a draw")
        self.assertEqual(boundary_compare(0, 13), "You win with a BlackJack")
        self.assertEqual(boundary_compare(19, 0), "Your opponent wins with a BlackJack")
        self.assertEqual(boundary_compare(22, 17), "You went over. You lose!")
        self.assertEqual(boundary_compare(18, 25), "You win! Opponent went over.")

    def test_error_handling_compare(self):
        with self.assertRaises(TypeError):
            error_handling_compare("Dsa", 2)

    def test_consistent_compare(self):
        self.assertEqual(consistent_compare(12, 12), "It's a draw")
        self.assertEqual(consistent_compare(18, 17), "Result is consistent")

if __name__ == '__main__':
    unittest.main()
