#!/usr/bin/python3
"""
Module defines a Rectangle class that inherits from BaseGeometry.

The Rectangle class initializes with private width and height attributes,
both validated as positive integers using BaseGeometry's integer_validator method.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represents a rectangle with private width and height."""

    def __init__(self, width, height):
        """Initialize Rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
