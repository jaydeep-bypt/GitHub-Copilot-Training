"""
Data utilities module.
Provides reusable functions for CSV file operations, data reading, and cleaning.
"""

import csv
import os
from typing import List, Dict, Any, Optional


def file_exists(filepath: str) -> bool:
    """
    Check if a file exists at the given path.
    
    Args:
        filepath: Path to the file to check
        
    Returns:
        True if file exists, False otherwise
    """
    return os.path.exists(filepath)


def read_csv_file(filepath: str) -> Optional[List[Dict[str, Any]]]:
    """
    Read data from a CSV file and return as list of dictionaries.
    
    Args:
        filepath: Path to the CSV file to read
        
    Returns:
        List of dictionaries containing row data, or None if error occurs
    """
    if not file_exists(filepath):
        return None
    
    try:
        data = []
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data
    except Exception:
        return None


def write_csv_file(filepath: str, data: List[Dict[str, Any]], fieldnames: List[str]) -> bool:
    """
    Write data to a CSV file.
    
    Args:
        filepath: Path to the output CSV file
        data: List of dictionaries to write
        fieldnames: List of field names for the CSV header
        
    Returns:
        True if successful, False otherwise
    """
    try:
        with open(filepath, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        return True
    except Exception:
        return False


def create_sample_csv(filepath: str, data: List[Dict[str, Any]]) -> bool:
    """
    Create a sample CSV file with provided data.
    
    Args:
        filepath: Path for the new CSV file
        data: List of dictionaries containing sample data
        
    Returns:
        True if successful, False otherwise
    """
    if not data:
        return False
    
    fieldnames = list(data[0].keys())
    return write_csv_file(filepath, data, fieldnames)


def clean_numeric_field(value: Any, field_type: type = float) -> Optional[Any]:
    """
    Clean and convert a field to numeric type.
    
    Args:
        value: Value to clean and convert
        field_type: Target type (int or float)
        
    Returns:
        Converted value or None if conversion fails
    """
    try:
        return field_type(value)
    except (ValueError, TypeError):
        return None


def clean_text_field(value: str) -> str:
    """
    Clean text field by removing extra whitespace.
    
    Args:
        value: Text string to clean
        
    Returns:
        Cleaned text string
    """
    return ' '.join(str(value).split())


def validate_required_fields(row: Dict[str, Any], required_fields: List[str]) -> bool:
    """
    Validate that a row contains all required fields.
    
    Args:
        row: Dictionary representing a data row
        required_fields: List of required field names
        
    Returns:
        True if all required fields are present and non-empty, False otherwise
    """
    return all(row.get(field) for field in required_fields)


def validate_csv_structure(filepath: str, required_fields: List[str]) -> bool:
    """
    Validate that a CSV file has the required structure.
    
    Args:
        filepath: Path to the CSV file
        required_fields: List of required field names
        
    Returns:
        True if file has valid structure, False otherwise
    """
    if not file_exists(filepath):
        return False
    
    try:
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            
            if not rows:
                return True  # Empty file is valid
            
            # Check if all required fields are present
            return all(field in rows[0] for field in required_fields)
    except Exception:
        return False
