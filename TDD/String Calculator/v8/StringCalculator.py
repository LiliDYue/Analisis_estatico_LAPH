"""
    TESTS
"""
import unittest

class TestStringCalculator(unittest.TestCase):

    def test_empty_string_returns_0(self):
        self.assertEqual(stringCalculator(''), 0)

    def test_single_integer(self):
        self.assertEqual(stringCalculator('1'), 1)

    def test_two_integers_comma(self):
        self.assertEqual(stringCalculator('1,2'), 3)

    def test_two_integers_newline(self):
        self.assertEqual(stringCalculator('1\n2'), 3)

    def test_mixed_separators_valid(self):
        self.assertEqual(stringCalculator('1,2\n3'), 6)

    def test_many_numbers_newline(self):
        self.assertEqual(stringCalculator('1\n2\n3\n4'), 10)

    def test_comma_then_newline_treated_as_zero(self):
        self.assertEqual(stringCalculator('1,\n3'), 4)

    def test_newline_then_comma_treated_as_zero(self):
        self.assertEqual(stringCalculator('1\n,3'), 4)

    def test_trailing_comma_raises(self):
        with self.assertRaises(ValueError):
            stringCalculator('1,2,3,')

    def test_trailing_newline_raises(self):
        with self.assertRaises(ValueError):
            stringCalculator('1,2\n')

    def test_custom_delimiter_pipe(self):
        self.assertEqual(stringCalculator('//|\n1|2'), 3)

    def test_custom_delimiter_word(self):
        self.assertEqual(stringCalculator('//sep\n1sep2'), 3)

    def test_custom_delimiter_many_numbers(self):
        self.assertEqual(stringCalculator('//|\n1|2|3|4'), 10)

    def test_custom_delimiter_cannot_mix_with_comma(self):
        with self.assertRaises(ValueError):
            stringCalculator('//|\n1|2,3')

    def test_custom_delimiter_trailing_raises(self):
        with self.assertRaises(ValueError):
            stringCalculator('//|\n1|2|')

    def test_negative_number_raises(self):
        with self.assertRaises(ValueError) as context:
            stringCalculator('1,-2,3')
        self.assertEqual(str(context.exception), "Negative number(s) not allowed: -2")

    def test_multiple_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            stringCalculator('1,-2,-4,3')
        self.assertEqual(str(context.exception), "Negative number(s) not allowed: -2, -4")

    def test_negative_with_newlines(self):
        with self.assertRaises(ValueError) as context:
            stringCalculator('1\n-2\n3')
        self.assertEqual(str(context.exception), "Negative number(s) not allowed: -2")

    def test_negative_with_custom_delimiter(self):
        with self.assertRaises(ValueError) as context:
            stringCalculator('//|\n1|-2|3')
        self.assertEqual(str(context.exception), "Negative number(s) not allowed: -2")

    def test_multiple_negative_custom_delimiter(self):
        with self.assertRaises(ValueError) as context:
            stringCalculator('//|\n1|-2|-4|3')
        self.assertEqual(str(context.exception), "Negative number(s) not allowed: -2, -4")

    def test_multiple_errors_trailing_and_negative(self):
        with self.assertRaises(ValueError) as context:
            stringCalculator('1,-2,')
        
        message = str(context.exception)
        self.assertIn('Invalid input: string cannot end with a separator', message)
        self.assertIn('Negative number(s) not allowed: -2', message)
        self.assertIn('\n|', message)

    def test_multiple_negatives_only(self):
        with self.assertRaises(ValueError) as context:
            stringCalculator('1,-2,-4,3')
        
        self.assertEqual(
            str(context.exception),
            "Negative number(s) not allowed: -2, -4"
        )

    def test_multiple_errors_custom_delimiter(self):
        with self.assertRaises(ValueError) as context:
            stringCalculator('//|\n1|-2|')
        
        message = str(context.exception)
        self.assertIn('Invalid input: string cannot end with a separator', message)
        self.assertIn('Negative number(s) not allowed: -2', message)
        self.assertIn('\n|', message)

    def test_mix_delimiters_and_negative(self):
        with self.assertRaises(ValueError) as context:
            stringCalculator('//|\n1|-2,3')
        
        message = str(context.exception)
        self.assertIn('Invalid input: cannot mix delimiters', message)
        self.assertIn('Negative number(s) not allowed: -2', message)

    def test_ignore_numbers_greater_than_1000(self):
        self.assertEqual(stringCalculator('2,1001'), 2)

    def test_ignore_multiple_numbers_greater_than_1000(self):
        self.assertEqual(stringCalculator('1000,1001,2000,3'), 1003)

    def test_ignore_with_newlines(self):
        self.assertEqual(stringCalculator('1\n1001\n2'), 3)

    def test_ignore_with_custom_delimiter(self):
        self.assertEqual(stringCalculator('//|\n1|1001|2'), 3)

    def test_ignore_and_negative(self):
        with self.assertRaises(ValueError) as context:
            stringCalculator('2,-3,1001')

        self.assertIn('Negative number(s) not allowed: -3', str(context.exception))

    def test_ignore_and_mix_error(self):
        with self.assertRaises(ValueError) as context:
            stringCalculator('//|\n1|1001,2')

        self.assertIn('Invalid input: cannot mix delimiters', str(context.exception))

"""
    METODO
"""

def stringCalculator(numbers):
    if numbers == '':
        return 0

    errors = []
    delimiter = None

    if numbers.startswith('//'):
        header, numbers = numbers.split('\n', 1)
        delimiter = header[2:]

    if delimiter:
        if numbers.endswith(delimiter):
            errors.append('Invalid input: string cannot end with a separator')

        parts = numbers.split(delimiter)

        mix_error = any(',' in n or '\n' in n for n in parts)
        if mix_error:
            errors.append('Invalid input: cannot mix delimiters')

        negatives = []
        total = 0

        for n in parts:
            if n.strip() == '':
                continue

            sub_parts = n.replace('\n', ',').split(',')

            for sub in sub_parts:
                if sub.strip() == '':
                    continue
                try:
                    value = float(sub)

                    if value < 0:
                        negatives.append(str(int(value)))

                    if value <= 1000 and not mix_error:
                        total += value

                except ValueError:
                    continue

        if negatives:
            errors.append(f"Negative number(s) not allowed: {', '.join(negatives)}")

        if errors:
            raise ValueError("\n|".join(errors))

        return total

    if numbers.endswith(',') or numbers.endswith('\n'):
        errors.append('Invalid input: string cannot end with a separator')

    numbers = numbers.replace(',\n', ',0,').replace('\n,', ',0,')

    parts = numbers.replace('\n', ',').split(',')

    negatives = []
    total = 0

    for n in parts:
        if n.strip() == '':
            continue

        value = float(n)

        if value < 0:
            negatives.append(str(int(value)))

        if value <= 1000:
            total += value

    if negatives:
        errors.append(f"Negative number(s) not allowed: {', '.join(negatives)}")

    if errors:
        raise ValueError("\n|".join(errors))

    return total

if __name__ == '__main__':
    unittest.main()
