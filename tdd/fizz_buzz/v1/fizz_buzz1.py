"""
FizzBuzz implementation with unit tests.
"""

import unittest


def fizz_buzz(number: int) -> str:
    """
    Return FizzBuzz result for a given number.

    Rules:
    - Multiples of 3 → "Fizz"
    - Multiples of 5 → "Buzz"
    - Multiples of both → "FizzBuzz"
    - Otherwise → the number as string

    :param number: Input value
    :raises TypeError: If input is not an integer
    :return: Result as string
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")

    if number % 15 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"

    return str(number)


class TestFizzBuzz(unittest.TestCase):
    """
    Unit tests for fizz_buzz function.
    """

    def test_returns_string(self):
        """Test result is always a string."""
        result = fizz_buzz(1)
        self.assertIsInstance(result, str)

    def test_returns_string_with_multiple_inputs(self):
        """Test multiple inputs return string."""
        for number in [1, 3, 5, 15, 100]:
            with self.subTest(number=number):
                result = fizz_buzz(number)
                self.assertIsInstance(result, str)

    def test_raises_error_when_input_is_not_a_number(self):
        """Test invalid inputs raise TypeError."""
        for invalid in ["hello", None, [1], {"a": 1}]:
            with self.subTest(invalid=invalid):
                with self.assertRaises(TypeError):
                    fizz_buzz(invalid)


if __name__ == "__main__":
    unittest.main()
