#!/usr/bin/python3
""" defines add attribute function"""

def add_attribute(obj, attribute, value):
    """ check if an object has attributes, and if so,
    add accordingly
    """
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
