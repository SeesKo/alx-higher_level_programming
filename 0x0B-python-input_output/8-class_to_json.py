#!/usr/bin/python3
"""Defines a function that returns a dictionary description."""


def class_to_json(obj):
    """
    Returns the dictionary description with a simple
    data structure for JSON serialization.
    """
    return obj.__dict__
