#!/usr/bin/python3

def uppercase(str):
    # Printing the string str in uppercase followed by a new line
    result = ""
    for char in str:
        # Checking if the character is a lowercase letter
        if 97 <= ord(char) <= 122:
            # Convert to uppercase by subtracting 32 from the ASCII value
            # Difference between uppercase & lowercase ASCII is 32
            result += "{}".format(chr(ord(char) - 32))
        else:
            result += char
    # Printing the result string with a newline character
    print(result)
