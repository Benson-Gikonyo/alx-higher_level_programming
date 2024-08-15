#!/usr/bin/python3
"""defines read_file function, which reads a file"""


def read_file(filename=""):
    """read a file
    Args:
        filename (str): file to be read. Defaults to "".
    """
    with open(filename, encoding="utf-8") as f:
        read_file = f.read()

    print(read_file)
