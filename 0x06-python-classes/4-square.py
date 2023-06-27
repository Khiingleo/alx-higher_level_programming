#!/usr/bin/python3

"""Defines a class square"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """
        Initialize a square object

        Args:
            size (int): The size of the square
        """
        self.size = size

    @property
    def size(self):
        """
        Get the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square

        Args:
            value (int): The size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of a square

        Returns:
            int: the area of the square
        """
        return self.__size * self.__size
