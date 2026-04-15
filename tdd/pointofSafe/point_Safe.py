"""
TESTS
"""
import unittest


class TestPointOfSale(unittest.TestCase):
    """
    Kata - Point of Sale

    Create a simple app for scanning bar codes to sell products.
    """

    @classmethod
    def setUpClass(cls):
        """Set up reusable test data."""
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
        """Test scanning individual barcodes."""
        for case in self.scan_test_data:
            with self.subTest(case=case):
                pos = PointOfSale()
                result = pos.scan(case["input"])
                self.assertEqual(result, case["output"])

    def test_total(self):
        """Test total calculation after multiple scans."""
        for case in self.total_test_data:
            with self.subTest(case=case):
                pos = PointOfSale()
                for barcode in case["input"]:
                    pos.scan(barcode)
                result = pos.total()
                self.assertEqual(result, case["output"])


"""
METODO
"""


class PointOfSale:
    """
    Point of Sale system that scans barcodes and tracks a running total.
    """

    PRODUCTS = {
        "12345": 7.25,
        "23456": 12.50,
    }

    def __init__(self):
        """Initialize total amount."""
        self._total = 0.0

    def scan(self, barcode: str) -> str:
        """
        Scan a barcode and return its price or an error message.

        Valid prices are accumulated in the running total.
        """
        if not barcode:
            return "Error: empty barcode"

        if barcode not in self.PRODUCTS:
            return "Error: barcode not found"

        price = self.PRODUCTS[barcode]
        self._total += price
        return f"${price:.2f}"

    def total(self) -> str:
        """
        Return the sum of all successfully scanned product prices.
        """
        return f"${self._total:.2f}"


if __name__ == "__main__":
    unittest.main()