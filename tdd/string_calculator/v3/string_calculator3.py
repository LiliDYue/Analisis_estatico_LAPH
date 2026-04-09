"""
Module for testing and implementing a string calculator
with support for multiple delimiters.
"""

import unittest


def string_calculator(numbers: str) -> float:
    """
    Convert a string of numbers into their sum.

    Supports:
    - Comma and newline as delimiters
    - Mixed delimiters
    - Invalid sequences treated as zero
    - Empty elements ignored

    :param numbers: String containing numbers
    :return: Sum of the numbers
    """
    if numbers == "":
        return 0

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

    def test_empty_string(self):
        """Test empty string returns 0."""
        self.assertEqual(string_calculator(""), 0)

    def test_single_number(self):
        """Test a single number."""
        self.assertEqual(string_calculator("5"), 5)

    def test_multiple_numbers_comma(self):
        """Test multiple numbers separated by commas."""
        self.assertEqual(string_calculator("1,2,3"), 6)

    def test_multiple_numbers_newline(self):
        """Test multiple numbers separated by newlines."""
        self.assertEqual(string_calculator("1\n2\n3"), 6)

    def test_mixed_delimiters(self):
        """Test mixed delimiters (comma and newline)."""
        self.assertEqual(string_calculator("1\n2,3"), 6)

    def test_comma_newline_treated_as_zero(self):
        """Test ',\\n' treated as zero."""
        self.assertEqual(string_calculator("1,\n2"), 3)

    def test_newline_comma_treated_as_zero(self):
        """Test '\\n,' treated as zero."""
        self.assertEqual(string_calculator("1\n,2"), 3)

    def test_multiple_invalid_sequences(self):
        """Test multiple invalid delimiter sequences."""
        self.assertEqual(string_calculator("1,\n,2\n,3"), 6)

    def test_empty_elements_ignored(self):
        """Test empty elements are ignored."""
        self.assertEqual(string_calculator("1,,2"), 3)


if __name__ == "__main__":
    unittest.main()
