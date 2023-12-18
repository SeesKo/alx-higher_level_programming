def safe_print_list(my_list=[], x=0):
    elem_count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            elem_count += 1
    except IndexError:
        pass  # Handle the case when the index is out of range

    print()  # Print a new line after the elements
    return elem_count
