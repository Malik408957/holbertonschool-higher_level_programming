#!/usr/bin/python3

def no_c(my_string):
    # Create an empty string to build the result
    result = ""
    # Iterate through each character in the string
    for char in my_string:
        # Check if character is not 'c' and not 'C'
        if char != 'c' and char != 'C':
            result += char
    return result
