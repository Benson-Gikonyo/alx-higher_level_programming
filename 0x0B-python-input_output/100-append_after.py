#!/usr/bin/python3
""" define  append_after() function"""

import sys


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,
    after each line containing a specific string

    Args:
        filename (str): filename
        search_string (str): prerequisite string
        new_string (str): string to add if string is present
    """

    text = ""
    with open(filename, 'r') as f:
        f_line = f.readline()
        while f_line != "":
            text += f_line
            if search_string in f_line:
                text += new_string
            f_line = f.readline()
    with open(filename, 'w') as f:
        f.write(text)
