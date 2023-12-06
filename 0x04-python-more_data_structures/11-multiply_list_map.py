#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """ return new list where each value corresponds with
    the original list multiplied by number
    """
    return list(map(lambda x: x * number, my_list))
