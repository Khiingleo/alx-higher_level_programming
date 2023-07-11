#!/usr/bin/python3
"""Defines a append_write function"""


def append_write(filename="", text=""):
    """
    appends a string at the end of the text file

    Args:
        filename (str): the name of the file (default is empty string)
        text (str): the string to append
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
