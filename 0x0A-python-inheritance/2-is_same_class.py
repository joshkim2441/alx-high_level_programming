#!/usr/bin/python3
"""Defines the function "is_same_class" """


def is_same_class(obj, a_class):
    """Returns ``True`` if object is exactly an
    instance of the specified class, otherwise ``False`` """
    return type(obj) is a_class
