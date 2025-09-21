#!/usr/bin/python3
"""
2-append_write.py
Function that appends a string to a text file
"""


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file and return number of characters added

    Args:
        filename (str): The path to the file
        text (str): The text to append to the file

    Returns:
        int: Number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as file:
        chars_added = file.write(text)
        return chars_added
