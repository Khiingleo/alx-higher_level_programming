#!/usr/bin/python3
"""Adds a new attribute to an object if possible"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribut to the object if possible

    Args:
        obj (object): the object to add the attribute to
        attribute (str): the name of the attribute
        value: the value to assign to the attribute (can be anything)
    Raises:
        TypeError: if the object cannot have a new attribute
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attribute, value)
