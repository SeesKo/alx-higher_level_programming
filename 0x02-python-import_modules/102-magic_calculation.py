#!/usr/bin/python3
def magic_calculation(a, b):
    magic_module = __import__('magic_calculation_102',
                              globals(), locals(), ['add', 'sub'], 0)
    add, sub = magic_module.add, magic_module.sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
