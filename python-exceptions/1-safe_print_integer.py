#!/usr/bin/python3
def safe_print_integer(value):
    """
    Prints an integer with "{:d}".format().
    Args:
        value: The value to print (can be any type)
    Returns:
        True if value was printed correctly (is integer),
        False otherwise
    """
    try:
        # Try to format and print as integer
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        # If value cannot be formatted as integer
        return False
