#!/usr/bin/python3
"""Defines a class_to_json function"""


def class_to_json(obj):
    """
    Converts an object to a dictionary description for
    JSON serializion

    Args:
        obj (object): instance of class
    """
    return obj.__dict__
