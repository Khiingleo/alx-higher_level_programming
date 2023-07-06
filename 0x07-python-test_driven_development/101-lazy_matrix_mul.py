#!/usr/bin/python
"""Uses numpy to define a matrix multiplication function"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices

    Args:
        m_a (matrix): the first matrix
        m_b (matrix): the second matrix
    Returns:
        The multiplication of the two matrices
    """

    return np.matmul(m_a, m_b)
