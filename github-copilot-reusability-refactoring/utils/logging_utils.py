"""
Logging utilities module.
Provides unified logging and output formatting functions.
"""

import logging
from datetime import datetime
from typing import Any, Optional


# Configure logging format
LOG_FORMAT = '[%(asctime)s] %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


def setup_logger(name: str = 'app', level: int = logging.INFO) -> logging.Logger:
    """
    Set up and configure a logger.
    
    Args:
        name: Logger name (default: 'app')
        level: Logging level (default: INFO)
        
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Remove existing handlers to avoid duplicates
    logger.handlers.clear()
    
    # Create console handler
    handler = logging.StreamHandler()
    handler.setLevel(level)
    
    # Create formatter
    formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)
    handler.setFormatter(formatter)
    
    # Add handler to logger
    logger.addHandler(handler)
    
    return logger


def log_info(logger: logging.Logger, message: str) -> None:
    """
    Log an info-level message.
    
    Args:
        logger: Logger instance
        message: Message to log
    """
    logger.info(message)


def log_error(logger: logging.Logger, message: str, exception: Optional[Exception] = None) -> None:
    """
    Log an error-level message.
    
    Args:
        logger: Logger instance
        message: Error message to log
        exception: Optional exception object
    """
    if exception:
        logger.error(f"{message}: {exception}")
    else:
        logger.error(message)


def log_warning(logger: logging.Logger, message: str) -> None:
    """
    Log a warning-level message.
    
    Args:
        logger: Logger instance
        message: Warning message to log
    """
    logger.warning(message)


def format_timestamp(dt: Optional[datetime] = None) -> str:
    """
    Format a datetime object as a string.
    
    Args:
        dt: Datetime object (default: current time)
        
    Returns:
        Formatted timestamp string
    """
    if dt is None:
        dt = datetime.now()
    return dt.strftime(DATE_FORMAT)


def format_currency(amount: float) -> str:
    """
    Format a number as currency string.
    
    Args:
        amount: Numeric amount
        
    Returns:
        Formatted currency string (e.g., "$123.45")
    """
    return f"${amount:.2f}"


def format_report_header(title: str, logger: logging.Logger) -> None:
    """
    Format and log a report header.
    
    Args:
        title: Report title
        logger: Logger instance
    """
    separator = "=" * 40
    log_info(logger, "")
    log_info(logger, separator)
    log_info(logger, f"{title}")
    log_info(logger, f"Generated at: {format_timestamp()}")
    log_info(logger, separator)


def format_report_footer(logger: logging.Logger) -> None:
    """
    Format and log a report footer.
    
    Args:
        logger: Logger instance
    """
    separator = "=" * 40
    log_info(logger, separator)
    log_info(logger, "")


def log_statistics(logger: logging.Logger, title: str, stats: dict) -> None:
    """
    Log formatted statistics.
    
    Args:
        logger: Logger instance
        title: Statistics section title
        stats: Dictionary containing statistics
    """
    log_info(logger, f"{title}:")
    for key, value in stats.items():
        # Format key as title case with spaces
        formatted_key = key.replace('_', ' ').title()
        
        # Format value based on type
        if isinstance(value, float):
            formatted_value = format_currency(value) if 'amount' in key.lower() or 'total' in key.lower() else f"{value}"
        else:
            formatted_value = str(value)
        
        log_info(logger, f"  {formatted_key}: {formatted_value}")
