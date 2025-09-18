#!/usr/bin/python3
"""
1-my_list.py
Module that defines a custom list class with sorting functionality.
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    Adds a method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        The original list remains unchanged.
        """
        print(sorted(self))
