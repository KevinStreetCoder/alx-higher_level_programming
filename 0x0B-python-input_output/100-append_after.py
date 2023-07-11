#!/usr/bin/python3
"""
    100-append_after: Append After
"""


def append_after(filename="", search_string="", new_string=""):
    """
        Insert a line of text after each line containing a specific string
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
