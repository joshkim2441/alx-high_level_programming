#!/usr/bin/python3
"""class square that defines a square by private
instance attribute: size
"""


class Square:
    """instantiate an object, set the size attribute"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size  #: size of the square
            """return the area of the square"""
    def area(self):
        return self.__size * self.__size
