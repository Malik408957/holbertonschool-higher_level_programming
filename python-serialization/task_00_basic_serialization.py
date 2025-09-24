#!/usr/bin/python3
"""
Basic serialization module
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file

    Args:
        data (dict): Python Dictionary with data
        filename (str): The filename of the output JSON file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize JSON file to recreate Python Dictionary

    Args:
        filename (str): The filename of the input JSON file

    Returns:
        dict: Python Dictionary with the deserialized JSON data
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
