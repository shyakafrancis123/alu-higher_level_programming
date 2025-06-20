#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Return a copy of the original list if idx is invalid
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    # Create a copy of the list
    new_list = my_list[:]
    # Replace the element at idx
    new_list[idx] = element
    return new_list
