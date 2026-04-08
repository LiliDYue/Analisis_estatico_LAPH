"""
    TESTS
"""

import unittest


class TestStringCalculator(unittest.TestCase):

    def test_empty_string_returns_0(self):
        self.assertEqual(stringCalculator(""), 0)

    def test_single_integer(self):
        self.assertEqual(stringCalculator("1"), 1)

    def test_two_integers_comma(self):
        self.assertEqual(stringCalculator("1,2"), 3)

    def test_two_integers_newline(self):
        self.assertEqual(stringCalculator("1\n2"), 3)

    def test_mixed_separators_valid(self):
        self.assertEqual(stringCalculator("1,2\n3"), 6)

    def test_many_numbers_newline(self):
        self.assertEqual(stringCalculator("1\n2\n3\n4"), 10)

    def test_comma_then_newline_treated_as_zero(self):
        self.assertEqual(stringCalculator("1,\n3"), 4)

    def test_newline_then_comma_treated_as_zero(self):
        self.assertEqual(stringCalculator("1\n,3"), 4)

    def test_trailing_comma_raises(self):
        with self.assertRaises(ValueError):
            stringCalculator("1,2,3,")

    def test_trailing_newline_raises(self):
        with self.assertRaises(ValueError):
            stringCalculator("1,2\n")

    def test_custom_delimiter_pipe(self):
        self.assertEqual(stringCalculator("//|\n1|2"), 3)

    def test_custom_delimiter_word(self):
        self.assertEqual(stringCalculator("//sep\n1sep2"), 3)

    def test_custom_delimiter_many_numbers(self):
        self.assertEqual(stringCalculator("//|\n1|2|3|4"), 10)

    def test_custom_delimiter_cannot_mix_with_comma(self):
        with self.assertRaises(ValueError):
            stringCalculator("//|\n1|2,3")

    def test_custom_delimiter_trailing_raises(self):
        with self.assertRaises(ValueError):
            stringCalculator("//|\n1|2|")

    def test_negative_number_raises(self):
        with self.assertRaises(ValueError) as context:
            stringCalculator("1,-2,3")
        self.assertEqual(str(context.exception), "Negative number(s) not allowed: -2")

    def test_multiple_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            stringCalculator("1,-2,-4,3")
        self.assertEqual(
            str(context.exception), "Negative number(s) not allowed: -2, -4"
        )

    def test_negative_with_newlines(self):
        with self.assertRaises(ValueError) as context:
            stringCalculator("1\n-2\n3")
        self.assertEqual(str(context.exception), "Negative number(s) not allowed: -2")

    def test_negative_with_custom_delimiter(self):
        with self.assertRaises(ValueError) as context:
            stringCalculator("//|\n1|-2|3")
        self.assertEqual(str(context.exception), "Negative number(s) not allowed: -2")

    def test_multiple_negative_custom_delimiter(self):
        with self.assertRaises(ValueError) as context:
            stringCalculator("//|\n1|-2|-4|3")
        self.assertEqual(
            str(context.exception), "Negative number(s) not allowed: -2, -4"
        )


"""
    METODO
"""


def stringCalculator(numbers):
    if numbers == "":
        return 0

    delimiter = None
    if numbers.startswith("//"):
        header, numbers = numbers.split("\n", 1)
        delimiter = header[2:]

    if delimiter:
        if numbers.endswith(delimiter):
            raise ValueError("Invalid input: string cannot end with a separator")

        parts = numbers.split(delimiter)

        for n in parts:
            if "," in n or "\n" in n:
                raise ValueError("Invalid input: cannot mix delimiters")

        negatives = []
        total = 0

        for n in parts:
            if n.strip() == "":
                continue
            value = float(n)
            if value < 0:
                negatives.append(str(int(value)))
            total += value

        if negatives:
            raise ValueError(f"Negative number(s) not allowed: {', '.join(negatives)}")

        return total

    if numbers.endswith(",") or numbers.endswith("\n"):
        raise ValueError("Invalid input: string cannot end with a separator")

    numbers = numbers.replace(",\n", ",0,").replace("\n,", ",0,")

    parts = numbers.replace("\n", ",").split(",")

    negatives = []
    total = 0

    for n in parts:
        if n.strip() == "":
            continue
        value = float(n)
        if value < 0:
            negatives.append(str(int(value)))
        total += value

    if negatives:
        raise ValueError(f"Negative number(s) not allowed: {', '.join(negatives)}")

    return total


if __name__ == "__main__":
    unittest.main()
