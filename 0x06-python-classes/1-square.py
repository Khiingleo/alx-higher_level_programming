#!/usr/bin/python3

"""
Defines a class square
with a private instance attribute size
"""


class Square:
    """A class that represents a square."""

    def __init__(self, size):
        """

        Initializes a Square object

        Args:
            size (int): The size of the square
        """
        self.__size = size
