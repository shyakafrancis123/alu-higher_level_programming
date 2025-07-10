#!/usr/bin/python3
"""
Defines a Square class with size, position, area, and printable output.
"""

class Square:
    """Square class with private size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size  # validated by setter
        self.position = position  # validated by setter

    @property
    def size(self):
        """Retrieve size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character # considering position."""
        if self.__size == 0:
            print()
            return

        # Print vertical spaces according to position[1]
        for _ in range(self.__position[1]):
            print()

        # Print each square line with horizontal spaces position[0]
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Define string representation like my_print but returns a string."""
        if self.__size == 0:
            return ""

        # Add vertical spaces
        lines = [""] * self.__position[1]

        # Add each line of the square with horizontal spaces
        for _ in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)

        # Join all lines with newline characters
        return "\n".join(lines)

