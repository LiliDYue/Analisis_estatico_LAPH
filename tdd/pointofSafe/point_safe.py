"""
TESTS
"""

import unittest


class TestPointOfSale(unittest.TestCase):
    """Tests for PointOfSale."""

    @classmethod
    def setUpClass(cls):
        """Set up test data."""
        cls.scan_test_data = [
            {"input": "12345", "output": "$7.25"},
            {"input": "23456", "output": "$12.50"},
            {"input": "99999", "output": "Error: barcode not found"},
            {"input": "", "output": "Error: empty barcode"},
        ]

        cls.total_test_data = [
            {"input": ["12345"], "output": "$7.25"},
            {"input": ["12345", "23456"], "output": "$19.75"},
            {"input": ["12345", "99999", ""], "output": "$7.25"},
            {"input": [], "output": "$0.00"},
        ]

    def test_scan(self):
        """Test scan."""
        for case in self.scan_test_data:
            with self.subTest(case=case):
                pos = PointOfSale()
                self.assertEqual(pos.scan(case["input"]), case["output"])

    def test_total(self):
        """Test total."""
        for case in self.total_test_data:
            with self.subTest(case=case):
                pos = PointOfSale()
                for barcode in case["input"]:
                    pos.scan(barcode)
                self.assertEqual(pos.total(), case["output"])


class PointOfSale:
    """Point of Sale system."""

    PRODUCTS = {
        "12345": 7.25,
        "23456": 12.50,
    }

    def __init__(self):
        """Initialize POS."""
        self._total = 0.0

    def scan(self, barcode: str) -> str:
        """Scan barcode."""
        if not barcode:
            return "Error: empty barcode"

        if barcode not in self.PRODUCTS:
            return "Error: barcode not found"

        price = self.PRODUCTS[barcode]
        self._total += price
        return f"${price:.2f}"

    def total(self) -> str:
        """Return total."""
        return f"${self._total:.2f}"


if __name__ == "__main__":
    unittest.main()
