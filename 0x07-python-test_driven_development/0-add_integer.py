#!/usr/bin/python3
"""Defines a function to add integers and/or float"""


def add_integer(a, b=98):
    """Function that adds two integers and/or float number
    Args:
        a: the first number
        b: the second number

    Return:
        the addition of the integers a and b

    Before addition float arguments are typecast to ints

    Raises:
        TypeError: If either a or b is not an integer or float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
