"""
Main entry point for data processing pipeline.
Orchestrates data cleaning, analysis, and report generation.
"""

import csv
import os
from datetime import datetime

def main():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting data processing pipeline...")
    
    # Check if data file exists
    data_file = "sales_data.csv"
    if not os.path.exists(data_file):
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Creating sample data file...")
        create_sample_data(data_file)
    
    # Read data from CSV
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Reading data from {data_file}...")
    data = []
    try:
        with open(data_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except Exception as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error reading file: {e}")
        return
    
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Loaded {len(data)} records")
    
    # Clean the data
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Cleaning data...")
    clean_data = []
    for row in data:
        if row.get('amount') and row.get('quantity'):
            try:
                amount = float(row['amount'])
                quantity = int(row['quantity'])
                # Round to 2 decimal places
                amount = round(amount * 100) / 100
                row['amount'] = amount
                row['quantity'] = quantity
                clean_data.append(row)
            except ValueError:
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Skipping invalid row")
    
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Cleaned data: {len(clean_data)} valid records")
    
    # Calculate basic statistics
    amounts = [float(row['amount']) for row in clean_data]
    if amounts:
        total = sum(amounts)
        average = total / len(amounts)
        minimum = min(amounts)
        maximum = max(amounts)
        
        # Round results
        total = round(total * 100) / 100
        average = round(average * 100) / 100
        minimum = round(minimum * 100) / 100
        maximum = round(maximum * 100) / 100
        
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Statistics calculated successfully")
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Total: ${total}")
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Average: ${average}")
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Min: ${minimum}")
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Max: ${maximum}")
    
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Pipeline completed successfully")

def create_sample_data(filename):
    """Create sample CSV data for testing"""
    data = [
        {'date': '2025-01-01', 'product': 'Widget A', 'amount': '125.50', 'quantity': '10'},
        {'date': '2025-01-02', 'product': 'Widget B', 'amount': '87.25', 'quantity': '5'},
        {'date': '2025-01-03', 'product': 'Widget C', 'amount': '210.00', 'quantity': '15'},
        {'date': '2025-01-04', 'product': 'Widget A', 'amount': '156.75', 'quantity': '12'},
        {'date': '2025-01-05', 'product': 'Widget D', 'amount': '99.99', 'quantity': '8'},
    ]
    
    with open(filename, 'w', newline='') as file:
        fieldnames = ['date', 'product', 'amount', 'quantity']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    main()
