#!/usr/bin/python3
for first_digit in range(0, 10):
    for second_digit in range(first_digit + 1, 10):
        if first_digit == 0 and second_digit == 1:
            print("{}{}".format(first_digit, second_digit), end="")
        else:
            print(", {}{}".format(first_digit, second_digit), end="")
print()
