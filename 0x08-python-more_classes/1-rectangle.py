#!/usr/bin/python3

"""Defines a class Rectangle"""


class Rectangle:
    """
    Represents a rectangle object
    """
    def __init__(self, width=0, height=0):
        """
        initializes a rectangle object

        Args:
            width (int): the width of the rectangle object
            height (int): the height of the rectangle object
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle

        Returns:
            the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width of the rectangle

        Args:
            value (int): the width of the rectangle
        Raises:
            TypeError: if the width is not an integer
            ValueError: if the width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the width of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height of the rectangle

        Args:
            value (int): the height of the rectangle
        Raises:
            TypeError: if the height is not an integer
            ValueError: if the height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
