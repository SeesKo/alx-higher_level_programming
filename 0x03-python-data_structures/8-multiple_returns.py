#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns tuple with the length of
    a string and its first character"""

    # Checking if the sentence is empty
    if len(sentence) == 0:
        return (0, None)

    # Returning a tuple with the length and the first char
    return (len(sentence), sentence[0])
