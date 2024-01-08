#!/usr/bin/python3
"""Defines ``is_kind_of_class`` function"""


def is_kind_of_class(obj, a_class):
    """Returns True if object is an instance of, or instance
    of class inherited from, the specified class"""

    return isinstance(obj, a_class)
