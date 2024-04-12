#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    """
    prints an integer.

    Args:
        value (any type ):value to be printed
    """
    try:
        if value.is_interger() ==  True:
            print("{:d}".format())
            return True
        else:
            raise Exception
            
 
    except Exception:
        return False
        sys.stderr.write("Unknown format code 'd' for object of type 'str'\n")
