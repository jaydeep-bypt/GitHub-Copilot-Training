"""
Data cleaning module.
Handles data validation, cleaning, and normalization.
"""

import csv
import os
from datetime import datetime

def clean_csv_data(input_file, output_file):
    """Clean CSV data and write to output file"""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting data cleaning process...")
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error: Input file {input_file} not found")
        return False
    
    # Read input data
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Reading data from {input_file}...")
    data = []
    try:
        with open(input_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except Exception as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error reading file: {e}")
        return False
    
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Loaded {len(data)} records")
    
    # Clean and validate data
    clean_data = []
    invalid_count = 0
    
    for row in data:
        # Validate required fields
        if not row.get('amount') or not row.get('quantity') or not row.get('product'):
            invalid_count += 1
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Skipping row with missing fields")
            continue
        
        try:
            # Clean and convert numeric fields
            amount = float(row['amount'])
            quantity = int(row['quantity'])
            
            # Round amount to 2 decimal places
            amount = round(amount * 100) / 100
            
            # Validate ranges
            if amount < 0 or quantity < 0:
                invalid_count += 1
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Skipping row with negative values")
                continue
            
            # Clean product name (remove extra whitespace)
            product = ' '.join(row['product'].split())
            
            # Create cleaned row
            clean_row = {
                'date': row.get('date', ''),
                'product': product,
                'amount': amount,
                'quantity': quantity
            }
            clean_data.append(clean_row)
            
        except (ValueError, TypeError) as e:
            invalid_count += 1
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Skipping row with invalid data: {e}")
            continue
    
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Cleaned {len(clean_data)} records, skipped {invalid_count} invalid records")
    
    # Write cleaned data to output file
    if clean_data:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Writing cleaned data to {output_file}...")
        try:
            with open(output_file, 'w', newline='') as file:
                fieldnames = ['date', 'product', 'amount', 'quantity']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(clean_data)
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Data cleaning completed successfully")
            return True
        except Exception as e:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error writing output file: {e}")
            return False
    else:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] No valid data to write")
        return False

def validate_data_file(filename):
    """Validate a CSV data file"""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Validating {filename}...")
    
    if not os.path.exists(filename):
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] File does not exist")
        return False
    
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] File contains {len(rows)} rows")
        
        # Check for required fields
        required_fields = ['date', 'product', 'amount', 'quantity']
        if rows:
            missing = [field for field in required_fields if field not in rows[0]]
            if missing:
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Missing required fields: {missing}")
                return False
        
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Validation passed")
        return True
        
    except Exception as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Validation error: {e}")
        return False

if __name__ == "__main__":
    clean_csv_data("sales_data.csv", "sales_data_clean.csv")
