"""
Math utilities module.
Provides reusable functions for mathematical operations and calculations.
"""

from typing import List, Optional, Dict, Any


def round_to_decimal_places(value: float, decimal_places: int = 2) -> float:
    """
    Round a number to specified decimal places.
    
    Args:
        value: Number to round
        decimal_places: Number of decimal places (default: 2)
        
    Returns:
        Rounded value
    """
    multiplier = 10 ** decimal_places
    return round(value * multiplier) / multiplier


def calculate_sum(values: List[float]) -> float:
    """
    Calculate the sum of a list of numbers.
    
    Args:
        values: List of numbers to sum
        
    Returns:
        Sum of all values, or 0 if list is empty
    """
    return sum(values) if values else 0.0


def calculate_average(values: List[float]) -> Optional[float]:
    """
    Calculate the average (mean) of a list of numbers.
    
    Args:
        values: List of numbers
        
    Returns:
        Average value, or None if list is empty
    """
    if not values:
        return None
    return sum(values) / len(values)


def calculate_minimum(values: List[float]) -> Optional[float]:
    """
    Find the minimum value in a list of numbers.
    
    Args:
        values: List of numbers
        
    Returns:
        Minimum value, or None if list is empty
    """
    return min(values) if values else None


def calculate_maximum(values: List[float]) -> Optional[float]:
    """
    Find the maximum value in a list of numbers.
    
    Args:
        values: List of numbers
        
    Returns:
        Maximum value, or None if list is empty
    """
    return max(values) if values else None


def calculate_statistics(values: List[float]) -> Dict[str, Any]:
    """
    Calculate comprehensive statistics for a list of numbers.
    
    Args:
        values: List of numbers
        
    Returns:
        Dictionary containing total, average, min, max, and count
    """
    if not values:
        return {
            'total': 0.0,
            'average': 0.0,
            'min': None,
            'max': None,
            'count': 0
        }
    
    total = calculate_sum(values)
    average = calculate_average(values)
    minimum = calculate_minimum(values)
    maximum = calculate_maximum(values)
    
    return {
        'total': round_to_decimal_places(total),
        'average': round_to_decimal_places(average) if average is not None else 0.0,
        'min': round_to_decimal_places(minimum) if minimum is not None else None,
        'max': round_to_decimal_places(maximum) if maximum is not None else None,
        'count': len(values)
    }


def aggregate_by_key(data: List[Dict[str, Any]], key_field: str, value_field: str) -> Dict[str, float]:
    """
    Aggregate numeric values grouped by a key field.
    
    Args:
        data: List of dictionaries containing data
        key_field: Field name to group by
        value_field: Field name containing numeric values to sum
        
    Returns:
        Dictionary mapping keys to aggregated values
    """
    result = {}
    for row in data:
        key = row.get(key_field)
        value = row.get(value_field, 0)
        
        if key:
            try:
                numeric_value = float(value)
                result[key] = result.get(key, 0.0) + numeric_value
            except (ValueError, TypeError):
                continue
    
    # Round all results
    return {k: round_to_decimal_places(v) for k, v in result.items()}


def validate_positive_number(value: float) -> bool:
    """
    Validate that a number is positive (greater than or equal to zero).
    
    Args:
        value: Number to validate
        
    Returns:
        True if value is positive, False otherwise
    """
    return value >= 0
