#!/usr/bin/python3
"""
Defines a Square class with size as a number and supports comparison by area.
"""

class Square:
    """Square class with private size attribute and comparison operators."""

    def __init__(self, size=0):
        self.size = size  # will call the setter for validation

    @property
    def size(self):
        """Retrieve size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    # Comparison operators based on area

    def __eq__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() == other.area()

    def __ne__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() != other.area()

    def __lt__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() < other.area()

    def __le__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() <= other.area()

    def __gt__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() > other.area()

    def __ge__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() >= other.area()

