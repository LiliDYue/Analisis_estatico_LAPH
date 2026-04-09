"""
FizzBuzz implementation with unit tests.
"""

import unittest


def fizz_buzz(number: int) -> str:
    """
    Return:
    - 'Fizz' if multiple of 3
    - 'Buzz' if multiple of 5
    - 'FizzBuzz' if multiple of both
    - otherwise the number as string

    :param number: Input number
    :raises TypeError: If input is not an integer
    :return: Result as string
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")

    if number % 3 == 0 and number % 5 == 0:
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
        """Verify result is always a string."""
        result = fizz_buzz(1)
        self.assertIsInstance(result, str)

    def test_returns_string_with_multiple_inputs(self):
        """Verify multiple inputs return string."""
        for number in [1, 3, 5, 15, 100]:
            with self.subTest(number=number):
                result = fizz_buzz(number)
                self.assertIsInstance(result, str)

    def test_raises_error_when_input_is_not_a_number(self):
        """Verify TypeError for invalid inputs."""
        for invalid in ["hello", None, [1], {"a": 1}]:
            with self.subTest(invalid=invalid):
                with self.assertRaises(TypeError):
                    fizz_buzz(invalid)

    def test_returns_fizz_when_multiple_of_3(self):
        """Verify 'Fizz' for multiples of 3."""
        for number in [3, 6, 9, 12]:
            with self.subTest(number=number):
                self.assertEqual(fizz_buzz(number), "Fizz")

    def test_does_not_return_fizz_when_not_multiple_of_3(self):
        """Verify not 'Fizz' when not multiple of 3."""
        for number in [1, 2, 4, 5]:
            with self.subTest(number=number):
                self.assertNotEqual(fizz_buzz(number), "Fizz")

    def test_returns_buzz_when_multiple_of_5(self):
        """Verify 'Buzz' for multiples of 5."""
        for number in [5, 10, 20, 25]:
            with self.subTest(number=number):
                self.assertEqual(fizz_buzz(number), "Buzz")

    def test_does_not_return_buzz_when_not_multiple_of_5(self):
        """Verify not 'Buzz' when not multiple of 5."""
        for number in [1, 2, 3, 4]:
            with self.subTest(number=number):
                self.assertNotEqual(fizz_buzz(number), "Buzz")

    def test_returns_fizzbuzz_when_multiple_of_3_and_5(self):
        """Verify 'FizzBuzz' for multiples of both."""
        for number in [15, 30, 45, 60]:
            with self.subTest(number=number):
                self.assertEqual(fizz_buzz(number), "FizzBuzz")

    def test_does_not_return_fizzbuzz_when_not_multiple_of_both(self):
        """Verify not 'FizzBuzz' when not multiple of both."""
        for number in [3, 5, 6, 10]:
            with self.subTest(number=number):
                self.assertNotEqual(fizz_buzz(number), "FizzBuzz")


if __name__ == "__main__":
    unittest.main()
