#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """ Check if key exists in dictionary """
    if key in a_dictionary:
        """ Delete if it exists, if not, no change """
        del a_dictionary[key]
    return a_dictionary
