#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elem_count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            elem_count += 1

    # Handling case when index is out of range
    except IndexError:
        pass

    # Printing new line after the elements
    print()
    return elem_count
