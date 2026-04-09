"""
Module for testing and validating passwords with numeric requirements.
"""

import unittest


def validate_password(password: str) -> bool:
    """
    Validate that the password:
    - Has at least 8 characters
    - Contains at least 2 numbers

    :param password: Password string to validate
    :raises ValueError: If validation rules are not met
    :return: True if valid
    """
    if len(password) < 8:
        raise ValueError("The password must be at least 8 characters")

    digit_count = sum(1 for char in password if char.isdigit())
    if digit_count < 2:
        raise ValueError("The password must contain at least 2 numbers")

    return True


class TestValidatePassword(unittest.TestCase):
    """
    Unit tests for validate_password function with numeric rules.
    """

    def test_valid_password_exact_8_with_2_numbers(self):
        """Test valid password with exactly 8 characters and 2 numbers."""
        self.assertTrue(validate_password("abcd1234"))

    def test_valid_password_more_than_8_with_many_numbers(self):
        """Test valid password with more than 8 characters and multiple numbers."""
        self.assertTrue(validate_password("secure12345"))

    def test_invalid_password_less_than_8_chars(self):
        """Test password shorter than 8 characters."""
        with self.assertRaises(ValueError) as context:
            validate_password("abc123")
        self.assertEqual(
            str(context.exception), "The password must be at least 8 characters"
        )

    def test_invalid_empty_password(self):
        """Test empty password."""
        with self.assertRaises(ValueError) as context:
            validate_password("")
        self.assertEqual(
            str(context.exception), "The password must be at least 8 characters"
        )

    def test_invalid_password_no_numbers(self):
        """Test password with no numeric characters."""
        with self.assertRaises(ValueError) as context:
            validate_password("abcdefgh")
        self.assertEqual(
            str(context.exception), "The password must contain at least 2 numbers"
        )

    def test_invalid_password_only_one_number(self):
        """Test password with only one numeric character."""
        with self.assertRaises(ValueError) as context:
            validate_password("abcdefg1")
        self.assertEqual(
            str(context.exception), "The password must contain at least 2 numbers"
        )

    def test_invalid_password_short_and_no_numbers(self):
        """Test password that is too short and has no numbers."""
        with self.assertRaises(ValueError) as context:
            validate_password("abc")
        self.assertEqual(
            str(context.exception), "The password must be at least 8 characters"
        )


if __name__ == "__main__":
    unittest.main()
