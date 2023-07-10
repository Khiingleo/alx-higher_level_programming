#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """
    A class that represents base geometry
    """
    def area(self):
        """
        raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates 'Value'

        Args:
            name (string): the name
            value (int): the value
        Raises:
            TypeError: if value is not an integer
            ValueError: ig value is less than or equal to 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
