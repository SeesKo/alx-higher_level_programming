#!/usr/bin/python3
"""Defines a function that returns a dictionary description."""


def class_to_json(obj):
    """
    Returns the dictionary description with a simple
    data structure for JSON serialization.
    """
    attributes = obj.__dict__
    serializable_attributes = {}

    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_attributes[key] = value

    return serializable_attributes
