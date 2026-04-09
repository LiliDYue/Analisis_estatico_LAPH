"""
Module for testing and validating passwords with full constraints.
"""

import string
import unittest


def validate_password(password: str) -> bool:
    """
    Validate that the password:
    - Has at least 8 characters
    - Contains at least 2 numbers
    - Contains at least 1 uppercase letter
    - Contains at least 1 special character

    Raises ValueError with all corresponding error messages.

    :param password: Password string to validate
    :raises ValueError: If validation rules are not met
    :return: True if valid
    """
    errors = []

    if len(password) < 8:
        errors.append("The password must be at least 8 characters")

    digit_count = sum(1 for char in password if char.isdigit())
    if digit_count < 2:
        errors.append("The password must contain at least 2 numbers")

    if not any(char.isupper() for char in password):
        errors.append("The password must contain at least one capital letter")

    if not any(char in string.punctuation for char in password):
        errors.append("The password must contain at least one special character")

    if errors:
        raise ValueError(" | ".join(errors))

    return True


class TestValidatePassword(unittest.TestCase):
    """
    Unit tests for validate_password function with full validation rules.
    """

    def test_valid_password_all_conditions(self):
        """Test valid password meeting all conditions."""
        self.assertTrue(validate_password("Abcd12!@"))

    def test_valid_password_multiple_specials(self):
        """Test valid password with multiple special characters."""
        self.assertTrue(validate_password("Secure123!#"))

    def test_invalid_password_no_special_char(self):
        """Test password without special characters."""
        with self.assertRaises(ValueError) as context:
            validate_password("Abcd1234")
        self.assertIn(
            "The password must contain at least one special character",
            str(context.exception),
        )

    def test_invalid_password_no_uppercase(self):
        """Test password without uppercase letters."""
        with self.assertRaises(ValueError) as context:
            validate_password("abcd12!@")
        self.assertIn(
            "The password must contain at least one capital letter",
            str(context.exception),
        )

    def test_invalid_password_not_enough_numbers(self):
        """Test password without enough numbers."""
        with self.assertRaises(ValueError) as context:
            validate_password("Abcdef!@")
        self.assertIn(
            "The password must contain at least 2 numbers", str(context.exception)
        )

    def test_invalid_password_short(self):
        """Test password shorter than 8 characters."""
        with self.assertRaises(ValueError) as context:
            validate_password("Ab1!")
        self.assertIn(
            "The password must be at least 8 characters", str(context.exception)
        )

    def test_invalid_password_multiple_failures(self):
        """Test password failing all conditions."""
        with self.assertRaises(ValueError) as context:
            validate_password("abc")
        message = str(context.exception)
        self.assertIn("The password must be at least 8 characters", message)
        self.assertIn("The password must contain at least 2 numbers", message)
        self.assertIn("The password must contain at least one capital letter", message)
        self.assertIn(
            "The password must contain at least one special character", message
        )

    def test_invalid_password_no_special_and_numbers(self):
        """Test password without special characters and numbers."""
        with self.assertRaises(ValueError) as context:
            validate_password("Abcdefgh")
        message = str(context.exception)
        self.assertIn("The password must contain at least 2 numbers", message)
        self.assertIn(
            "The password must contain at least one special character", message
        )


if __name__ == "__main__":
    unittest.main()
