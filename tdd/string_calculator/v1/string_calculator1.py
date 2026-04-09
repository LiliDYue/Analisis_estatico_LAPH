"""
Module for testing and implementing a simple string calculator.
"""

import unittest


def string_calculator(numbers: str) -> float:
    """
    Convert a comma-separated string of numbers into their sum.

    :param numbers: String containing numbers separated by commas
    :return: Sum of the numbers as float (or int if empty)
    """
    if numbers == "":
        return 0

    total = 0.0
    for number in numbers.split(","):
        total += float(number)

    return total


class TestStringCalculator(unittest.TestCase):
    """
    Unit tests for string_calculator function.
    """

    def test_empty_string_returns_0(self):
        """Test empty string returns 0."""
        self.assertEqual(string_calculator(""), 0)

    def test_single_integer(self):
        """Test a single integer."""
        self.assertEqual(string_calculator("1"), 1)

    def test_two_integers(self):
        """Test two integers."""
        self.assertEqual(string_calculator("1,2"), 3)

    def test_single_float(self):
        """Test a single float."""
        self.assertAlmostEqual(string_calculator("1.2"), 1.2)

    def test_integer_and_float(self):
        """Test integer and float combination."""
        self.assertAlmostEqual(string_calculator("1,1.2"), 2.2)

    def test_two_floats(self):
        """Test two floats."""
        self.assertAlmostEqual(string_calculator("1.2,2.3"), 3.5)


if __name__ == "__main__":
    unittest.main()
