"""
Report generator module.
Creates formatted reports from processed data.
"""

import csv
import os
from datetime import datetime

def generate_report(data_file):
    """Generate a formatted report from CSV data"""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Generating report...")
    
    # Check if file exists
    if not os.path.exists(data_file):
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error: File {data_file} not found")
        return
    
    # Read CSV data
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
    
    # Clean and process data
    clean_data = []
    for row in data:
        if row.get('amount') and row.get('product'):
            try:
                amount = float(row['amount'])
                # Round to 2 decimal places
                amount = round(amount * 100) / 100
                row['amount'] = amount
                clean_data.append(row)
            except ValueError:
                continue
    
    # Calculate totals by product
    product_totals = {}
    for row in clean_data:
        product = row['product']
        amount = float(row['amount'])
        if product in product_totals:
            product_totals[product] += amount
        else:
            product_totals[product] = amount
    
    # Round product totals
    for product in product_totals:
        product_totals[product] = round(product_totals[product] * 100) / 100
    
    # Calculate overall statistics
    amounts = [float(row['amount']) for row in clean_data]
    total = sum(amounts)
    average = total / len(amounts) if amounts else 0
    
    # Round results
    total = round(total * 100) / 100
    average = round(average * 100) / 100
    
    # Generate report
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ========== SALES REPORT ==========")
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Total Records: {len(clean_data)}")
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ")
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Product Breakdown:")
    for product, amount in sorted(product_totals.items()):
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]   {product}: ${amount}")
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ")
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Total Sales: ${total}")
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Average Sale: ${average}")
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ==================================\n")
    
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Report generation completed")

if __name__ == "__main__":
    generate_report("sales_data.csv")
