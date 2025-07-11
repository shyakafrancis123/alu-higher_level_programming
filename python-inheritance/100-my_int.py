#!/usr/bin/python3
"""
Module defines MyInt class that inherits from int,
but inverts the behavior of == and != operators.
"""


class MyInt(int):
    """
    MyInt is a rebel integer class where equality and inequality
    operators are inverted.
    """

    def __eq__(self, other):
        """Invert equality: return True if not equal."""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Invert inequality: return True if equal."""
        return int.__eq__(self, other)

