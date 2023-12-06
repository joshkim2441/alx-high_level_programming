#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """ return new dictionary where all keys associated with given
    value have been deleted, if value doesn't exist, the
    dicionary doesn't change
    """
    return {key: val for key, val in a_dictionary.items() if val != value}
