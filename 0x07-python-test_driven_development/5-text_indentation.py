#!/usr/bin/python3
""" Contains the text_indentation(text) function
prints a text with 2 new lines
"""


def text_indentation(text):
    """prints a text with 2 new lines after each
    of these characters: ., ? and :
    Args:
        text (str): text to be printed

    Return: Nothing
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if text is None:
        raise TypeError("text_indentation() missing 1 \
            required positional argument: 'text'")

    strip_text = text.strip()
    chars = ['.', ':', '?']

    for idx in range(0, len(strip_text)):
        if strip_text[idx - 1] in chars:
            print("\n")
        else:
            print(strip_text[idx], end='')

    print("\n")
