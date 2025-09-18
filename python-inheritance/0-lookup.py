#!/usr/bin/python3
"""
0-lookup.py
Module that returns the list of available attributes and methods of an object.
"""

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: Any Python object to inspect

    Returns:
        list: List of attributes and method names
    """
    return dir(obj)
