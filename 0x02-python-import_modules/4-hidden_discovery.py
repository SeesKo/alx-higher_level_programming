#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # Get all names defined in the module
    module_names = dir(hidden_4)

    # Filter names based on criteria (not starting with '__')
    filt_names = [name for name in module_names if not name.startswith('__')]

    # Print names in alphabetical order
    for name in sorted(filt_names):
        print(name)
