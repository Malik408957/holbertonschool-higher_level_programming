#!/usr/bin/python3

def element_at(my_list, idx):
    # Check if index is negative or out of range (greater than or equal to list length)
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
