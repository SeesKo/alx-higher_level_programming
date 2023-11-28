#!/usr/bin/python3

# "{:d}" formats i as a decimal number.
# "= 0x{:x}" formats the hexadecimal representation of i.

for i in range(99):
    print("{:d} = 0x{:x}".format(i, i))
