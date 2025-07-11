#!/usr/bin/python3
"""Defines a base geometry class."""


class BaseGeometry:
    """Base geometry class with area method."""

    def area(self):
        """Raises an Exception because area is not implemented."""
        raise Exception("area() is not implemented")
