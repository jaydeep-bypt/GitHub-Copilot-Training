"""
test_my_module.py

Unit tests for my_module.py using pytest.
Includes edge cases, table-driven tests, and mocks.
"""

import sys
import os
import pytest
from unittest.mock import patch

# Ensure the project root is in sys.path for module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from my_module import parse_string, calculate_sum, fetch_user_data

# ----------------------
# Tests for parse_string
# ----------------------
@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("hello world", ["hello", "world"]),
        ("one two three", ["one", "two", "three"]),
        ("", []),  # Edge case: empty string
        ("   ", []),  # Edge case: string with only spaces
        ("multiple   spaces here", ["multiple", "spaces", "here"]),  # Edge: multiple spaces
    ]
)
def test_parse_string(input_str, expected):
    """Test parse_string with normal and edge cases."""
    assert parse_string(input_str) == expected

# ------------------------
# Tests for calculate_sum
# ------------------------
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, -2, -3),  # Edge: negative numbers
        (999999999, 1, 1000000000),  # Edge: very large numbers
        (-100, 100, 0),
    ]
)
def test_calculate_sum(a, b, expected):
    """Test calculate_sum with normal and edge cases."""
    assert calculate_sum(a, b) == expected

# ---------------------------
# Tests for fetch_user_data
# ---------------------------
def test_fetch_user_data_success():
    """Test fetch_user_data with a valid user ID (mocked)."""
    mock_response = {"id": 1, "name": "Leanne Graham"}
    with patch("my_module.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        result = fetch_user_data(1)
        assert result == mock_response

def test_fetch_user_data_not_found():
    """Test fetch_user_data with an invalid user ID (mocked 404)."""
    with patch("my_module.requests.get") as mock_get:
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = {}
        with pytest.raises(ValueError, match="User with id 999 not found."):
            fetch_user_data(999)

def test_fetch_user_data_api_error():
    """Test fetch_user_data with a network error (mocked exception)."""
    with patch("my_module.requests.get", side_effect=Exception("Network error")):
        with pytest.raises(Exception, match="Network error"):
            fetch_user_data(1)
