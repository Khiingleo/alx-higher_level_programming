#!/usr/bin/python3
"""Define a class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """
    represents a rectangle instance
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width

        Args:
            value (int): the width
        raises:
            ValueError: if the width is less than 0
            TypeError: if the width is not an integer
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height

        Raises:
            TypeError: if the height is not an integer
            ValueError: if the height is <= 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gets x"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        sets the x co-ordinates of the rectangle

        Raises:
            TypeError: if x is not an integer
            ValueError: if x is < 0
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """gets y"""
        return self.__y

    @y.setter
    def y(self, value):
        """
        sets the y co-ordinates of the rectangle

        Raises:
            The same errors as x
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """uses # to print the rectangle"""
        if self.__width == 0 or self.__height == 0:
            print()

        [print("") for _ in range(self.__y)]
        for _ in range(self.__height):
            [print(" ", end="") for _ in range(self.__x)]
            [print("#", end="") for _ in range(self.__width)]
            print()

    def to_dictionary(self):
        """returns the dictionary representation of the rectangle instance"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
        }

    def __str__(self):
        """returns the str output"""
        message = "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return message.format(type(self).__name__, self.id,
                              self.x, self.y,
                              self.width, self.height)

    def update(self, *args, **kwargs):
        """
        updates the rectangle
        """
        if args:
            num_arg = 0
            for arg in args:
                if num_arg == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif num_arg == 1:
                    self.width = arg
                elif num_arg == 2:
                    self.height = arg
                elif num_arg == 3:
                    self.x = arg
                elif num_arg == 4:
                    self.y = arg
                num_arg += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "height":
                    self.height = value
                elif key == "width":
                    self.width = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
