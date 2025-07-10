#!/usr/bin/python3
"""
This module defines a Square class with private size and position attributes,
with validation, and methods to compute area and print the square with position offset.
"""


class Square:
    """
    Represents a square with size and position.

    Attributes:
        size (int): The size of the square (length of sides).
        position (tuple): A tuple of two positive integers representing
                          the horizontal and vertical offset for printing.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size        # Will use setter for validation
        self.position = position  # Will use setter for validation

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

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with validation."""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the '#' character respecting the position."""
        if self.__size == 0:
            print()
            return

        # Print vertical offset (position[1])
        for _ in range(self.__position[1]):
            print()

        # Print each row
        for _ in range(self.__size):
            # Print horizontal offset (position[0]) as spaces
            print(" " * self.__position[0] + "#" * self.__size)

