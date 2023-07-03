#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor

    Args:
        matrix (list): The matrix to be divided
        div (int/float): the divisor
    Returns:
        A new matrix with the result of the previus matrix's elements
        divided by the divisor
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or matrix == [] or \
            not all(isinstance(row, list) for row in matrix) or \
            not all(isinstance(num, (int, float))
                    for row in matrix for num in row):
        raise TypeError(message)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = []
    for row in matrix:
        result = [round(num / div, 2) for num in row]
        new.append(result)

    return new
