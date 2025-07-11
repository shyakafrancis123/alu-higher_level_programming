#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.

The Rectangle class has private width and height attributes, validated
as positive integers using BaseGeometry's integer_validator method.

It implements an area method and a string representation in the format:
[Rectangle] <width>/<height>.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle with validated width and height."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height.

        Args:
            width (int): The rectangle's width, must be positive integer.
            height (int): The rectangle's height, must be positive integer.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the rectangle's area."""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

