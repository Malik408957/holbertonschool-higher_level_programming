#!/usr/bin/python3
"""
This module contains a function that checks if an object is an instance
of a class that inherited from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if object is an instance of a class that inherited from specified class

    Args:
        obj: Object to check
        a_class: Class to check inheritance from

    Returns:
        bool: True if obj is instance of subclass, False otherwise
    """
    return isinstance(obj, a_class) and type(obj) != a_class
