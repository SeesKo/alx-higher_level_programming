#!/usr/bin/python3
"""Defines a class representing a generic geometry."""


class BaseGeometry:
    """
    A base class representing a generic geometry.
    """
    def area(self):
        """
        Raises an Exception with the message
        'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
