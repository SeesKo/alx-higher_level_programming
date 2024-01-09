#!/usr/bin/python3
"""Defines a class `Student` with attributes."""


class Student:
    """Defines a student with first_name, last_name, and age."""
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a `Student` instance."""
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the `Student` instance
        based on the provided dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
