#!/usr/bin/python3
"Reads a text file and prints its content to stdout."


def read_file(filename=""):
    """
    Reads a text file and prints its content to the standard output.
    """
    try:
        with open(filename, encoding='utf-8') as file:
            print(file.read(), end='')
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
