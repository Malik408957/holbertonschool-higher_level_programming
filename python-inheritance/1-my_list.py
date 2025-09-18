#!/usr/bin/python3
"""
1-my_list.py
Module that defines a custom list class with sorting functionality.
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    Adds a method to print and return the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        Returns a new sorted list.
        The original list remains unchanged.

        Returns:
            list: New sorted list
        """
        sorted_list = sorted(self)
        print(sorted_list)
        return sorted_list
