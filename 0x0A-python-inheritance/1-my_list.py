#!/usr/bin/python3
"""Defines a public instance ``print_sorted`` method"""


class MyList(list):
    """Defines a class MyList"""

    def print_sorted(self):
        """Defines a public instance mehtod that prints
        the sorted list in ascending sort"""
        print(sorted(self))
