#!/usr/bin/python3
"""Defines a "5-text_indentation" function"""


def text_indentation(text):
    """ Prints 2 new lines after ".?:" characters
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    string = text[:]

    for j in ".?:":
        list_text = string.split(j)
        string = ""
        for a in list_text:
            a = a.strip(" ")
            string = a + j if string is "" else string + "\n\n" + a + j

    print(string[:-3], end="")
