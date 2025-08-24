#!/usr/bin/python3

def print_last_digit(number):
    """
    Prints and returns the last digit of a number.
    
    Args:
        number: The input number (can be positive, negative or zero)
    
    Returns:
        The last digit of the number (always positive)
    """
    # Get the absolute value to handle negative numbers
    # Use modulo 10 to get the last digit
    last_digit = abs(number) % 10
    
    # Print the last digit without newline
    print(last_digit, end="")
    
    # Return the last digit value
    return last_digit

# Test the function (this part is for testing only)
if __name__ == "__main__":
    print_last_digit(98)
    print_last_digit(0)
    r = print_last_digit(-1024)
    print(r)
