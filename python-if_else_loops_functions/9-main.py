#!/usr/bin/env python3
print_last_digit = __import__('9-print_last_digit').print_last_digit

# Test cases
print("Test 1 (98): ", end="")
result1 = print_last_digit(98)
print(f" → Returned: {result1}")

print("Test 2 (0): ", end="")
result2 = print_last_digit(0) 
print(f" → Returned: {result2}")

print("Test 3 (-1024): ", end="")
result3 = print_last_digit(-1024)
print(f" → Returned: {result3}")

print("Test 4 (12345): ", end="")
result4 = print_last_digit(12345)
print(f" → Returned: {result4}")

print("Test 5 (-7): ", end="")
result5 = print_last_digit(-7)
print(f" → Returned: {result5}")
