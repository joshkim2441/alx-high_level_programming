#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """ return new dictionary where all keys associated with given
    value have been deleted, if value doesn't exist, the
    dicionary doesn't change
    """
    for key in list(a_dictionary):
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
