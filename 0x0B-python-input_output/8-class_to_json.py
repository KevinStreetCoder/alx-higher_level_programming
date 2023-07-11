#!/usr/bin/python3
"""
    8-class_to_json: class_to_json()
"""


def class_to_json(obj):
    """
        class_to_json returns the dictionary description with a simple data structure
        for JSON serialization of an object
    """
    return obj.__dict__
