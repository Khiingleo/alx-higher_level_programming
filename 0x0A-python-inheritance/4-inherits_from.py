#!/usr/bin/python3
"""Defines a function that returns true if the object is an instance
of a class that inherited fr-om the specified class
"""


def inherits_from(obj, a_class):
    """
    checks if an object is an instance of a class
    that inherited fr-om the specified class

    Args:
        obj (object): the object to check
        a_class (class): the class to consider
    Returns:
        True: if the object is an instance
        False: otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
