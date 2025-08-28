#!/usr/bin/python3

# Import the add function from add_0.py
from add_0 import add

# Check if this file is being run directly (not imported)
if __name__ == "__main__":
    # Assign values to variables
    a = 1
    b = 2
    
    # Format and print the result
    print("{} + {} = {}".format(a, b, add(a, b)))
