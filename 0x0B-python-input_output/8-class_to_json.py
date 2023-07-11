#!/usr/bin/python3
"""Defines a class_to_json function"""
import json


def class_to_json(obj):
    """
    Converts an object to a dictionary description for
    JSON serialization

    Args:
        obj: An instance of a class
    Returns:
        A dictionary representation of the object
    """
    return obj.__dict__
