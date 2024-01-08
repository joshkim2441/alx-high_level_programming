#!/usr/bin/python3
"""Defines a class square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representeation of a square"""

    def __init__(self, size):
        """Initialize the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Informal string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
