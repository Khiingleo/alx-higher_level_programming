#!/usr/bin/python3
"""Defines a Base class"""


class Base:
    """
    represents a Base object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializes a new Base

        Args:
            id (int): The Base id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
