"""
Module for testing and validating passwords with multiple conditions.
"""

import unittest


def validate_password(password: str) -> bool:
    """
    Validate that the password:
    - Has at least 8 characters
    - Contains at least 2 numbers

    If one or both conditions fail, raises a ValueError
    with the corresponding message(s).

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

    if errors:
        raise ValueError(" | ".join(errors))

    return True


class TestValidatePassword(unittest.TestCase):
    """
    Unit tests for validate_password function with combined validations.
    """

    def test_valid_password_exact_conditions(self):
        """Test valid password meeting exact requirements."""
        self.assertTrue(validate_password("abcd1234"))

    def test_valid_password_more_numbers(self):
        """Test valid password with more than required numbers."""
        self.assertTrue(validate_password("secure12345"))

    def test_invalid_password_short(self):
        """Test password shorter than 8 characters."""
        with self.assertRaises(ValueError) as context:
            validate_password("abc123")
        self.assertIn(
            "The password must be at least 8 characters", str(context.exception)
        )

    def test_invalid_password_not_enough_numbers(self):
        """Test password with insufficient numeric characters."""
        with self.assertRaises(ValueError) as context:
            validate_password("abcdefgh")
        self.assertIn(
            "The password must contain at least 2 numbers", str(context.exception)
        )

    def test_invalid_password_both_conditions(self):
        """Test password failing both conditions."""
        with self.assertRaises(ValueError) as context:
            validate_password("abc")
        message = str(context.exception)
        self.assertIn("The password must be at least 8 characters", message)
        self.assertIn("The password must contain at least 2 numbers", message)

    def test_invalid_password_one_number(self):
        """Test password with only one numeric character."""
        with self.assertRaises(ValueError) as context:
            validate_password("abcdefg1")
        self.assertIn(
            "The password must contain at least 2 numbers", str(context.exception)
        )


if __name__ == "__main__":
    unittest.main()
