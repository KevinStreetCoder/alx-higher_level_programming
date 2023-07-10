#!/usr/bin/python3
"""
    10-rectangle: class Rectangle from BaseGeomerty
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A class called Square that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a Square instance with a size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return a string representation of the Square instance."""
        return "[Square] {}/{}".format(self.__size, self.__size)
