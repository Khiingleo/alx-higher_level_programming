#!/usr/bin/python3
"""Defines a matrix multiplication function"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices

    Args:
        m_a (matrix): the first matrix
        b_a (matrix): the second matrix
    Raises:
        TypeError: if m_a or m_b are not list of lists of int/floats
        TypeError: If m_b or m_b is empty
        TypeError: if m_a or m_b rows are different sizes
        ValueError: if m_a and m_b can't be multiplied
    Returns:
        matrix: a new matrix containing the result of the multiplication
    """
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(rows, list) for rows in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(rows, list) for rows in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all(isinstance(num, (int, float)) for rows in m_a for num in rows):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for rows in m_b for num in rows):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            elem = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(elem)
        result.append(row)

    return result
