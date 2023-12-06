#!/usr/bin/python3
def best_score(a_dictionary):
    """ Use max function to find key with maximum value
    set the key argument to 'a_dictionary.get' to compare values
    """
    return max(a_dictionary, key=a_dictionary.get) if a_dictionary else None
