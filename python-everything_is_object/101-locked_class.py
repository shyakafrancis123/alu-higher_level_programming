#!/usr/bin/python3
"""Defines a LockedClass that restricts attribute assignment."""

class LockedClass:
    """A class that only allows setting 'first_name' attribute."""
    __slots__ = ['first_name']
