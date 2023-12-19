#!/usr/bin/python3
"""size is a private instance in this class"""


class Square:
    """instantiate an object"""
    def __init__(self, size=0):
        """set the size attribute during the
        creation of the object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size  #: size of the square
