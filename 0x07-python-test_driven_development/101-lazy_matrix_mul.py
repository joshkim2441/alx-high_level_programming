#!/usr/bin/python3
"""Defines the lazy_matrix module"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Calculates matrix multiplication of two matrices
    Args:
        m_a: matrix a
        m_b: matrix b
    Return:
        The result of the multiplication
    """
    return (numpy.matmul(m_a, m_b))
