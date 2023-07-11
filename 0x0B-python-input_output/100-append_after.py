#!/usr/bin/python3
"""Defines a append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """
    appends a new line of text to a file after each line
    containing a specific string

    Args:
        filename (str): the name of the file (default is "")
        search_string (str): the string to look for (default is "")
        new_string (str): the new line of text to add (default is "")
    """
    lines = ""
    with open(filename, "r+", encoding="utf-8") as f:
        for line in f:
            lines += line
            if search_string in line:
                lines += new_string
        f.seek(0)
        f.write(lines)
