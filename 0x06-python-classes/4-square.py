#!/usr/bin/python3
"""deifine class square with private instance: size"""


class Square:
    """instantiate an object, set size attribute
    during creation of square object
    """
    def __init__(self, size=0):
        self.size = size
        """get the value of size with type and value checks"""
    @property
    def size(self):
        return self.__size
    """set the value of size with type and value checks"""

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
            """return tha area of the square"""
    def area(self):
        return self.__size * self.__size
