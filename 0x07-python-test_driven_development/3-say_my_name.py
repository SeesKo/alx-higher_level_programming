#!/usr/bin/python3
"""
Defines a function that prints a person's name.

first_name and last_name must be strings.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>.
    """

    # Validate first_name input
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Validate last_name input
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the formatted name
    print("My name is {} {}".format(first_name, last_name))
