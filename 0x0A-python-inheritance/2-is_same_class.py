#!/usr/bin/python3
"""Defines a function that returns true if the 
object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    checks if an object is exactly an instance
    of the specified class
      
    Args:
        obj (object): the object to check
        a_class (class): the specified class
    Returns:
        True: if the object is an exect instance of the class
        False: otherwise
    """
    if type(obj) == a_class:
        return True
    return False
