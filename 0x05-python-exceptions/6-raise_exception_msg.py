#!/usr/bin/python3
def raise_exception_msg(message=""):
    """
    raises a name exception with a message.

    Args:
        message (str): message to send to the user.
    """

    try:
        raise Exception

    except Exception:
        print(message)
