"""
TESTS
"""

import json
import os
import unittest

from ddt import data, ddt, unpack


@ddt
class TestCitySearch(unittest.TestCase):
    """Tests for city search."""

    @data(("",), ("V",), ("a",), ("1",))
    @unpack
    def test_fewer_than_2_chars_returns_no_results(self, text):
        """Test short inputs."""
        self.assertEqual(search_cities(text), [])

    @data(
        ("Va", ["Valencia", "Vancouver"]),
        ("Rom", ["Rome"]),
        ("Par", ["Paris"]),
        ("Xy", []),
    )
    @unpack
    def test_prefix_match(self, text, expected):
        """Test prefix."""
        result = search_cities(text)
        self.assertEqual(sorted(result), sorted(expected))

    @data(
        ("va", ["Valencia", "Vancouver"]),
        ("VA", ["Valencia", "Vancouver"]),
        ("Va", ["Valencia", "Vancouver"]),
        ("par", ["Paris"]),
        ("PAR", ["Paris"]),
    )
    @unpack
    def test_case_insensitive(self, text, expected):
        """Test case insensitive."""
        result = search_cities(text)
        self.assertEqual(sorted(result), sorted(expected))

    @data(
        ("ape", "Budapest"),
        ("ong", "Hong Kong"),
        ("kok", "Bangkok"),
        ("dam", "Amsterdam"),
        ("dam", "Rotterdam"),
    )
    @unpack
    def test_partial_match_contains_city(self, text, expected_city):
        """Test partial match."""
        self.assertIn(expected_city, search_cities(text))

    @data(("*", 16))
    @unpack
    def test_asterisk_returns_all_cities(self, text, expected_count):
        """Test wildcard."""
        result = search_cities(text)
        self.assertEqual(len(result), expected_count)

        for city in CITIES:
            self.assertIn(city, result)


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(CURRENT_DIR, "cities.json"), encoding="utf-8") as file:
    CITIES = json.load(file)


def search_cities(text: str) -> list[str]:
    """Search cities."""
    if text == "*":
        return list(CITIES)

    if len(text) < 2:
        return []

    query = text.lower()
    return [city for city in CITIES if query in city.lower()]


if __name__ == "__main__":
    unittest.main()
