#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Create an empty list to store results
    result = []
    # Iterate through each number in the list
    for num in my_list:
        # Check if number is divisible by 2
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
