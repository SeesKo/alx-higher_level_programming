#!/usr/bin/python3

def remove_char_at(str, n):
    # Creates copy of the string with char at position n removed.
    if n < 0 or n >= len(str):
        return str  # Return original string if n is out of bounds

    # Using slicing to create new string without char at position n
    return str[:n] + str[n+1:]
