#!/usr/bin/python3

def no_c(my_string):
    """Removes all characters c & C from a string."""

    # Initializing an empty string to store the result
    result = ""

    # Iterating through each char in the input string
    for char in my_string:
        if char != 'c' and char != 'C':
            result += char

    return result
