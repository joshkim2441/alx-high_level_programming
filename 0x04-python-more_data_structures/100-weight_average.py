#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    """ Each tuple in the list should contain two integers:
        a score and a weight
        """
    return sum(x[0] * x[1] for x in my_list) / sum(x[1] for x in my_list)
