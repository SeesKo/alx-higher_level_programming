#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elem_count = 0
    try:
        for i in range(x):
            value = my_list[i]
            if type(value) is int:
                print("{:d}".format(value), end="")
                elem_count += 1
    except (ValueError, TypeError):
        pass

    print()
    return elem_count
