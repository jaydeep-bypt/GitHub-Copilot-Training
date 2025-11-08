"""
my_module.py

A simple Python module for string parsing, arithmetic, and user data fetching.
"""

import requests
from typing import List, Dict

def parse_string(s: str) -> List[str]:
    """
    Parses a string into individual words and returns a list.
    Words are separated by whitespace.
    Args:
        s (str): Input string.
    Returns:
        List[str]: List of words.
    """
    return s.split()

def calculate_sum(a: int, b: int) -> int:
    """
    Returns the sum of two integers.
    Args:
        a (int): First integer.
        b (int): Second integer.
    Returns:
        int: Sum of a and b.
    """
    return a + b

def fetch_user_data(user_id: int) -> Dict:
    """
    Fetches user data from the API endpoint.
    Args:
        user_id (int): The user ID to fetch.
    Returns:
        dict: User data as a dictionary.
    Raises:
        ValueError: If the user is not found or request fails.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"User with id {user_id} not found.")
