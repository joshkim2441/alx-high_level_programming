#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    """ Return a new matrix of same size, where each vlaue is the
    square of the corresponding value in the matrix
    Initial matrix is not modified
    """
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
