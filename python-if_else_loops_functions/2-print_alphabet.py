#!/usr/bin/python3

# Create the alphabet string using a loop
alphabet = ""
for code in range(97, 123):
    alphabet += chr(code)

# Use only one print function with string format
print("{}".format(alphabet), end="")
