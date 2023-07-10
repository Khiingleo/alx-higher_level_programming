#!/usr/bin/python3
"""Defines a function that checks if an object is an
instance of or if the object is an instance of a class
that inherited fr-om the specified class"""


def is_kind_of_class(obj, a_class):
    """
    checks if an object is an instance or if the object
    is an instance of a class that inherited a
    fr-om specified class

    Args:
        obj (object): the object to check
        a_class (class): the specified class
    Returns:
        True: if object is an instacne
        False: otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
