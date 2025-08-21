#!/usr/bin/python3
import random

# generate a random number between -10000 and 10000
number = random.randint(-10000, 10000)

# get the last digit by dividing by 10 and taking the remainder
# proper handling of negative numbers is mandatory
last_digit = abs(number) % 10

# if the original number is negative, make the last digit negative too
if number < 0:
    last_digit = -last_digit

# format and print the result
result = f"Last digit of {number} is {last_digit} and is"

# check the conditions - FIXED: should be greater than 5, not greater than or equal to 6
if last_digit > 5:
    print(f"{result} greater than 5")
elif last_digit == 0:
    print(f"{result} 0")
else:
    print(f"{result} less than 6 and not 0")
