"""
test_practice_sequences.py
Mihaela
Created March 20, 2019. Last updated February 10, 2020
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


if __name__ == '__main__':
    unittest.main()
