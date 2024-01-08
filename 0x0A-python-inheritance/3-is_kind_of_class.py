#!/usr/bin/python3
"""Defines an object-checking function."""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of, or if obj is an instance
    of a class inherited from, the specified class.
    """
    return isinstance(obj, a_class)
