#!/usr/bin/python3

def print_last_digit(number):
    """Print the last digit of a number and return it."""
    # Get the absolute value to handle negative numbers
    # Use modulo 10 to get the last digit
    last_digit = abs(number) % 10
    
    # Print the last digit without newline
    print(last_digit, end="")
    
    # Return the last digit value
    return last_digit


if __name__ == "__main__":
    print_last_digit(98)
    print_last_digit(0)
    r = print_last_digit(-1024)
    print(r)
