#!/usr/bin/python3

def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer"""

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_num = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
            }
    result = 0

    for i in range(len(roman_string)):
        value = roman_num[roman_string[i]]
        result += value if i == len(roman_string) - 1 or \
            value >= roman_num[roman_string[i + 1]] else -value

    return result
