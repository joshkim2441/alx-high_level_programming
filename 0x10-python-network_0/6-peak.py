#!/usr/bin/python3
""" A module that finds a peak in a list of unsorted integers """


def find_peak(list_of_ints):
    """ A function that finds a peak in a list of unsorted integers
    Args:
        list_of_ints (list): an integer list
    Return:
        int: peak(s)
    """
    _list = list_of_ints
    if _list == []:
        return None
    lgt = len(_list)

    start, end = 0, lgt - 1
    while start < end:
        mid = start + (end - start) // 2
        if _list[mid] > _list[mid - 1] and _list[mid] > _list[mid + 1]:
            return _list[mid]
        if _list[mid - 1] > _list[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return _list[start]
