#!/usr/bin/python3

"""Defines a class square"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """
        Initializes a class object

        Args:
            size (int): the size of the square
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square

        Args:
            value (int): the size of the square
        Raises:
            TypeError: value is not integer
            ValueError: value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        calculates the area of the square

        Returns:
            int: the area of the square
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """compare and return if equal"""
        return self.size == other.size

    def __ne__(self, other):
        """compare and return if not equal"""
        return self.size != other.size

    def __lt__(self, other):
        """compare and return if less than"""
        return self.size < other.size

    def __le__(self, other):
        """compare and return if less than or equal to"""
        return self.size <= other.size

    def __gt__(self, other):
        """compare and return if greater than"""
        return self.size > other.size

    def __ge__(self, other):
        """compare and return if greater than or equal to"""
        return self.size >= other.size
