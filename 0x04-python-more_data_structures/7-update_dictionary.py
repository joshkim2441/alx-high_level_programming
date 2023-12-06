#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """ replace value of key if it exists, if not, create it """
    a_dictionary[key] = value
    return a_dictionary
