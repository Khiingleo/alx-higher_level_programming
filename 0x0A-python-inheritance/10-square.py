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
