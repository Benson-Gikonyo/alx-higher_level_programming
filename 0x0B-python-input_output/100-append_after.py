#!/usr/bin/python3
""" define  append_after() function"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,
    after each line containing a specific string

    Args:
        filename (str): filename
        search_string (str): prerequisite string
        new_string (str): string to add if string is present
    """

    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as f:
        f.write(text)
