#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """Prevents the user from dynamically creating
    new instance attributes unless it is called ``first_name``
    """


__slots__ = ['first_name']
