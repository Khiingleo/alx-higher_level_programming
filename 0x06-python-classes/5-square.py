#!/usr/bin/python3

"""Defines a class Square"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """
        Initialize a square object

        Args:
            size (int): The size of the square
        """
        self.size = size

    @property
    def size(self):
        """
        Get the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square

        Args:
            value (int): size of the square
        Raises:
            TypeError: if the size is not an integer
            ValueError: if the size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square

        Returns:
            int: the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        prints the square with the char #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                [print("#", end="") for j in range(self.__size)]
                print()
