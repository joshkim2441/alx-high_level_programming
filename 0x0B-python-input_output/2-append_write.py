#!/usr/bin/python3
"""Defines the function append_write"""


def append_write(filename="", text=""):
    """Appends a string at end of a text file (utf-8)
    and returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as file:
        characters_added = file.write(text)
    return characters_added
