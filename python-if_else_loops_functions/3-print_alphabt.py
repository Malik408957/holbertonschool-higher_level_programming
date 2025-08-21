#!/usr/bin/python3

result = ""
for ascii_code in range(97, 123):
    if ascii_code != 101 and ascii_code != 113:
        result += chr(ascii_code)

print("{}".format(result), end="")
