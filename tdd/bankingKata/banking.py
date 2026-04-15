"""
TESTS
"""

# pylint: disable=protected-access

import contextlib
import datetime
import io
import unittest
from unittest.mock import patch


class TestAccount(unittest.TestCase):
    """Tests for Account."""

    FIXED_DATE = "13/04/2026"

    @classmethod
    def setUpClass(cls):
        """Set up test data."""
        cls.deposit_test_data = [
            {"input": [1000], "expected_balance": 1000},
            {"input": [1000, 2000], "expected_balance": 3000},
            {"input": [500, 500, 500], "expected_balance": 1500},
        ]

        cls.withdraw_test_data = [
            {"deposits": [1000], "input": [500], "expected_balance": 500},
            {"deposits": [2000], "input": [200, 300], "expected_balance": 1500},
        ]

        cls.statement_test_data = [
            {
                "operations": [("deposit", 1000)],
                "expected": "DATE | AMOUNT | BALANCE\n13/04/2026 | 1000 | 1000",
            },
            {
                "operations": [("deposit", 1000), ("withdraw", 500)],
                "expected": (
                    "DATE | AMOUNT | BALANCE\n"
                    "13/04/2026 | -500 | 500\n"
                    "13/04/2026 | 1000 | 1000"
                ),
            },
            {
                "operations": [
                    ("deposit", 1000),
                    ("deposit", 2000),
                    ("withdraw", 500),
                ],
                "expected": (
                    "DATE | AMOUNT | BALANCE\n"
                    "13/04/2026 | -500 | 2500\n"
                    "13/04/2026 | 2000 | 3000\n"
                    "13/04/2026 | 1000 | 1000"
                ),
            },
        ]

    def _make_account_with_ops(self, operations):
        """Create account and apply operations."""
        account = Account()
        for operation, amount in operations:
            if operation == "deposit":
                account.deposit(amount)
            elif operation == "withdraw":
                account.withdraw(amount)
        return account

    def _capture_statement(self, account):
        """Capture printed statement."""
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            account.printStatement()
        return buffer.getvalue().strip()

    @patch("__main__.datetime.date")
    def test_deposit(self, mock_date):
        """Test deposit."""
        mock_date.today.return_value.strftime.return_value = self.FIXED_DATE

        for case in self.deposit_test_data:
            with self.subTest(case=case):
                account = Account()
                for amount in case["input"]:
                    account.deposit(amount)
                self.assertEqual(account._balance, case["expected_balance"])

    @patch("__main__.datetime.date")
    def test_withdraw(self, mock_date):
        """Test withdraw."""
        mock_date.today.return_value.strftime.return_value = self.FIXED_DATE

        for case in self.withdraw_test_data:
            with self.subTest(case=case):
                account = Account()
                for amount in case["deposits"]:
                    account.deposit(amount)
                for amount in case["input"]:
                    account.withdraw(amount)
                self.assertEqual(account._balance, case["expected_balance"])

    @patch("__main__.datetime.date")
    def test_print_statement(self, mock_date):
        """Test print statement."""
        mock_date.today.return_value.strftime.return_value = self.FIXED_DATE

        for case in self.statement_test_data:
            with self.subTest(case=case):
                account = self._make_account_with_ops(case["operations"])
                output = self._capture_statement(account)
                self.assertEqual(output, case["expected"])


# pylint: disable=invalid-name
class Account:
    """Bank account."""

    def __init__(self):
        """Initialize account."""
        self._balance = 0
        self._transactions = []

    def deposit(self, amount: int):
        """Deposit money."""
        self._balance += amount
        date = datetime.date.today().strftime("%d/%m/%Y")
        self._transactions.append((date, amount, self._balance))

    def withdraw(self, amount: int):
        """Withdraw money."""
        self._balance -= amount
        date = datetime.date.today().strftime("%d/%m/%Y")
        self._transactions.append((date, -amount, self._balance))

    def printStatement(self):
        """Print statement."""
        print("DATE | AMOUNT | BALANCE")
        for date, amount, balance in reversed(self._transactions):
            print(f"{date} | {amount} | {balance}")


if __name__ == "__main__":
    unittest.main()
