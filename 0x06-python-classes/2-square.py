#!/usr/bin/python3
"""defines a class Square"""


class Square:
    """class Square that represents a square"""
    def __init__(self, size=0):
        """initialize the Square
        Args:
            size (int): the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size  #: size of the square
