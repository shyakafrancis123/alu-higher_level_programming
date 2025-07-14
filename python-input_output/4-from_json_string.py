#!/usr/bin/python3
"""
Module to convert a JSON string to a Python object.
"""


import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        any: Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
