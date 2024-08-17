#!/usr/bin/python3
""" defines append_file function which writes to a file."""


def append_write(filename="", text=""):
    """appends a string to a text file (UTF8)
    and returns the number of characters written:

    Args:
        filename (str): file to write to.
        text (str): text to be written.

    Return: number of characters
    """
    with open(filename, "a", encoding="utf-8") as f:
        write = f.write(text)
        return write
        f.close()
