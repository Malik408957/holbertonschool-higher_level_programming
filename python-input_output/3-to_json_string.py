#!/usr/bin/python3
"""
3-to_json_string.py
Function that returns the JSON representation of an object
"""

import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object as a string

    Args:
        my_obj: The Python object to serialize

    Returns:
        str: JSON string representation of the object
    """
    return json.dumps(my_obj)
