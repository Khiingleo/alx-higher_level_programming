#!/usr/bin/python3
"""Function that writes a string to a text file and returns
the number of characters written"""


def write_file(filename="", text=""):
    """
    writes a string to the text file and returns num
    of characteres written

    Args:
        filename (str): the name of the file to open
        text (str): the text to write into the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
