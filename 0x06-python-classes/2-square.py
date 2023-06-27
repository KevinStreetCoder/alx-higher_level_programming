#!/usr/bin/python3

class Square:
    """
    A class that defines a square.
    Attributes:
        size (int): The side length of the square.
    """
    def __init__(self, size=0):
        """
        Initialize a Square object.
        Args:
            size (int): The side length of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be &#62;= 0")
        self._size = size
