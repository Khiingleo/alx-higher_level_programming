#!/usr/bin/python3
"""Defines a load_fr-om_json_file function"""
import json


def load_from_json_file(filename):
    """
    creates an object from a JSON file

    Args:
        filename (str): the name of the file
    """
    with open(filename, 'r') as f:
        return json.load(f)
