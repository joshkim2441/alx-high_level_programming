#!/usr/bin/python3
"""
Defines the matrix_mul function
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices(lists of lists of ints and floats)"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    list1 = len(m_a)
    if list1 == 0:
        raise ValueError("m_a can't be empty")
    list2 = None
    for a in m_a:
        if type(a) is not list:
            raise TypeError("m_a must be a list of lists")
        if list2 is None:
            list2 = len(a)
            if list2 == 0:
                raise ValueError("m_a can't be empty")
        if list2 != len(a):
            raise TypeError("each row of m_a must be of the same size")
        for b in a:
            if type(b) is not int and type(b) is not float:
                raise TypeError("m_a should contain only integers or floats")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    list3 = None
    for a in m_b:
        if type(a) is not list:
            raise TypeError("m_b must be a list of lists")
        if list3 is None:
            list3 = len(a)
            if list3 == 0:
                raise ValueError("m_b can't be empty")
        if list3 != len(a):
            raise TypeError("each row of m_b must be of the same size")
        for b in a:
            if type(b) is not int and type(b) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if list2 != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    matrix = []
    for a in range(list1):
        c = []
        for b in range(list3):
            m = 0
            for d in range(list2):
                m += m_a[a][d] * m_b[d][b]
            c.append(m)
        matrix.append(c)
    return matrix
