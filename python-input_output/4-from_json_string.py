#!/usr/bin/python3
"""
4-from_json_string.py
Function that returns an object represented by a JSON string
"""

import json


def from_json_string(my_str):
    """
    Return the Python object represented by a JSON string

    Args:
        my_str (str): The JSON string to deserialize

    Returns:
        object: Python data structure represented by the JSON string
    """
    return json.loads(my_str)
