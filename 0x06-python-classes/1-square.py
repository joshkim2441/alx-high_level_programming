#!/usr/bin/python3
"""size is a private instance attribute in
this class
"""
class Square:
    """instantiate an object"""
    def __init__(self, size):
        """set the size attribute during
        the creation of an object
        """
        self.__size = size #: size of the square
