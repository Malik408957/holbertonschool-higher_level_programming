#!/usr/bin/python3
"""
5-save_to_json_file.py
Function that writes an Object to a text file using JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using JSON representation

    Args:
        my_obj: The Python object to serialize and write
        filename (str): The path to the file to write to
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
