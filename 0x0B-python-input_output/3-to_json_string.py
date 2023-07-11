#!/usr/bin/python3
"""Defines a function that returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """
    converts object to it's JSON representation

    Args:
        my_obj (object): the object to convert
    Returns:
        JSON representation of the object
    """
    return json.dumps(my_obj)
