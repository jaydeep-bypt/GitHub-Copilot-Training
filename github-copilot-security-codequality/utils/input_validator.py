# input_validator.py
"""Input validation utilities for security."""
import re
from typing import Optional


def validate_username(username: str) -> bool:
    """
    Validate username format to prevent injection attacks.
    
    Args:
        username: Username string to validate
        
    Returns:
        True if valid, False otherwise
    """
    # Allow alphanumeric, underscore, hyphen, 3-20 characters
    pattern = r'^[a-zA-Z0-9_-]{3,20}$'
    return bool(re.match(pattern, username))


def sanitize_input(user_input: str, max_length: int = 100) -> Optional[str]:
    """
    Sanitize user input by removing potentially dangerous characters.
    
    Args:
        user_input: Raw user input
        max_length: Maximum allowed length
        
    Returns:
        Sanitized input or None if invalid
    """
    if not user_input or len(user_input) > max_length:
        return None
    
    # Remove SQL-dangerous characters
    dangerous_chars = ["'", '"', ';', '--', '/*', '*/']
    sanitized = user_input
    for char in dangerous_chars:
        sanitized = sanitized.replace(char, '')
    
    return sanitized.strip()
