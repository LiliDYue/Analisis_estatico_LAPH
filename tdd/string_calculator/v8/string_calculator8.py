"""
String Calculator with unit tests.
"""

import unittest


def _extract_delimiter(numbers: str):
    """Extract custom delimiter if present."""
    if numbers.startswith("//"):
        header, numbers = numbers.split("\n", 1)
        return header[2:], numbers
    return None, numbers


def _split_and_validate(numbers: str, delimiter: str | None, errors: list):
    """Split numbers and validate delimiter rules."""
    if delimiter:
        if numbers.endswith(delimiter):
            errors.append("Invalid input: string cannot end with a separator")

        parts = numbers.split(delimiter)

        if any("," in part or "\n" in part for part in parts):
            errors.append("Invalid input: cannot mix delimiters")

        return parts

    if numbers.endswith(",") or numbers.endswith("\n"):
        errors.append("Invalid input: string cannot end with a separator")

    numbers = numbers.replace(",\n", ",0,").replace("\n,", ",0,")
    return numbers.replace("\n", ",").split(",")


def _calculate_sum(parts: list, errors: list) -> int:
    """Calculate total, collect negatives, ignore >1000."""
    negatives = []
    total = 0

    for part in parts:
        if part.strip() == "":
            continue

        try:
            value = int(part)
        except ValueError:
            continue

        if value < 0:
            negatives.append(str(value))
            continue

        if value > 1000:
            continue

        total += value

    if negatives:
        errors.append(f"Negative number(s) not allowed: {', '.join(negatives)}")

    return total


def string_calculator(numbers: str) -> int:
    """
    Add numbers from a string based on delimiters.
    """
    if numbers == "":
        return 0

    errors = []

    delimiter, numbers = _extract_delimiter(numbers)

    parts = _split_and_validate(numbers, delimiter, errors)

    total = _calculate_sum(parts, errors)

    if errors:
        raise ValueError("\n|".join(errors))

    return total


class TestStringCalculator(unittest.TestCase):
    """Unit tests for string_calculator."""

    def test_empty_string_returns_0(self):
        """Should return 0 when the input string is empty."""
        self.assertEqual(string_calculator(""), 0)

    def test_single_integer(self):
        """Should return the same number when a single value is provided."""
        self.assertEqual(string_calculator("1"), 1)

    def test_two_integers_comma(self):
        """Should correctly sum two numbers separated by a comma."""
        self.assertEqual(string_calculator("1,2"), 3)

    def test_two_integers_newline(self):
        """Should correctly sum two numbers separated by a newline."""
        self.assertEqual(string_calculator("1\n2"), 3)

    def test_mixed_separators_valid(self):
        """Should allow mixing commas and newlines as delimiters."""
        self.assertEqual(string_calculator("1,2\n3"), 6)

    def test_many_numbers_newline(self):
        """Should correctly sum multiple numbers separated by newlines."""
        self.assertEqual(string_calculator("1\n2\n3\n4"), 10)

    def test_comma_then_newline_treated_as_zero(self):
        """Should treat a comma followed by newline as zero."""
        self.assertEqual(string_calculator("1,\n3"), 4)

    def test_newline_then_comma_treated_as_zero(self):
        """Should treat a newline followed by comma as zero."""
        self.assertEqual(string_calculator("1\n,3"), 4)

    def test_trailing_comma_raises(self):
        """Should raise ValueError if the string ends with a comma."""
        with self.assertRaises(ValueError):
            string_calculator("1,2,3,")

    def test_trailing_newline_raises(self):
        """Should raise ValueError if the string ends with a newline."""
        with self.assertRaises(ValueError):
            string_calculator("1,2\n")

    def test_custom_delimiter_pipe(self):
        """Should support '|' as a custom delimiter."""
        self.assertEqual(string_calculator("//|\n1|2"), 3)

    def test_custom_delimiter_word(self):
        """Should support a word as a custom delimiter."""
        self.assertEqual(string_calculator("//sep\n1sep2"), 3)

    def test_custom_delimiter_many_numbers(self):
        """Should correctly sum multiple numbers using a custom delimiter."""
        self.assertEqual(string_calculator("//|\n1|2|3|4"), 10)

    def test_custom_delimiter_cannot_mix_with_comma(self):
        """Should raise ValueError when mixing custom delimiter with comma."""
        with self.assertRaises(ValueError):
            string_calculator("//|\n1|2,3")

    def test_custom_delimiter_trailing_raises(self):
        """Should raise ValueError if the custom delimiter appears at the end."""
        with self.assertRaises(ValueError):
            string_calculator("//|\n1|2|")

    def test_negative_number_raises(self):
        """Should raise ValueError when a negative number is present."""
        with self.assertRaises(ValueError) as context:
            string_calculator("1,-2,3")
        self.assertEqual(str(context.exception), "Negative number(s) not allowed: -2")


if __name__ == "__main__":
    unittest.main()
