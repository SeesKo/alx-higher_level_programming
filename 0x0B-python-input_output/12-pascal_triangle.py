#!/usr/bin/python3
"""Defines a pascal triangle-creating function."""


def pascal_triangle(n):
    """Generates Pascal's Triangle up to the nth row."""
    if n <= 0:
        return []

    pascal = []

    for i in range(n):
        row = [1] * (i + 1)

        if i > 1:
            for j in range(1, i):
                row[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

        pascal.append(row)

    return pascal
