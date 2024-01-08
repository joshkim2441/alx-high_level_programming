#!/usr/bin/python3
"""Defines inherits_from function"""


def inherits_from(obj, a_class):
    """Returns true if object is an instance of a class
    inherited dierectly/directly from specified class"""

    return issubclass(type(obj), a_class) and type(obj) is not a_class
