#!/usr/bin/python3
def multiple_returns(sentence):
    """
    returns a tuple with the length of a string and its first character.
    Args:
        sentence (string): string to be measured

    Return: tuple with length of string and 1st character of sentence
    """

    if not sentence or len(sentence) == 0:
        return (0, None)

    return (len(sentence), sentence[0])
