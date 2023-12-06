#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list"""
    # Creating new list to store the replaced elements
    new_list = []

    # Iterating through elements of the input list
    for element in my_list:
        # Replacing element if it matches the search element
        new_element = replace if element == search else element
        new_list.append(new_element)

    return new_list
