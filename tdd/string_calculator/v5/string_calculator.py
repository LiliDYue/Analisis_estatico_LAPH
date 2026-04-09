"""
Module for testing and implementing a string calculator
with support for custom delimiters and validations.
"""

import unittest


def string_calculator(numbers: str) -> float:
    """
    Convert a string of numbers into their sum.

    Supports:
    - Comma and newline delimiters
    - Custom delimiters (e.g. "//;\\n1;2")
    - Invalid sequences treated as zero
    - Validation for trailing separators
    - Prevents mixing delimiters

    :param numbers: Input string
    :raises ValueError: If input format is invalid
    :return: Sum of numbers
    """
    if numbers == "":
        return 0

    delimiter = None

    # Custom delimiter
    if numbers.startswith("//"):
        header, numbers = numbers.split("\n", 1)
        delimiter = header[2:]

    if delimiter:
        if numbers.endswith(delimiter):
            raise ValueError("Invalid input: string cannot end with a separator")

        for part in numbers.split(delimiter):
            if "," in part or "\n" in part:
                raise ValueError("Invalid input: cannot mix delimiters")

        total = 0.0
        for part in numbers.split(delimiter):
            if part.strip() == "":
                continue
            total += float(part)

        return total

    # Default behavior
    if numbers.endswith(",") or numbers.endswith("\n"):
        raise ValueError("Invalid input: string cannot end with a separator")

    numbers = numbers.replace(",\n", ",0,").replace("\n,", ",0,")

    total = 0.0
    for part in numbers.replace("\n", ",").split(","):
        if part.strip() == "":
            continue
        total += float(part)

    return total


class TestStringCalculator(unittest.TestCase):
    """
    Unit tests for string_calculator function.
    """

    def test_empty_string_returns_0(self):
        """Test empty string."""
        self.assertEqual(string_calculator(""), 0)

    def test_single_integer(self):
        """Test single integer."""
        self.assertEqual(string_calculator("1"), 1)

    def test_two_integers_comma(self):
        """Test comma-separated integers."""
        self.assertEqual(string_calculator("1,2"), 3)

    def test_two_integers_newline(self):
        """Test newline-separated integers."""
        self.assertEqual(string_calculator("1\n2"), 3)

    def test_mixed_separators_valid(self):
        """Test mixed delimiters."""
        self.assertEqual(string_calculator("1,2\n3"), 6)

    def test_many_numbers_newline(self):
        """Test multiple newline-separated numbers."""
        self.assertEqual(string_calculator("1\n2\n3\n4"), 10)

    def test_comma_then_newline_treated_as_zero(self):
        """Test ',\\n' treated as zero."""
        self.assertEqual(string_calculator("1,\n3"), 4)

    def test_newline_then_comma_treated_as_zero(self):
        """Test '\\n,' treated as zero."""
        self.assertEqual(string_calculator("1\n,3"), 4)

    def test_trailing_comma_raises(self):
        """Test trailing comma."""
        with self.assertRaises(ValueError):
            string_calculator("1,2,3,")

    def test_trailing_newline_raises(self):
        """Test trailing newline."""
        with self.assertRaises(ValueError):
            string_calculator("1,2\n")

    def test_custom_delimiter_pipe(self):
        """Test custom delimiter '|'."""
        self.assertEqual(string_calculator("//|\n1|2"), 3)

    def test_custom_delimiter_word(self):
        """Test custom word delimiter."""
        self.assertEqual(string_calculator("//sep\n1sep2"), 3)

    def test_custom_delimiter_many_numbers(self):
        """Test multiple values with custom delimiter."""
        self.assertEqual(string_calculator("//|\n1|2|3|4"), 10)

    def test_custom_delimiter_cannot_mix_with_comma(self):
        """Test delimiter mixing raises error."""
        with self.assertRaises(ValueError):
            string_calculator("//|\n1|2,3")

    def test_custom_delimiter_trailing_raises(self):
        """Test trailing custom delimiter."""
        with self.assertRaises(ValueError):
            string_calculator("//|\n1|2|")


if __name__ == "__main__":
    unittest.main()
