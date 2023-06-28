#!/usr/bin/python3

import math

"""Defines a magic class"""


class MagicClass:
    """A class that represents a magical circle"""

    def __init__(self, radius=0):
        """
        initializes a magicClass object

        Args:
            radius (float): the radius of the circle
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        calculates the area of a circle

        returns:
            float: the area of the circle
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """
        calculates the circumference of the circle

        Returns:
            floatL the circumference of the circle
        """
        return 2 * math.pi * self.__radius
