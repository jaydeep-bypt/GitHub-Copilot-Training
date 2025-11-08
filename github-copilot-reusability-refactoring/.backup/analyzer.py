"""
Data analyzer module.
Performs statistical analysis and calculations on data.
"""

import csv
import os
from datetime import datetime

def analyze_sales_data(data_file):
    """Analyze sales data and calculate statistics"""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting data analysis...")
    
    # Check if file exists
    if not os.path.exists(data_file):
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error: File {data_file} not found")
        return None
    
    # Read CSV data
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Loading data from {data_file}...")
    data = []
    try:
        with open(data_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except Exception as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error reading file: {e}")
        return None
    
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Loaded {len(data)} records")
    
    # Clean and convert data
    amounts = []
    quantities = []
    
    for row in data:
        try:
            if row.get('amount'):
                amount = float(row['amount'])
                # Round to 2 decimal places
                amount = round(amount * 100) / 100
                amounts.append(amount)
            
            if row.get('quantity'):
                quantity = int(row['quantity'])
                quantities.append(quantity)
        except (ValueError, TypeError):
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Skipping invalid row")
            continue
    
    # Calculate amount statistics
    amount_stats = {}
    if amounts:
        total_amount = sum(amounts)
        avg_amount = total_amount / len(amounts)
        min_amount = min(amounts)
        max_amount = max(amounts)
        
        # Round results
        amount_stats = {
            'total': round(total_amount * 100) / 100,
            'average': round(avg_amount * 100) / 100,
            'min': round(min_amount * 100) / 100,
            'max': round(max_amount * 100) / 100,
            'count': len(amounts)
        }
    
    # Calculate quantity statistics
    quantity_stats = {}
    if quantities:
        total_qty = sum(quantities)
        avg_qty = total_qty / len(quantities)
        min_qty = min(quantities)
        max_qty = max(quantities)
        
        # Round results
        quantity_stats = {
            'total': total_qty,
            'average': round(avg_qty * 100) / 100,
            'min': min_qty,
            'max': max_qty,
            'count': len(quantities)
        }
    
    # Calculate product-wise statistics
    product_stats = {}
    for row in data:
        try:
            product = row.get('product')
            amount = float(row.get('amount', 0))
            quantity = int(row.get('quantity', 0))
            
            # Round amount
            amount = round(amount * 100) / 100
            
            if product:
                if product not in product_stats:
                    product_stats[product] = {
                        'total_amount': 0,
                        'total_quantity': 0,
                        'count': 0
                    }
                
                product_stats[product]['total_amount'] += amount
                product_stats[product]['total_quantity'] += quantity
                product_stats[product]['count'] += 1
        except (ValueError, TypeError):
            continue
    
    # Round product totals
    for product in product_stats:
        product_stats[product]['total_amount'] = round(product_stats[product]['total_amount'] * 100) / 100
        avg = product_stats[product]['total_amount'] / product_stats[product]['count']
        product_stats[product]['average_amount'] = round(avg * 100) / 100
    
    # Print analysis results
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ========== ANALYSIS RESULTS ==========")
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ")
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Amount Statistics:")
    if amount_stats:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]   Total: ${amount_stats['total']}")
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]   Average: ${amount_stats['average']}")
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]   Min: ${amount_stats['min']}")
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]   Max: ${amount_stats['max']}")
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]   Count: {amount_stats['count']}")
    
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ")
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Quantity Statistics:")
    if quantity_stats:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]   Total: {quantity_stats['total']}")
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]   Average: {quantity_stats['average']}")
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]   Min: {quantity_stats['min']}")
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]   Max: {quantity_stats['max']}")
    
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ")
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Product Statistics:")
    for product, stats in sorted(product_stats.items()):
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]   {product}:")
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]     Total Sales: ${stats['total_amount']}")
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]     Average Sale: ${stats['average_amount']}")
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]     Total Quantity: {stats['total_quantity']}")
    
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ======================================\n")
    
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Analysis completed successfully")
    
    return {
        'amount_stats': amount_stats,
        'quantity_stats': quantity_stats,
        'product_stats': product_stats
    }

if __name__ == "__main__":
    analyze_sales_data("sales_data.csv")
