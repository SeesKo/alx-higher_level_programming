#!/usr/bin/python3
"""Defines an object-checking function"""


def is_same_class(obj, a_class):
    """Checks if obj is exactly an instance of the specified class."""
    return type(obj) is a_class
