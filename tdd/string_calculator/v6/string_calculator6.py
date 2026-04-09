"""
Tests y método String Calculator con correcciones para pylint.
"""

import unittest


def _extract_delimiter(numbers: str):
    """Extrae delimitador personalizado si existe."""
    if numbers.startswith("//"):
        header, numbers = numbers.split("\n", 1)
        return header[2:], numbers
    return None, numbers


def _validate_trailing_separator(numbers: str, delimiter: str | None):
    """Valida que no termine con separador."""
    if delimiter:
        if numbers.endswith(delimiter):
            raise ValueError("Invalid input: string cannot end with a separator")
    else:
        if numbers.endswith(",") or numbers.endswith("\n"):
            raise ValueError("Invalid input: string cannot end with a separator")


def _split_numbers(numbers: str, delimiter: str | None):
    """Divide la cadena en partes según delimitador."""
    if delimiter:
        parts = numbers.split(delimiter)
        for part in parts:
            if "," in part or "\n" in part:
                raise ValueError("Invalid input: cannot mix delimiters")
        return parts

    numbers = numbers.replace(",\n", ",0,").replace("\n,", ",0,")
    return numbers.replace("\n", ",").split(",")


def _sum_numbers(parts):
    """Suma números y valida negativos."""
    negatives = []
    total = 0

    for part in parts:
        if part.strip() == "":
            continue

        value = int(part)

        if value < 0:
            negatives.append(str(value))

        total += value

    if negatives:
        raise ValueError(f"Negative number(s) not allowed: {', '.join(negatives)}")

    return total


def string_calculator(numbers: str) -> int:
    """
    Suma números en un string con diferentes delimitadores.
    """
    if numbers == "":
        return 0

    delimiter, numbers = _extract_delimiter(numbers)

    _validate_trailing_separator(numbers, delimiter)

    parts = _split_numbers(numbers, delimiter)

    return _sum_numbers(parts)


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
        """Should treat comma followed by newline as a zero value."""
        self.assertEqual(string_calculator("1,\n3"), 4)

    def test_newline_then_comma_treated_as_zero(self):
        """Should treat newline followed by comma as a zero value."""
        self.assertEqual(string_calculator("1\n,3"), 4)

    def test_trailing_comma_raises(self):
        """Should raise ValueError if string ends with a comma."""
        with self.assertRaises(ValueError):
            string_calculator("1,2,3,")

    def test_trailing_newline_raises(self):
        """Should raise ValueError if string ends with a newline."""
        with self.assertRaises(ValueError):
            string_calculator("1,2\n")

    def test_custom_delimiter_pipe(self):
        """Should support a custom delimiter using '|'."""
        self.assertEqual(string_calculator("//|\n1|2"), 3)

    def test_custom_delimiter_word(self):
        """Should support a custom delimiter using a word."""
        self.assertEqual(string_calculator("//sep\n1sep2"), 3)

    def test_custom_delimiter_many_numbers(self):
        """Should correctly sum multiple numbers with a custom delimiter."""
        self.assertEqual(string_calculator("//|\n1|2|3|4"), 10)

    def test_custom_delimiter_cannot_mix_with_comma(self):
        """Should raise ValueError when mixing custom delimiter with comma."""
        with self.assertRaises(ValueError):
            string_calculator("//|\n1|2,3")

    def test_custom_delimiter_trailing_raises(self):
        """Should raise ValueError if custom delimiter appears at the end."""
        with self.assertRaises(ValueError):
            string_calculator("//|\n1|2|")

    def test_negative_number_raises(self):
        """Should raise ValueError when a negative number is present."""
        with self.assertRaises(ValueError) as context:
            string_calculator("1,-2,3")
        self.assertEqual(str(context.exception), "Negative number(s) not allowed: -2")

    def test_multiple_negative_numbers(self):
        """Should report all negative numbers found in the input."""
        with self.assertRaises(ValueError) as context:
            string_calculator("1,-2,-4,3")
        self.assertEqual(
            str(context.exception), "Negative number(s) not allowed: -2, -4"
        )


if __name__ == "__main__":
    unittest.main()
