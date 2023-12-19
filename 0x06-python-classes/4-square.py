#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """represents a class Square"""
    def __init__(self, size=0):
        """initialize the Square
        Args:
            value (int): the size of the Square
        """
        self.size = size

    @property
    def size(self):
        """int: private size

        Returns:
            Private size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value into size, it must be an int

        Args:
            value (int): the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns the area

        Returns:
              area
        """
        return self.__size * self.__size
