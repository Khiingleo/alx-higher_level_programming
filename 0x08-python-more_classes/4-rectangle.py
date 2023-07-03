#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Represents a rectangle object"""

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle object

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle
        Args:
            value (int): the width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the width of the rectangle
        Args:
            value (int): the height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """printable representation of the rectangle using "#" """
        if self.__width == 0 or self.__height == 0:
            return ("")

        result = []
        for i in range(self.__height):
            [result.append("#") for _ in range(self.__width)]
            if i != self.__height - 1:
                result.append('\n')
        return "".join(result)

    def __repr__(self):
        """string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
