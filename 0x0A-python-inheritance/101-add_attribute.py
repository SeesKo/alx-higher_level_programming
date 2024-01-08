#!/usr/bin/python3
"""Module for adding a new attribute to an object if possible."""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute will be added.
        attribute: The name of the new attribute.
        value: The value of the new attribute.

    Raises:
        TypeError: If the object can't have a new attribute.
    """
    if "__dict__" in dir(obj):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
