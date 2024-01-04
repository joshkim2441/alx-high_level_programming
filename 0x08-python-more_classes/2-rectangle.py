#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """A class representing a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with optional width and height."""
        self._width = width
        self._height = height

    @property
    def width(self):
        """Getter for the width attribute."""
        return self._width

    @width.setter
    def width(self, value):
        """Setter for the width attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self._height

    @height.setter
    def height(self, value):
        """Setter for the height attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Calculate and return the rectangle area."""
        return self._width * self._height

    def perimeter(self):
        """Calculate and return the rectangle perimeter."""
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

