#!/usr/bin/python3
"""Defines an object attribute lookup function"""


def lookup(obj):
    """
    returns a list of attributes and methods of given object

    Args:
        obj (object): the object to inspect
    Returns:
        list: a list of strings containing information about
        the `object`
    """
    return dir(obj)
