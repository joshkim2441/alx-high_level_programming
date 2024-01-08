#1/usr/bin/python3
"""Defines ``lookup`` function"""


def lookup(obj):
    """Returns a list of available attributes
    and methods of an object
    """
    return dir(obj)
