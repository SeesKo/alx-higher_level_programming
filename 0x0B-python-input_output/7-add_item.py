#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a file."""

import sys
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation."""
    with open(filename, 'w', encoding='utf-8') as myFile:
        json.dump(my_obj, myFile)

def load_from_json_file(filename):
    """Creates an object from a JSON file."""
    try:
        with open(filename, 'r', encoding='utf-8') as myFile:
            return json.load(myFile)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Load existing data or create an empty list
data = load_from_json_file("add_item.json")

# Add command line arguments to the list
for arg in sys.argv[1:]:
    data.append(arg)

# Save the updated list to the file
save_to_json_file(data, "add_item.json")
