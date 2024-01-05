#!/usr/bin/python3
"""
This defines a "2-matrix_divided" module.
"""


def matrix_divided(matrix, div):
    """Divides all elements in the matrix by div

    Args:
        matrix (list): A list of lists of ints/floats
    Raises:
        TypeError: If the matrix contains non-numbers
                                          rows of different sizes
                       div is not an int/float
        ZerDivisionError: If the div is 0
    Retruns:
        A new matrix that represents the result of division
    """
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(row)
        elif size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]
