#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list and only integers.
    Args:
        my_list: The list to process (can contain any type)
        x: Number of elements to access in the list
    Returns:
        The real number of integers printed
    """
    count = 0
    try:
        for i in range(x):
            try:
                # Try to print as integer
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except (ValueError, TypeError):
                # Skip non-integer values silently
                continue
    except IndexError:
        # Re-raise IndexError for out-of-range access
        raise
    finally:
        # Print new line after all elements
        print()
    return count
