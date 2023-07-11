#!/usr/bin/python3
"""
    3-to_json_string: to_json_string()
"""


import json


def to_json_string(my_obj):
    """
        to_json_string returns the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
