#!/usr/bin/python3
"""
Function to return dictionary description for JSON serialization
"""

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure 
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class

    Returns:
        dict: Dictionary containing serializable attributes
    """
    # Serializable data types
    serializable_types = (list, dict, str, int, bool)

    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, serializable_types):
            result[key] = value
    return result
