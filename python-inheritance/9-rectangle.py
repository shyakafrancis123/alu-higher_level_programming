#!/usr/bin/python3
"""
Module defines a Rectangle class inheriting from BaseGeometry.

The Rectangle class has private width and height attributes validated
as positive integers. It implements an area method and a string
representation in the format: [Rectangle] <width>/<height>.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class with width and height validated."""

    def __init__(self, width, height):
        """Initialize Rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return string representation of the Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

