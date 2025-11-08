# db_utils.py
"""Database utilities for secure data access."""
import sqlite3
from typing import List, Tuple, Any


def execute_safe_query(db_path: str, query: str, params: Tuple[Any, ...]) -> List[Tuple]:
    """
    Execute a parameterized SQL query safely.
    
    Args:
        db_path: Path to SQLite database
        query: SQL query with ? placeholders
        params: Tuple of parameters to bind safely
        
    Returns:
        List of result tuples
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results
