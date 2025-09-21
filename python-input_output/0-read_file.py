#!/usr/bin/python3
"""
0-read_file.py
Function that reads a text file and prints it to stdout
"""

def read_file(filename=""):
    """
    Read a UTF8 text file and print its content to stdout

    Args:
        filename (str): The path to the file to read
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end='')
