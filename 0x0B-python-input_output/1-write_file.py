#!/usr/bin/python3
""" defines write_file function which writes to a file."""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    and returns the number of characters written:

    Args:
        filename (str): file to write to.
        text (str): text to be written.

    Return: number of characters
    """
    with open(filename, "w", encoding="utf-8") as f:
        write = f.write(text)
        return write
        f.close()