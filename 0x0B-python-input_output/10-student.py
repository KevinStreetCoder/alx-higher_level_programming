#!/usr/bin/python3
"""
    10-student: Student class
"""


class Student:
    """
        Student class
    """

    def __init__(self, first_name, last_name, age):
        """
            Initialize a new Student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            Retrieve a dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
