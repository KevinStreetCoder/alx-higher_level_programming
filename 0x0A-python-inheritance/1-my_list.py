#!/usr/bin/python3
"""
    1-my_list()
"""
class MyList(list):
    """A class that inherits from list and provides a print_sorted method."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        sorted_list = sorted(self)
        print(sorted_list)
