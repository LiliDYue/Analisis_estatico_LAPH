"""
Module for testing and validating passwords.
"""

import unittest


def validate_password(password: str) -> bool:
    """
    Validate that the password has at least 8 characters.

    :param password: Password string to validate
    :raises ValueError: If password is less than 8 characters
    :return: True if valid
    """
    if len(password) < 8:
        raise ValueError("The password must be at least 8 characters")
    return True


class TestValidatePassword(unittest.TestCase):
    """
    Unit tests for validate_password function.
    """

    def test_valid_password_exact_8_chars(self):
        """Test valid password with exactly 8 characters."""
        self.assertTrue(validate_password("12345678"))

    def test_valid_password_more_than_8_chars(self):
        """Test valid password with more than 8 characters."""
        self.assertTrue(validate_password("securepassword"))

    def test_invalid_password_less_than_8_chars(self):
        """Test invalid password with less than 8 characters."""
        with self.assertRaises(ValueError) as context:
            validate_password("1234567")
        self.assertEqual(
            str(context.exception), "The password must be at least 8 characters"
        )

    def test_invalid_empty_password(self):
        """Test invalid empty password."""
        with self.assertRaises(ValueError) as context:
            validate_password("")
        self.assertEqual(
            str(context.exception), "The password must be at least 8 characters"
        )

    def test_invalid_password_7_chars(self):
        """Test invalid password with 7 characters."""
        with self.assertRaises(ValueError):
            validate_password("abcdefg")


if __name__ == "__main__":
    unittest.main()
