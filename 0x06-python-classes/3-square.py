#!/usr/bin/python3
"""class Square that defines a square
"""


class Square:
    """represents a class Square"""
    def __init__(self, size=0):
        """initialize the Square
        Args:
            size (int): the size of the Square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size  #: size of the square
            """return the area of the square"""
    def area(self):
        return self.__size * self.__size
