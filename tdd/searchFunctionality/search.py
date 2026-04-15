"""
TESTS
"""
import json
import os
import unittest


class TestCitySearch(unittest.TestCase):
    """Tests for city search functionality."""

    @classmethod
    def setUpClass(cls):
        """Set up test data."""
        cls.fewer_than_2_cases = ["", "V", "a", "1"]

        cls.prefix_cases = [
            {"input": "Va", "output": ["Valencia", "Vancouver"]},
            {"input": "Rom", "output": ["Rome"]},
            {"input": "Par", "output": ["Paris"]},
            {"input": "Xy", "output": []},
        ]

        cls.case_insensitive_cases = [
            {"input": "va", "output": ["Valencia", "Vancouver"]},
            {"input": "VA", "output": ["Valencia", "Vancouver"]},
            {"input": "Va", "output": ["Valencia", "Vancouver"]},
            {"input": "par", "output": ["Paris"]},
            {"input": "PAR", "output": ["Paris"]},
        ]

        cls.partial_match_cases = [
            {"input": "ape", "output": "Budapest"},
            {"input": "ong", "output": "Hong Kong"},
            {"input": "kok", "output": "Bangkok"},
            {"input": "dam", "output": "Amsterdam"},
            {"input": "dam", "output": "Rotterdam"},
        ]

    def test_fewer_than_2_chars_returns_no_results(self):
        """Req 1: fewer than 2 chars → no results."""
        for text in self.fewer_than_2_cases:
            with self.subTest(text=text):
                self.assertEqual(search_cities(text), [])

    def test_prefix_match(self):
        """Req 2: prefix match."""
        for case in self.prefix_cases:
            with self.subTest(case=case):
                result = search_cities(case["input"])
                self.assertEqual(sorted(result), sorted(case["output"]))

    def test_case_insensitive(self):
        """Req 3: case insensitive."""
        for case in self.case_insensitive_cases:
            with self.subTest(case=case):
                result = search_cities(case["input"])
                self.assertEqual(sorted(result), sorted(case["output"]))

    def test_partial_match_contains_city(self):
        """Req 4: partial match."""
        for case in self.partial_match_cases:
            with self.subTest(case=case):
                self.assertIn(case["output"], search_cities(case["input"]))

    def test_asterisk_returns_all_cities(self):
        """Req 5: '*' returns all cities."""
        result = search_cities("*")
        self.assertEqual(len(result), len(CITIES))

        for city in CITIES:
            self.assertIn(city, result)


# =====================
# METODO
# =====================

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(CURRENT_DIR, "cities.json"), encoding="utf-8") as file:
    CITIES = json.load(file)


def search_cities(text: str) -> list[str]:
    """Search cities based on input text."""
    if text == "*":
        return list(CITIES)

    if len(text) < 2:
        return []

    query = text.lower()
    return [city for city in CITIES if query in city.lower()]


if __name__ == "__main__":
    unittest.main()
    