#!/usr/bin/python3

"""
Defines a function that adds two integers
"""


def add_integer(a, b=98):
    """
    adds two integers

    Args:
        a (int/float): the first integer or float.
        b (int/float): the second integer or float.
    Returns:
        int: the addition of a and b
    Raises:
        TypeError: If a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
