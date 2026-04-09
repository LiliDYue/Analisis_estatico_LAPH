"""
Module for testing and implementing a string calculator
with multiple delimiters and validations.
"""

import unittest


def string_calculator(numbers: str) -> float:
    """
    Convert a string of numbers into their sum.

    Supports:
    - Comma and newline as delimiters
    - Mixed delimiters
    - Invalid sequences treated as zero

    Raises:
    - ValueError if the string ends with a separator

    :param numbers: String containing numbers
    :return: Sum of the numbers
    """
    if numbers == "":
        return 0

    if numbers.endswith(",") or numbers.endswith("\n"):
        raise ValueError("Invalid input: string cannot end with a separator")

    # Handle invalid sequences
    numbers = numbers.replace(",\n", ",0,").replace("\n,", ",0,")

    total = 0.0

    # Normalize delimiters
    for number in numbers.replace("\n", ",").split(","):
        if number.strip() == "":
            continue
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
        """Test single integer."""
        self.assertEqual(string_calculator("1"), 1)

    def test_two_integers_comma(self):
        """Test two integers separated by comma."""
        self.assertEqual(string_calculator("1,2"), 3)

    def test_two_integers_newline(self):
        """Test two integers separated by newline."""
        self.assertEqual(string_calculator("1\n2"), 3)

    def test_mixed_separators_valid(self):
        """Test mixed valid separators."""
        self.assertEqual(string_calculator("1,2\n3"), 6)

    def test_many_numbers_newline(self):
        """Test multiple numbers with newline."""
        self.assertEqual(string_calculator("1\n2\n3\n4"), 10)

    def test_comma_then_newline_treated_as_zero(self):
        """Test ',\\n' treated as zero."""
        self.assertEqual(string_calculator("1,\n3"), 4)

    def test_newline_then_comma_treated_as_zero(self):
        """Test '\\n,' treated as zero."""
        self.assertEqual(string_calculator("1\n,3"), 4)

    def test_trailing_comma_raises(self):
        """Test trailing comma raises ValueError."""
        with self.assertRaises(ValueError):
            string_calculator("1,2,3,")

    def test_trailing_newline_raises(self):
        """Test trailing newline raises ValueError."""
        with self.assertRaises(ValueError):
            string_calculator("1,2\n")


if __name__ == "__main__":
    unittest.main()
