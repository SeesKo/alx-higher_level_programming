#!/usr/bin/python3
"""
This module defines a function that adds 2 integers.

If a or b are floats, casts them to integers before addition.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
