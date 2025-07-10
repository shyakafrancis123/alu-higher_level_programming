#!/usr/bin/python3
"""
This module defines a class Square with a private size attribute.
"""


class Square:
    """
    Represents a square with a private size attribute.

    The size is private to allow control over its value in future tasks.
    """

    def __init__(self, size):
        self.__size = size
