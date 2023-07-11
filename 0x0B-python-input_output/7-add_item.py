#!/usr/bin/python3
"""
    7-add_item: Add items to a Python list and save to a file
"""


import sys
from os.path import exists
from json import loads
from json import dump
from json import JSONDecodeError
from sys import argv


def save_to_json_file(my_obj, filename):
    """
        save_to_json_file writes an Object to a text file,
        using a JSON representation
    """
    with open(filename, "w", encoding='utf-8') as a_file:
        dump(my_obj, a_file)


def load_from_json_file(filename):
    """
        load_from_json_file creates an Object from a "JSON file"
    """
    with open(filename, "r", encoding='utf-8') as a_file:
        return loads(a_file.read())


filename = "add_item.json"

if exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

my_list.extend(argv[1:])
save_to_json_file(my_list, filename)
