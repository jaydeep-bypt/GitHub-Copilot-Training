"""
Utility Module for Common Programming Tasks

This module provides utility functions for everyday programming tasks including
string manipulation, date formatting, and age calculations. It's designed to
simplify common operations that developers frequently encounter.

Author: GitHub Copilot
Date: 2025-10-11
Version: 1.0.0
"""

from datetime import datetime
from typing import Union


def format_date(date_obj: datetime, fmt: str = "%Y-%m-%d") -> str:
    """
    Format a datetime object into a string representation.
    
    This function takes a datetime object and converts it to a formatted string
    using the specified format pattern. It's useful for displaying dates in
    user-friendly formats or preparing dates for storage/transmission.
    
    Parameters:
        date_obj (datetime): The datetime object to format. Must be a valid
                           datetime instance.
        fmt (str, optional): The format string specifying how the date should
                           be formatted. Defaults to "%Y-%m-%d" (ISO format).
                           Common formats:
                           - "%Y-%m-%d" -> 2025-10-11
                           - "%B %d, %Y" -> October 11, 2025
                           - "%m/%d/%Y" -> 10/11/2025
    
    Returns:
        str: The formatted date string according to the specified format.
    
    Raises:
        AttributeError: If date_obj is not a datetime object.
        ValueError: If the format string is invalid.
    
    Example:
        >>> from datetime import datetime
        >>> date = datetime(2025, 10, 11, 14, 30, 0)
        >>> format_date(date)
        '2025-10-11'
        >>> format_date(date, "%B %d, %Y")
        'October 11, 2025'
        >>> format_date(date, "%m/%d/%Y %H:%M")
        '10/11/2025 14:30'
    """
    return date_obj.strftime(fmt)


def capitalize_words(text: str) -> str:
    """
    Capitalize the first letter of every word in a string.
    
    This function takes a string and capitalizes the first letter of each word
    while making all other letters lowercase. Words are separated by whitespace.
    This is useful for formatting names, titles, or any text that needs proper
    title case formatting.
    
    Parameters:
        text (str): The input string to be capitalized. Can contain multiple
                   words separated by spaces, tabs, or other whitespace characters.
    
    Returns:
        str: A new string with the first letter of each word capitalized
             and all other letters in lowercase.
    
    Example:
        >>> capitalize_words("hello world")
        'Hello World'
        >>> capitalize_words("PYTHON programming")
        'Python Programming'
        >>> capitalize_words("the quick brown fox")
        'The Quick Brown Fox'
        >>> capitalize_words("john doe")
        'John Doe'
        >>> capitalize_words("")
        ''
    """
    return text.title()


def calculate_age(birthdate: str, fmt: str = "%Y-%m-%d") -> int:
    """
    Calculate a person's age in years from their birthdate string.
    
    This function takes a birthdate as a string, parses it according to the
    specified format, and calculates the person's current age in complete years.
    The calculation is based on the current date and accounts for whether the
    birthday has occurred this year or not.
    
    Parameters:
        birthdate (str): The birthdate as a string. Must match the format
                        specified in the fmt parameter.
        fmt (str, optional): The format string that describes how the birthdate
                           string is formatted. Defaults to "%Y-%m-%d" (ISO format).
                           Common formats:
                           - "%Y-%m-%d" -> 1990-05-15
                           - "%m/%d/%Y" -> 05/15/1990
                           - "%d-%m-%Y" -> 15-05-1990
    
    Returns:
        int: The calculated age in complete years (whole number).
    
    Raises:
        ValueError: If the birthdate string doesn't match the specified format
                   or if the date is invalid (e.g., February 30).
        TypeError: If birthdate is not a string.
    
    Example:
        >>> # Assuming current date is 2025-10-11
        >>> calculate_age("1990-05-15")
        35
        >>> calculate_age("2000-12-25")
        24
        >>> calculate_age("05/15/1990", "%m/%d/%Y")
        35
        >>> calculate_age("15-05-1990", "%d-%m-%Y")
        35
    """
    # Parse the birthdate string into a datetime object
    birth_date = datetime.strptime(birthdate, fmt)
    
    # Get the current date
    today = datetime.now()
    
    # Calculate the age
    age = today.year - birth_date.year
    
    # Adjust age if birthday hasn't occurred this year yet
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age


def clean_whitespace(text: str) -> str:
    """
    Remove extra whitespace from a string and normalize spacing.
    
    This function removes leading and trailing whitespace, and replaces
    multiple consecutive whitespace characters (spaces, tabs, newlines)
    with single spaces. Useful for cleaning user input or formatting text.
    
    Parameters:
        text (str): The input string to clean.
    
    Returns:
        str: The cleaned string with normalized whitespace.
    
    Example:
        >>> clean_whitespace("  hello    world  ")
        'hello world'
        >>> clean_whitespace("line1\\n\\n\\nline2")
        'line1 line2'
    """
    import re
    return re.sub(r'\s+', ' ', text.strip())


def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate a string to a maximum length and add a suffix if truncated.
    
    This function shortens a string to fit within a specified maximum length.
    If truncation occurs, it adds a suffix (like "...") to indicate the text
    was cut off. Useful for displaying previews or fitting text in limited space.
    
    Parameters:
        text (str): The input string to potentially truncate.
        max_length (int): The maximum allowed length for the final string
                         (including the suffix).
        suffix (str, optional): The string to append when truncation occurs.
                              Defaults to "...".
    
    Returns:
        str: The original string if it fits, or a truncated version with suffix.
    
    Raises:
        ValueError: If max_length is less than the length of the suffix.
    
    Example:
        >>> truncate_string("This is a very long sentence", 15)
        'This is a ve...'
        >>> truncate_string("Short text", 20)
        'Short text'
        >>> truncate_string("Hello World", 8, ">>")
        'Hello >>>'
    """
    if len(text) <= max_length:
        return text
    
    if max_length < len(suffix):
        raise ValueError("max_length must be at least as long as the suffix")
    
    return text[:max_length - len(suffix)] + suffix