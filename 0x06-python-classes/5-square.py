#!/usr/bin/python3
"""define a class that defines a Square"""


class Square:
    """a class Square that defines a square"""
    def __init__(self, size=0):
        """initiate a square

        Args:
            value (int): the size of the square
        """
        self.__size = size

    @property
    def size(self):
        """initiate: Private size

        Returns:
            Private size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """sets a value into size, it must be an int

        Args:
            value (int): the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size * self.__size

    def area(self):
        """Returns the area

        Returns:
            area
        """
        return self.__size * self.__size

    def my_print(self):
        """prints the square with the character # in stdout"""

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
