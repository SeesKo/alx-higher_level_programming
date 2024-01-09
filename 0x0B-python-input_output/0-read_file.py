#!/usr/bin/python3
"Reads a text file and prints its content to stdout."


def read_file(filename=""):
    """
    Reads a text file and prints its content to the standard output.
    """
    with open(filename, encoding="utf-8") as myFile:
        for line in myFile:
            print(line, end="")
