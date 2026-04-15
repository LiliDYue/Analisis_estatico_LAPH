"""
Module for testing and validating passwords with multiple conditions.
"""

import unittest


def validate_password(password: str) -> bool:
    """
    Validate that the password:
    - Has at least 8 characters
    - Contains at least 2 numbers
    - Contains at least 1 uppercase letter

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

    has_uppercase = any(char.isupper() for char in password)
    if not has_uppercase:
        errors.append("The password must contain at least one capital letter")

    if errors:
        raise ValueError(" | ".join(errors))

    return True


class TestValidatePassword(unittest.TestCase):
    """
    Unit tests for validate_password function with full validation rules.
    """

    def test_valid_password_all_conditions(self):
        """Test valid password meeting all conditions."""
        self.assertTrue(validate_password("Abcd1234"))

    def test_valid_password_multiple_uppercase_and_numbers(self):
        """Test valid password with multiple uppercase letters and numbers."""
        self.assertTrue(validate_password("SECURE1234"))

    def test_invalid_password_short(self):
        """Test password shorter than 8 characters."""
        with self.assertRaises(ValueError) as context:
            validate_password("Abc12")
        self.assertIn(
            "The password must be at least 8 characters", str(context.exception)
        )

    def test_invalid_password_not_enough_numbers(self):
        """Test password without enough numeric characters."""
        with self.assertRaises(ValueError) as context:
            validate_password("Abcdefgh")
        self.assertIn(
            "The password must contain at least 2 numbers", str(context.exception)
        )

    def test_invalid_password_no_uppercase(self):
        """Test password without uppercase letters."""
        with self.assertRaises(ValueError) as context:
            validate_password("abcd1234")
        self.assertIn(
            "The password must contain at least one capital letter",
            str(context.exception),
        )

    def test_invalid_password_no_uppercase_and_numbers(self):
        """Test password without uppercase letters and numbers."""
        with self.assertRaises(ValueError) as context:
            validate_password("abcdefgh")
        message = str(context.exception)
        self.assertIn("The password must contain at least 2 numbers", message)
        self.assertIn("The password must contain at least one capital letter", message)

    def test_invalid_password_all_conditions_fail(self):
        """Test password failing all conditions."""
        with self.assertRaises(ValueError) as context:
            validate_password("abc")
        message = str(context.exception)
        self.assertIn("The password must be at least 8 characters", message)
        self.assertIn("The password must contain at least 2 numbers", message)
        self.assertIn("The password must contain at least one capital letter", message)

    def test_invalid_password_one_number(self):
        """Test password with only one numeric character."""
        with self.assertRaises(ValueError) as context:
            validate_password("Abcdefg1")
        self.assertIn(
            "The password must contain at least 2 numbers", str(context.exception)
        )


if __name__ == "__main__":
    unittest.main()
