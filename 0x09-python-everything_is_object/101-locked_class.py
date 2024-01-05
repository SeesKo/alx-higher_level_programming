#!/usr/bin/python3
"""Prevents the user from dynamically creating new instance attributes."""


class LockedClass:
    """
    A class with restricted instance attribute creation,
    allowing only 'first_name'.
    """
    __slots__ = ('first_name',)

    def __init__(self, first_name=None):
        """
        Initializes the LockedClass instance with the specified first_name.
        """
        self.first_name = first_name
