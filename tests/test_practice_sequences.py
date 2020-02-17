"""
test_practice_sequences.py
Snehitha Mamidi
February 17, 2020
"""

import unittest
from problems.practice_sequences import Practice


class TestMonthsAndDays(unittest.TestCase):
    """
    Tests for the months_and_days() method of class Practice in the module
    practice_sequences in the package problems.
    """
    def setUp(self):
        """
        Define attribute p to hold object of type Practice
        """
        self.p = Practice()

    def test_two_months(self):
        """
        Test case with lists for two months only
        """
        input1 = ['january', 'february']
        input2 = [31, 28]
        actual_result = self.p.months_and_days(input1, input2)
        expected_result = ['Jan-31', 'Feb-28']
        self.assertEqual(actual_result, expected_result)

    def test_12_months(self):
        """
        Test case with lists for 12 months
        """
        input1 = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        input2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        actual_result = self.p.months_and_days(input1, input2)
        expected_result = ['Jan-31', 'Feb-28', 'Mar-31', 'Apr-30', 'May-31', 'Jun-30', 'Jul-31', 'Aug-31', 'Sep-30', 'Oct-31', 'Nov-30', 'Dec-31']
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()
