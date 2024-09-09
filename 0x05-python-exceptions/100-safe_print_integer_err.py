#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    """
    prints an integer.

    Args:
        value (any type ):value to be printed
    """
    try:
        print("{:d}".format(value))
        return True  

    except (TypeError, ValueError) as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return False
