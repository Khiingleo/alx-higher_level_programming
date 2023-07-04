#!/usr/bin/python3
"""Defines a locked class LockedClass"""


class LockedClass:
    """
    A representation of a locked class that only
    allows access to the attribute 'first_name'
    """
    __slots__ = ["first_name"]
