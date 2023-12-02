#!/usr/bin/python


def max_integer(my_list=[]):
    # check if list is empty
    if len(my_list) == 0:
        return None
    # Initialize variable to first element of list
    max_num = my_list[0]
    # Iterate over the rest of the list
    for num in my_list:
        if num > max_num:
            # Update variable if larger int found
            max_num = num
    return max_num
