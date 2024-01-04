#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """A class representing a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize a rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the width property."""
        return self._width

    @width.setter
    def width(self, value):
        """Setter for the width property."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Getter for the height property."""
        return self._height

    @height.setter
    def height(self, value):
        """Setter for the height property."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
