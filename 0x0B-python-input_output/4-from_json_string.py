#!/usr/bin/python3
"""Defines a fro-m_json_string function"""
import json


def from_json_string(my_str):
    """
    returns a Python object represented by a JSON string
    """
    return json.loads(my_str)
