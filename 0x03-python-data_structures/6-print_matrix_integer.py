#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers"""

    for row in matrix:
        for i, elem in enumerate(row):
            print("{:d}".format(elem), end="")
            if i < len(row) - 1:
                print(" ", end="")
        print()
