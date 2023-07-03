#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Represents a rectangle object"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle object

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        compares the area between two rectangles

        Args:
            rect_1: the first rectangle
            rect_2: the second rectangle
        Returns:
            the rect_1 if both have the same value area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        a class method that returns a new rectangle

        Args:
            size (int): the size of the new rectangle
        """
        return cls(size, size)

    def __str__(self):
        """printable representation of the rectangle using "#" """
        if self.__width == 0 or self.__height == 0:
            return ("")

        res = []
        for i in range(self.__height):
            [res.append(str(self.print_symbol)) for _ in range(self.__width)]
            if i != self.__height - 1:
                res.append('\n')
        return "".join(res)

    def __repr__(self):
        """string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """destructor for the rectangle object"""
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1
