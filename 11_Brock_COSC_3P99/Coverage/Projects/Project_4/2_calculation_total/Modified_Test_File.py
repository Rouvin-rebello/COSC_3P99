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
from Function_2_Core_Functionality import core_calculation_total
from Function_2_Boundary_Edge_Cases import boundary_calculation_total
from Function_2_Error_Handling import error_handling_calculation_total
from Function_2_Integration import integration_calculation_total
from Function_2_Output_Consistency import consistent_calculation_total

class CalculationTotalTests(unittest.TestCase):
    def test_core_calculation_total_sum(self):
        self.assertEqual(core_calculation_total([5, 4, 3]), 12)

    def test_boundary_calculation_total_first_case(self):
        self.assertEqual(boundary_calculation_total([11, 10]), 0)

    def test_boundary_calculation_total_second_case(self):
        self.assertEqual(boundary_calculation_total([3, 5, 7, 11]), 16)

    def test_error_handling_calculation_total_error_case_one(self):
        with self.assertRaises(TypeError):
            error_handling_calculation_total("21321")

    def test_error_handling_calculation_total_error_case_two(self):
        with self.assertRaises(TypeError):
            error_handling_calculation_total([12, 3, "Hello", 2])

    def test_consistent_calculation_total_output(self):
        self.assertEqual(consistent_calculation_total([5, 11, 6]), 12)

if __name__ == '__main__':
    unittest.main()
