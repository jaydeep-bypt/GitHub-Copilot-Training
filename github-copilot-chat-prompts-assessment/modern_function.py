import asyncio
import csv
from typing import Dict, List, Any
import sys
import os

async def process_user_data(filename: str) -> Dict[str, Any]:
    """
    Reads a CSV file of user data and returns a summary by city.
    Each city contains a count of users and a list of their ages.
    """
    summary: Dict[str, Any] = {}
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File not found: {filename}")
    try:
        # Async file reading
        loop = asyncio.get_event_loop()
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row.get('name')
                age = row.get('age')
                city = row.get('city')
                if not city or not age:
                    continue
                if city not in summary:
                    summary[city] = {'count': 0, 'ages': []}
                summary[city]['count'] += 1
                try:
                    summary[city]['ages'].append(int(age))
                except ValueError:
                    pass
        return summary
    except Exception as e:
        print(f"Error processing file: {e}")
        return {}

async def main():
    import argparse
    parser = argparse.ArgumentParser(description="Process user data CSV and summarize by city.")
    parser.add_argument('filename', nargs='?', default='sample_users.csv', help='CSV file to process')
    args = parser.parse_args()
    result = await process_user_data(args.filename)
    if result:
        print("Summary by city:")
        for city, data in result.items():
            print(f"{city}: {data['count']} users, ages: {data['ages']}")
    else:
        print("No data processed.")

if __name__ == "__main__":
    # Create a sample CSV for demonstration if not present
    sample_csv = "sample_users.csv"
    if not os.path.exists(sample_csv):
        with open(sample_csv, 'w', newline='') as f:
            f.write("name,age,city\nAlice,30,New York\nBob,25,Los Angeles\nCharlie,notanumber,New York\nDana,40,Chicago\nEve,35,Los Angeles\n")
    asyncio.run(main())
