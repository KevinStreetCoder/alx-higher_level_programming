#!/usr/bin/python3
"""
    6-load_from_json_file: load_from_json_file()
"""


import json


def load_from_json_file(filename):
    """
        load_from_json_file creates an Object from a "JSON file"
    """
    with open(filename, "r", encoding='utf-8') as a_file:
        return json.load(a_file)
