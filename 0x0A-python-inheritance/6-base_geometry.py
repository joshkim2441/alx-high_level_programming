#!/usr/bin/python3
"""Defines the BaseGeometry class"""


class BaseGeometry:
    """Representation of base geometry"""

    def area(self):
        """Raises an exception if area is not implemented"""
        raise Exception("area() is not implemented")
