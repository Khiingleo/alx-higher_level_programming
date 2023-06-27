#!/usr/bin/python3

"""Defines a class square"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """
        Initializes a square object

        Args:
            size (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of a square

        Returns:
            int: The area of the square
        """
        return self.__size * self.__size
