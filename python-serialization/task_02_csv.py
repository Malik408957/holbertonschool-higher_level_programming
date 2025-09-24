#!/usr/bin/python3
"""
CSV to JSON conversion module
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON format and save to data.json

    Args:
        csv_filename (str): The name of the CSV file to convert

    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        # Open CSV file and read data using DictReader
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            # DictReader automatically uses first row as fieldnames
            csv_reader = csv.DictReader(csv_file)

            # Convert all rows to a list of dictionaries
            data_list = []
            for row in csv_reader:
                data_list.append(row)

        # Serialize and write to JSON file
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)

        print(f"Successfully converted {csv_filename} to data.json")
        return True

    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False
    except Exception as e:
        print(f"Error during conversion: {e}")
        return False
