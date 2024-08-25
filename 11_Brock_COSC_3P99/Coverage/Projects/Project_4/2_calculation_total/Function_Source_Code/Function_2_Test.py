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
from Function_2_Source import calculation_total

class CalculationTotalTests(unittest.TestCase):
    def test_calculation_total_sum(self):
        self.assertEqual(calculation_total([5, 4, 3]), 12)

    def test_calculation_total_first_case(self):
        self.assertEqual(calculation_total([11, 10]), 0)

    def test_calculation_total_second_case(self):
        self.assertEqual(calculation_total([3, 5, 7, 11]), 16)

    def test_calculation_total_error_case_one(self):
        with self.assertRaises(TypeError):
            calculation_total("21321")

    def test_calculation_total_error_case_two(self):
        with self.assertRaises(TypeError):
            calculation_total([12, 3, "Hello", 2])

if __name__ == '__main__':
    unittest.main()
