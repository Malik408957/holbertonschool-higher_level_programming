#!/usr/bin/python3
"""
1-write_file.py
Function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file and return number of characters written

    Args:
        filename (str): The path to the file
        text (str): The text to write to the file

    Returns:
        int: Number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        chars_written = file.write(text)
        return chars_written
