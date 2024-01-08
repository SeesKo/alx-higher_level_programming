#!/usr/bin/python3
"""Defines an object-attribute-and-method-lsiting function."""


def lookup(obj):
    """
    Returns a list of valid attributes for the given object.
    """
    return dir(obj)
