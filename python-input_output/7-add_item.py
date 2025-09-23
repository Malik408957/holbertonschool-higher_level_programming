#!/usr/bin/python3
"""
Script to add arguments to a list and save to JSON file
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def main():
    """Main function"""
    filename = "add_item.json"

    # Try to load existing items, if file doesn't exist, create empty list
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    # Add new arguments to the list (skip the first argument which is script name)
    items.extend(sys.argv[1:])

    # Save the updated list to file
    save_to_json_file(items, filename)

if __name__ == "__main__":
    main()
