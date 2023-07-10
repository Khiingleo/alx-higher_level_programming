#!/usr/bin/python3
"""Defines a class Rectangle that inherits fro-m BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    representation of a rectangle object
    """
    def __init__(self, width, height):
        """
        initializes a new rectangle instance

        Args:
            width (int): the width (must be positive)
            height (int); the height (must be positive)
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
