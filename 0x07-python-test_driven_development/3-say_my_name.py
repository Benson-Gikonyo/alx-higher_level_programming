#!/usr/bin/python3
""" contains the say_my_name function
"""

def say_my_name (first_name, last_name=""):
    """print 'My name is <first name> <last name>'

    Args:
        first_name (string): first name of person
        last_name (str, optional): second name of person. Defaults to "".
    
    Return: Nothing.
    """
    if first_name is None:
        raise TypeError("say_my_name() missing 1 required positional argument: 'first_name'")
    
    elif not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    elif len(last_name) == 0:
        print(f"My name is {first_name}")

    else:
        print(f"My name is {first_name} {last_name}")
