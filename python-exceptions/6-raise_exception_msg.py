#!/usr/bin/python3
def raise_exception_msg(message=""):
    """
    Raises a NameError exception with a custom message.
    Args:
        message (str): The error message to be displayed
    This function raises a NameError with the provided message
    to demonstrate custom exception messages.
    """
    raise NameError(message)
