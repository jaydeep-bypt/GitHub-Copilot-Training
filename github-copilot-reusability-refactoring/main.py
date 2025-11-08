"""
Main entry point for data processing pipeline.
Orchestrates data cleaning, analysis, and report generation.
"""

from typing import List, Dict, Any
from utils.data_utils import (
    file_exists, read_csv_file, create_sample_csv,
    clean_numeric_field, validate_required_fields
)
from utils.math_utils import round_to_decimal_places, calculate_statistics
from utils.logging_utils import setup_logger, log_info, log_error, format_currency


def main() -> None:
    """Main function to orchestrate the data processing pipeline."""
    # Set up logger
    logger = setup_logger('main')
    
    log_info(logger, "Starting data processing pipeline...")
    
    # Check if data file exists
    data_file = "sales_data.csv"
    if not file_exists(data_file):
        log_info(logger, "Creating sample data file...")
        create_sample_data(data_file)
    
    # Read data from CSV
    log_info(logger, f"Reading data from {data_file}...")
    data = read_csv_file(data_file)
    
    if data is None:
        log_error(logger, "Error reading file")
        return
    
    log_info(logger, f"Loaded {len(data)} records")
    
    # Clean the data
    log_info(logger, "Cleaning data...")
    clean_data = clean_and_validate_data(data, logger)
    
    log_info(logger, f"Cleaned data: {len(clean_data)} valid records")
    
    # Calculate basic statistics
    amounts = [float(row['amount']) for row in clean_data]
    if amounts:
        stats = calculate_statistics(amounts)
        
        log_info(logger, "Statistics calculated successfully")
        log_info(logger, f"Total: {format_currency(stats['total'])}")
        log_info(logger, f"Average: {format_currency(stats['average'])}")
        log_info(logger, f"Min: {format_currency(stats['min'])}")
        log_info(logger, f"Max: {format_currency(stats['max'])}")
    
    log_info(logger, "Pipeline completed successfully")


def clean_and_validate_data(data: List[Dict[str, Any]], logger) -> List[Dict[str, Any]]:
    """
    Clean and validate data rows.
    
    Args:
        data: List of data rows to clean
        logger: Logger instance for output
        
    Returns:
        List of cleaned and validated data rows
    """
    clean_data = []
    for row in data:
        if validate_required_fields(row, ['amount', 'quantity']):
            # Clean numeric fields
            amount = clean_numeric_field(row['amount'], float)
            quantity = clean_numeric_field(row['quantity'], int)
            
            if amount is not None and quantity is not None:
                # Round amount to 2 decimal places
                row['amount'] = round_to_decimal_places(amount)
                row['quantity'] = quantity
                clean_data.append(row)
            else:
                log_info(logger, "Skipping invalid row")
    
    return clean_data


def create_sample_data(filename: str) -> None:
    """
    Create sample CSV data for testing.
    
    Args:
        filename: Path to create the sample CSV file
    """
    data = [
        {'date': '2025-01-01', 'product': 'Widget A', 'amount': '125.50', 'quantity': '10'},
        {'date': '2025-01-02', 'product': 'Widget B', 'amount': '87.25', 'quantity': '5'},
        {'date': '2025-01-03', 'product': 'Widget C', 'amount': '210.00', 'quantity': '15'},
        {'date': '2025-01-04', 'product': 'Widget A', 'amount': '156.75', 'quantity': '12'},
        {'date': '2025-01-05', 'product': 'Widget D', 'amount': '99.99', 'quantity': '8'},
    ]
    
    create_sample_csv(filename, data)


if __name__ == "__main__":
    main()
