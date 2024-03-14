#!/usr/bin/python3
"""Defines a function to add integers and/or float"""


def add_integer(a, b):
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
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
