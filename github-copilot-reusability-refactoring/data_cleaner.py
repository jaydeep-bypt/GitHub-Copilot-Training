"""
Data cleaning module.
Handles data validation, cleaning, and normalization.
"""

from typing import List, Dict, Any, Optional
from utils.data_utils import (
    file_exists, read_csv_file, write_csv_file,
    clean_numeric_field, clean_text_field,
    validate_required_fields, validate_csv_structure
)
from utils.math_utils import round_to_decimal_places, validate_positive_number
from utils.logging_utils import setup_logger, log_info, log_error


def clean_csv_data(input_file: str, output_file: str) -> bool:
    """
    Clean CSV data and write to output file.
    
    Args:
        input_file: Path to input CSV file
        output_file: Path to output CSV file
        
    Returns:
        True if successful, False otherwise
    """
    # Set up logger
    logger = setup_logger('data_cleaner')
    
    log_info(logger, "Starting data cleaning process...")
    
    # Check if input file exists
    if not file_exists(input_file):
        log_error(logger, f"Error: Input file {input_file} not found")
        return False
    
    # Read input data
    log_info(logger, f"Reading data from {input_file}...")
    data = read_csv_file(input_file)
    
    if data is None:
        log_error(logger, "Error reading file")
        return False
    
    log_info(logger, f"Loaded {len(data)} records")
    
    # Clean and validate data
    clean_data, invalid_count = clean_and_validate_rows(data, logger)
    
    log_info(logger, f"Cleaned {len(clean_data)} records, skipped {invalid_count} invalid records")
    
    # Write cleaned data to output file
    if clean_data:
        log_info(logger, f"Writing cleaned data to {output_file}...")
        fieldnames = ['date', 'product', 'amount', 'quantity']
        success = write_csv_file(output_file, clean_data, fieldnames)
        
        if success:
            log_info(logger, "Data cleaning completed successfully")
            return True
        else:
            log_error(logger, "Error writing output file")
            return False
    else:
        log_info(logger, "No valid data to write")
        return False


def clean_and_validate_rows(data: List[Dict[str, Any]], logger) -> tuple[List[Dict[str, Any]], int]:
    """
    Clean and validate data rows.
    
    Args:
        data: List of raw data rows
        logger: Logger instance
        
    Returns:
        Tuple of (cleaned data list, invalid count)
    """
    clean_data = []
    invalid_count = 0
    required_fields = ['amount', 'quantity', 'product']
    
    for row in data:
        # Validate required fields
        if not validate_required_fields(row, required_fields):
            invalid_count += 1
            log_info(logger, "Skipping row with missing fields")
            continue
        
        # Clean and convert numeric fields
        amount = clean_numeric_field(row['amount'], float)
        quantity = clean_numeric_field(row['quantity'], int)
        
        if amount is None or quantity is None:
            invalid_count += 1
            log_info(logger, "Skipping row with invalid data")
            continue
        
        # Round amount to 2 decimal places
        amount = round_to_decimal_places(amount)
        
        # Validate ranges
        if not validate_positive_number(amount) or not validate_positive_number(quantity):
            invalid_count += 1
            log_info(logger, "Skipping row with negative values")
            continue
        
        # Clean product name
        product = clean_text_field(row['product'])
        
        # Create cleaned row
        clean_row = {
            'date': row.get('date', ''),
            'product': product,
            'amount': amount,
            'quantity': quantity
        }
        clean_data.append(clean_row)
    
    return clean_data, invalid_count


def validate_data_file(filename: str) -> bool:
    """
    Validate a CSV data file.
    
    Args:
        filename: Path to CSV file to validate
        
    Returns:
        True if valid, False otherwise
    """
    # Set up logger
    logger = setup_logger('data_validator')
    
    log_info(logger, f"Validating {filename}...")
    
    if not file_exists(filename):
        log_info(logger, "File does not exist")
        return False
    
    # Read and check file structure
    data = read_csv_file(filename)
    if data is None:
        log_error(logger, "Validation error: Cannot read file")
        return False
    
    log_info(logger, f"File contains {len(data)} rows")
    
    # Check for required fields
    required_fields = ['date', 'product', 'amount', 'quantity']
    if not validate_csv_structure(filename, required_fields):
        log_info(logger, f"Missing required fields")
        return False
    
    log_info(logger, "Validation passed")
    return True


if __name__ == "__main__":
    clean_csv_data("sales_data.csv", "sales_data_clean.csv")
