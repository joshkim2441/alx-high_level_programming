#!/usr/bin/python3
"""Defines a '4-print_square' module"""


def print_square(size):
    """Prints a square with "#" character with length of size"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
