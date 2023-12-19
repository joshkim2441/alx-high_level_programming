#!/usr/bin/python3
"""define square with private instance: size"""
class Square:
    """instantiate an object, set the size
    during creation of a square object
    """
    def __init__(self, size=0):
        self.__size = size
        """get the value of size with type
        and value checks"""
    @property
    def size(self):
        return self.__size
    """set the value of size with type
    and value checks"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size * self.__size
            """return the area of the square"""
    def area(self):
        return self.__size * self.__size
    """print the square using character # or
    empty line if size is 0
    """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
