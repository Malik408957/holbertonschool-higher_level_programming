#!/usr/bin/python3
def uppercase(str):
    """Convert a string to uppercase"""
    for char in str:
        diff = 32 if 97 <= ord(char) <= 122 else 0
        print("{:c}".format(ord(char) - diff), end="")
    print()
