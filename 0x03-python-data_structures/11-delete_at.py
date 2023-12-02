#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    # Check if list is neg or out of range
    if idx < 0 or idx >= len(my_list):
        # Return original list
        return my_list
    else:
        del my_list[idx]
    # Use list slicing to create new list including
    # all elements of my_list upto idx, followed by
    # all elements of my_list after idx
    return my_list
