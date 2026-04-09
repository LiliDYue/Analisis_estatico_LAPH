"""
FizzBuzz implementation with unit tests.
"""

import unittest


def fizz_buzz(number: int) -> str:
    """
    Return 'Fizz' if number is multiple of 3,
    otherwise return the number as string.

    :param number: Input number
    :raises TypeError: If input is not an integer
    :return: Result as string
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")

    if number % 3 == 0:
        return "Fizz"

    return str(number)


class TestFizzBuzz(unittest.TestCase):
    """
    Unit tests for fizz_buzz function.
    """

    def test_returns_string(self):
        """
        Verify that the function always returns a string
        for a valid numeric input.
        """
        result = fizz_buzz(1)
        self.assertIsInstance(result, str)

    def test_returns_string_with_multiple_inputs(self):
        """
        Verify that multiple valid inputs always return a string.
        """
        for number in [1, 3, 5, 15, 100]:
            with self.subTest(number=number):
                result = fizz_buzz(number)
                self.assertIsInstance(result, str)

    def test_raises_error_when_input_is_not_a_number(self):
        """
        Verify that a TypeError is raised when the input
        is not an integer.
        """
        for invalid in ["hello", None, [1], {"a": 1}]:
            with self.subTest(invalid=invalid):
                with self.assertRaises(TypeError):
                    fizz_buzz(invalid)

    def test_returns_fizz_when_multiple_of_3(self):
        """
        Verify that the function returns 'Fizz'
        when the number is a multiple of 3.
        """
        for number in [3, 6, 9, 12]:
            with self.subTest(number=number):
                self.assertEqual(fizz_buzz(number), "Fizz")

    def test_does_not_return_fizz_when_not_multiple_of_3(self):
        """
        Verify that the function does NOT return 'Fizz'
        when the number is NOT a multiple of 3.
        """
        for number in [1, 2, 4, 5]:
            with self.subTest(number=number):
                self.assertNotEqual(fizz_buzz(number), "Fizz")


if __name__ == "__main__":
    unittest.main()
