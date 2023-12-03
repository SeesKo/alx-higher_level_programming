#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples"""

    # Ensuring tuples have at least 2 elements
    a = tuple_a[:2] + (0, 0) if len(tuple_a) < 2 else tuple_a[:2]
    b = tuple_b[:2] + (0, 0) if len(tuple_b) < 2 else tuple_b[:2]

    # Summing up the corresponding elements of the tuples
    sum_tuple = (a[0] + b[0], a[1] + b[1])

    return sum_tuple
