#!/usr/bin/python3
"""Defines a save_to_json_file Function"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an object to a text file using JSON representation

    Args:
        my_obj (object): the object to write
        filename (str): the name of the file
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
