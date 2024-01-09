#!/usr/bin/python3
"""
Function to write string to a text file and
return number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and
    returns the number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
