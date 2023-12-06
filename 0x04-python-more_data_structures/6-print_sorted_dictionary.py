#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """ sort the keys using 'sorted' function """
    for key in sorted(a_dictionary):
        """ print each key-value pair in alphabetical order """
        print("{}: {}".format(key, a_dictionary[key]))
