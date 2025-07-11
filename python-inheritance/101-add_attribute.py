#!/usr/bin/python3
"""
Module provides a function to add a new attribute to an object
only if the object allows dynamic attribute creation.
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj (object): The object to add attribute to.
        name (str): The attribute name.
        value (any): The attribute value.

    Raises:
        TypeError: If the object does not allow new attributes.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")

