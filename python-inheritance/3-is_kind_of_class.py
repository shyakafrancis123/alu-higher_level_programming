#!/usr/bin/python3
"""Module that defines a function to check class inheritance."""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance or inherited instance of a_class."""
    return isinstance(obj, a_class)
