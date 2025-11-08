"""
Data analyzer module.
Performs statistical analysis and calculations on data.
"""

from typing import Dict, Any, Optional, List
from utils.data_utils import file_exists, read_csv_file, clean_numeric_field
from utils.math_utils import round_to_decimal_places, calculate_statistics
from utils.logging_utils import (
    setup_logger, log_info, log_error,
    format_report_header, format_report_footer, format_currency
)


def analyze_sales_data(data_file: str) -> Optional[Dict[str, Any]]:
    """
    Analyze sales data and calculate statistics.
    
    Args:
        data_file: Path to the CSV data file
        
    Returns:
        Dictionary containing analysis results, or None if error occurs
    """
    # Set up logger
    logger = setup_logger('analyzer')
    
    log_info(logger, "Starting data analysis...")
    
    # Check if file exists
    if not file_exists(data_file):
        log_error(logger, f"Error: File {data_file} not found")
        return None
    
    # Read CSV data
    log_info(logger, f"Loading data from {data_file}...")
    data = read_csv_file(data_file)
    
    if data is None:
        log_error(logger, "Error reading file")
        return None
    
    log_info(logger, f"Loaded {len(data)} records")
    
    # Extract and clean numeric data
    amounts, quantities = extract_numeric_data(data, logger)
    
    # Calculate amount statistics
    amount_stats = calculate_statistics(amounts) if amounts else {}
    
    # Calculate quantity statistics
    quantity_stats = calculate_statistics(quantities) if quantities else {}
    
    # Calculate product-wise statistics
    product_stats = calculate_product_statistics(data)
    
    # Print analysis results
    print_analysis_results(logger, amount_stats, quantity_stats, product_stats)
    
    log_info(logger, "Analysis completed successfully")
    
    return {
        'amount_stats': amount_stats,
        'quantity_stats': quantity_stats,
        'product_stats': product_stats
    }


def extract_numeric_data(data: List[Dict[str, Any]], logger) -> tuple[List[float], List[int]]:
    """
    Extract and clean numeric data from rows.
    
    Args:
        data: List of data rows
        logger: Logger instance
        
    Returns:
        Tuple of (amounts list, quantities list)
    """
    amounts = []
    quantities = []
    
    for row in data:
        # Clean amount field
        amount = clean_numeric_field(row.get('amount'), float)
        if amount is not None:
            amounts.append(round_to_decimal_places(amount))
        
        # Clean quantity field
        quantity = clean_numeric_field(row.get('quantity'), int)
        if quantity is not None:
            quantities.append(quantity)
        
        # Log if both fields are invalid
        if amount is None and quantity is None:
            log_info(logger, "Skipping invalid row")
    
    return amounts, quantities


def calculate_product_statistics(data: List[Dict[str, Any]]) -> Dict[str, Dict[str, float]]:
    """
    Calculate statistics grouped by product.
    
    Args:
        data: List of data rows
        
    Returns:
        Dictionary mapping products to their statistics
    """
    product_stats = {}
    
    for row in data:
        product = row.get('product')
        amount = clean_numeric_field(row.get('amount', 0), float)
        quantity = clean_numeric_field(row.get('quantity', 0), int)
        
        if product and amount is not None and quantity is not None:
            # Round amount
            amount = round_to_decimal_places(amount)
            
            # Initialize product entry if needed
            if product not in product_stats:
                product_stats[product] = {
                    'total_amount': 0.0,
                    'total_quantity': 0,
                    'count': 0
                }
            
            # Aggregate values
            product_stats[product]['total_amount'] += amount
            product_stats[product]['total_quantity'] += quantity
            product_stats[product]['count'] += 1
    
    # Calculate averages and round totals
    for product in product_stats:
        total = product_stats[product]['total_amount']
        count = product_stats[product]['count']
        
        product_stats[product]['total_amount'] = round_to_decimal_places(total)
        product_stats[product]['average_amount'] = round_to_decimal_places(total / count)
    
    return product_stats


def print_analysis_results(
    logger,
    amount_stats: Dict[str, Any],
    quantity_stats: Dict[str, Any],
    product_stats: Dict[str, Dict[str, float]]
) -> None:
    """
    Print formatted analysis results.
    
    Args:
        logger: Logger instance
        amount_stats: Amount statistics dictionary
        quantity_stats: Quantity statistics dictionary
        product_stats: Product-wise statistics dictionary
    """
    format_report_header("ANALYSIS RESULTS", logger)
    
    log_info(logger, "Amount Statistics:")
    if amount_stats:
        log_info(logger, f"  Total: {format_currency(amount_stats['total'])}")
        log_info(logger, f"  Average: {format_currency(amount_stats['average'])}")
        log_info(logger, f"  Min: {format_currency(amount_stats['min'])}")
        log_info(logger, f"  Max: {format_currency(amount_stats['max'])}")
        log_info(logger, f"  Count: {amount_stats['count']}")
    
    log_info(logger, "")
    log_info(logger, "Quantity Statistics:")
    if quantity_stats:
        log_info(logger, f"  Total: {quantity_stats['total']}")
        log_info(logger, f"  Average: {quantity_stats['average']}")
        log_info(logger, f"  Min: {quantity_stats['min']}")
        log_info(logger, f"  Max: {quantity_stats['max']}")
    
    log_info(logger, "")
    log_info(logger, "Product Statistics:")
    for product, stats in sorted(product_stats.items()):
        log_info(logger, f"  {product}:")
        log_info(logger, f"    Total Sales: {format_currency(stats['total_amount'])}")
        log_info(logger, f"    Average Sale: {format_currency(stats['average_amount'])}")
        log_info(logger, f"    Total Quantity: {stats['total_quantity']}")
    
    format_report_footer(logger)


if __name__ == "__main__":
    analyze_sales_data("sales_data.csv")
