#!/usr/bin/python3

"""Defines a sqaure class"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square object

        Args:
            size (int): the size of the square
            position (tuple): the position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size of the square

        Args:
            value (int): the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets the position of the square

        Args:
            value (tuple): the position of the square
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        calculates the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        prints the square using '#' char

        if size is 0, prints an empty line
        Uses the position to adjust the printing
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            [print(" ", end="") for _ in range(self.__position[0])]
            [print("#", end="") for _ in range(self.__size)]
            print()

    def __str__(self):
        """Define the way the square is printef"""
        if self.__size != 0:
            [print() for _ in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for _ in range(self.__position[0])]
            [print("#", end="") for _ in range(self.__size)]
            if i != self.__size - 1:
                print()
        return ("")
