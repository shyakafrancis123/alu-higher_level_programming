#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:  # Handles None or empty list
        return
    for i in my_list[::-1]:
        print("{:d}".format(i))
