#!/usr/bin/python3
"""defines a class square"""


class Square:
    """a class square that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize the class Square

        Args:
            size (int): the size of the new Square
            position (int, int): position of new Square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """get the current size of the Square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """set the current size of the Square"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or
        len(value) != 2 or
        not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 + ints")
        else:
            self.__position = value

    def area(self):
        """Return the area of the Square"""
        return self.__size * self.__size

    def my_print(self):
        """print the Square using the character #"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
