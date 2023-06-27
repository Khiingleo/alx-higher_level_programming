#!/usr/bin/python3

"""Defines a class Square"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square object

        Args:
            size (int): The size of the square
            position (int, int): the position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square

        Args:
            value (int): the size of thes square
        Raises:
            TypeError: if size is not an integer
            ValueError: if the size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the postion of the square

        Args:
            value (int): position
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using '#' char

        if size is 0, prints an empty line
        Uses position to adjust the printing
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                [print(" ", end="") for _ in range(self.__position[0])]
                [print("#", end="") for _ in range(self.__size)]
                print()
