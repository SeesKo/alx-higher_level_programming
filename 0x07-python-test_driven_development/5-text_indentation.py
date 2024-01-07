#!/usr/bin/python3
"""
Defines function that prints text with 2 new lines after characters.

`text` must be a string.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each of the characters: ., ? and :.
    """

    # Validate text input
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Process the text and print with 2 new lines after specified characters
    i = 0
    while i < len(text):
        char = text[i]

        # Print the current character
        print(char, end="")

        # Check if the current character is one of the specified characters
        if char in ".?:":
            # Move to the next line and print two new lines
            print("\n\n", end="")
            # Skip the following spaces, if any
            i += 1
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1

        i += 1
