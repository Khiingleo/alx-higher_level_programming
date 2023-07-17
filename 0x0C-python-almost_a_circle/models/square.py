#!/usr/bin/python3
"""Defines a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square instance
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initializes a new square instance

        Args:
            size (int): the size of the square
            x (int): the x axis
            y (int): the y axis
            id: the square id (default is None)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        updates the attributes of the class Square
        """
        if args:
            arg_num = 0
            for arg in args:
                if arg_num == 0:
                    self.id = arg
                elif arg_num == 1:
                    self.size = arg
                elif arg_num == 2:
                    self.x = arg
                elif arg_num == 3:
                    self.y = arg
                arg_num += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a square instance"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
        }

    def __str__(self):
        """
        returns the str() representation of the square
        """
        message = "[{:s}] ({:d}) {:d}/{:d} - {:d}"
        return message.format(type(self).__name__, self.id,
                              self.x, self.y, self.size)
