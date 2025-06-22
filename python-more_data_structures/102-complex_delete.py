#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # Create a copy of the dictionary without keys whose value equals the given value
    return {k: v for k, v in a_dictionary.items() if v != value}
