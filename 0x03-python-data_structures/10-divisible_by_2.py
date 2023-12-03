#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list"""

    # Initializin empty list to store True or False values
    new_list = []

    # Iterating thru elements in the original list
    for i in my_list:
        # Checking if element is a multiple of 2
        new_list.append(i % 2 == 0)

    return new_list
