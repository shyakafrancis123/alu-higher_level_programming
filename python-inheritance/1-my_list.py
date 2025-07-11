#!/usr/bin/python3
"""This module defines a class MyList that inherits from list."""

class MyList(list):
    """Custom list that can print itself in sorted order."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        sorted_list = sorted(self)
        print(sorted_list)
        return sorted_list
