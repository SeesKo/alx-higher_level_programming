#!/usr/bin/python3
"""
Defines a function that inserts a line of text to a
file, after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text after each line containing a specific string."""
    lines = []

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)
