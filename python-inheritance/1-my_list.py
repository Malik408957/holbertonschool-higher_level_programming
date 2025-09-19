#!/usr/bin/python3
"""MyList modulu"""


class MyList(list):
    """list sinfindən miras alan sinif"""

    def print_sorted(self):
        """Listəni çeşidləyib çap edir"""
        print(sorted(self))
