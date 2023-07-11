#!/usr/bin/python3
"""
    4-from_json_string: from_json_string()
"""


import json


def from_json_string(my_str):
    """
        from_json_string returns an object (Python data structure)
        represented by a JSON string
    """
    return json.loads(my_str)
