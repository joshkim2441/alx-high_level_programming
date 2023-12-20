#!/usr/bin/python3
"""defines a class Square"""


class Square:
    """represents a class Square"""
    def __init__(self, size=0):
        """initiate a class square

        Args:
            value (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """int: private size

        Returns:
            private size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ssets a value into size, must be an int

        Args:
            value (int): size of the square
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area

        Returns:
            area
        """
        return self.__size ** 2

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented
