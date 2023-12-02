#!/usr/bin/python


def max_integer(my_list=[]):
    # check if list is empty
    if my_list:
        my_list.sort()
        return (my_list[-1])
    else:
        return None
