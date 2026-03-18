# -*- coding: utf-8 -*-

"""
Unit tests for mock up.
"""

import unittest
from unittest.mock import MagicMock, Mock, patch

from white_box.mockup_exercises import (
    execute_command,
    fetch_data_from_api,
    perform_action_based_on_time,
    read_data_from_file,
)


class TestMockExamples(unittest.TestCase):
    """Test suite for mock-based examples."""

    @patch("white_box.mockup_exercises.requests.get")
    def test_fetch_data_from_api(self, mock_get):
        """
        Test fetching data from API using a standard Mock.

        - Mocks requests.get
        - Simulates JSON response
        """
        # Arrange
        mock_response = Mock()
        mock_response.json.return_value = {"key": "value"}
        mock_get.return_value = mock_response

        url = "http://fake-api.com"

        # Act
        result = fetch_data_from_api(url)

        # Assert
        self.assertEqual(result, {"key": "value"})
        mock_get.assert_called_once_with(url, timeout=10)

    @patch("builtins.open")
    def test_read_data_from_file(self, mock_open):
        """
        Test reading data from a file using a standard Mock.

        - Mocks built-in open
        - Simulates file read content
        """
        # Arrange
        mock_file = Mock()
        mock_file.read.return_value = "file content"
        mock_open.return_value.__enter__.return_value = mock_file

        filename = "fake_file.txt"

        # Act
        result = read_data_from_file(filename)

        # Assert
        self.assertEqual(result, "file content")
        mock_open.assert_called_once_with(filename, encoding="utf-8")

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command(self, mock_run):
        """
        Test subprocess command execution using a standard Mock.

        - Mocks subprocess.run
        - Simulates command output
        """
        # Arrange
        mock_result = Mock()
        mock_result.stdout = "command output"
        mock_run.return_value = mock_result

        command = ["ls", "-l"]

        # Act
        result = execute_command(command)

        # Assert
        self.assertEqual(result, "command output")
        mock_run.assert_called_once_with(
            command, capture_output=True, check=False, text=True
        )

    @patch("white_box.mockup_exercises.time")
    def test_perform_action_based_on_time(self, mock_time):
        """
        Test time-based behavior using MagicMock.

        - Uses MagicMock for more flexible mocking
        - Simulates different time values
        """
        # Arrange
        mock_time.time = MagicMock(return_value=5)

        # Act
        result = perform_action_based_on_time()

        # Assert
        self.assertEqual(result, "Action A")

        # Change return value to test other branch
        mock_time.time.return_value = 20

        result = perform_action_based_on_time()
        self.assertEqual(result, "Action B")


if __name__ == "__main__":
    unittest.main()
