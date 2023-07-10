#!/usr/bin/python3

"""Defines a class Square that inherits fr-om the class Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Representation of a square object
    """
    def __init__(self, size):
        """
        initializes a new square object

        Args:
            size (int): the size of the square (must be positive)
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        returns the string representation of the square object
        """
        return "[{:s}] {:d}/{:d}".format(type(self).__name__,
                                        self.__size, self.__size)
