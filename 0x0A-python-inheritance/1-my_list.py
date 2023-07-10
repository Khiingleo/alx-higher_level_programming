#!/usr/bin/python3
"""Defines a class MyList that inherits  list"""


class MyList(list):
    """
    A class that inherits list
    """
    def print_sorted(self):
        """prints list in sorted order(ascending)"""
        print(sorted(self))
