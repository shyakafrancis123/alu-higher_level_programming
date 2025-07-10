#!/usr/bin/python3
"""
This module defines a Square class with size validation,
getter/setter, area calculation, and a print method.
"""


class Square:
    """
    Represents a square with a private size attribute.

    Size must be an integer >= 0.
    """

    def __init__(self, size=0):
        self.size = size  # Use setter for validation

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#' to stdout."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)

