#!/usr/bin/python3
"""define a MagicClass matching provided bytecode"""

import math


class MagicClass:
    """representation of a circle"""

    def __init__(self, radius=0):
        """initiate a MagicClass

        Arg:
            radius (float or int): the new MagicClass radius
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        if radius < 0:
            raise ValueError('radius must be >= 0')
        self.__radius = radius

    def area(self):
        """return the area of MagicClass"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """return the MagicClass circumference"""
        return 2 * math.pi * self.__radius
