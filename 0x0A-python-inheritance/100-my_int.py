#!/usr/bin/python3
"""Defines a class MyInt that inherits fr-om int"""


class MyInt(int):
    """
    a representation of a subclass of int
    """
    def __init__(self, number):
        """
        initializes a MyInt object

        Args:
            number (int): the number passed
        """
        self.number = number

    def __ne__(self, other_num):
        """
        inverted __eq__ operator

        Args:
            other_num (int): the number to compare with
        """
        return self.number == other_num

    def __eq__(self, other_num):
        """
        inverted __ne__ operator

        Args:
            other_num (int): the number to compare with
        """
        return self.number != other_num
