#!/usr/bin/python3
"""Defines class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation of class Square"""
    def __init__(self, size):
        """Initialize a square"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
