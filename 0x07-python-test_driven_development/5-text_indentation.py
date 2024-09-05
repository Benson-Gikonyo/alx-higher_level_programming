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

    if type(text) is not str:
        raise TypeError("text must be a string")

    if text is None:
        raise TypeError("text_indentation() missing 1 \
            required positional argument: 'text'")

    text = text.strip()
    char = 0
    while char < len(text) and text[char] == ' ':
        char += 1
    
    while char < len(text):
        print(text[char], end="")
        if text[char] == "\n" or text[char] in ".?:":
            if text[char] in ".?:":
                print("\n")
            char += 1
            while char < len(text) and text[char] == ' ':
                char += 1
            continue
        char += 1
