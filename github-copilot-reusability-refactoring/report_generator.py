"""
Report generator module.
Creates formatted reports from processed data.
"""

from typing import List, Dict, Any
from utils.data_utils import file_exists, read_csv_file, clean_numeric_field
from utils.math_utils import round_to_decimal_places, aggregate_by_key, calculate_statistics
from utils.logging_utils import (
    setup_logger, log_info, log_error, 
    format_report_header, format_report_footer, format_currency
)


def generate_report(data_file: str) -> None:
    """
    Generate a formatted report from CSV data.
    
    Args:
        data_file: Path to the CSV data file
    """
    # Set up logger
    logger = setup_logger('report_generator')
    
    log_info(logger, "Generating report...")
    
    # Check if file exists
    if not file_exists(data_file):
        log_error(logger, f"Error: File {data_file} not found")
        return
    
    # Read CSV data
    log_info(logger, f"Reading data from {data_file}...")
    data = read_csv_file(data_file)
    
    if data is None:
        log_error(logger, "Error reading file")
        return
    
    log_info(logger, f"Loaded {len(data)} records")
    
    # Clean and process data
    clean_data = clean_report_data(data)
    
    # Calculate product totals
    product_totals = aggregate_by_key(clean_data, 'product', 'amount')
    
    # Calculate overall statistics
    amounts = [float(row['amount']) for row in clean_data]
    stats = calculate_statistics(amounts)
    
    # Generate report output
    format_report_header("SALES REPORT", logger)
    log_info(logger, f"Total Records: {len(clean_data)}")
    log_info(logger, "")
    log_info(logger, "Product Breakdown:")
    for product, amount in sorted(product_totals.items()):
        log_info(logger, f"  {product}: {format_currency(amount)}")
    log_info(logger, "")
    log_info(logger, f"Total Sales: {format_currency(stats['total'])}")
    log_info(logger, f"Average Sale: {format_currency(stats['average'])}")
    format_report_footer(logger)
    
    log_info(logger, "Report generation completed")


def clean_report_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Clean and validate data for report generation.
    
    Args:
        data: List of raw data rows
        
    Returns:
        List of cleaned data rows
    """
    clean_data = []
    for row in data:
        if row.get('amount') and row.get('product'):
            amount = clean_numeric_field(row['amount'], float)
            if amount is not None:
                # Round to 2 decimal places
                row['amount'] = round_to_decimal_places(amount)
                clean_data.append(row)
    
    return clean_data


if __name__ == "__main__":
    generate_report("sales_data.csv")
