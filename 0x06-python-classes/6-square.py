#!/usr/bin/python3

class Square:
    """
    A class to represent a square.
    """
    def __init__(self, size=0):
        """
        Initialize a Square object.
        Args:
            size (int): The side length of the square.
        """
        self.size = size
    @property
    def size(self):
        """
        Get the current square size.
        Returns:
            int: The current square size.
        """
        return self._size
    @size.setter
    def size(self, value):
        """
        Set the current square size.
        Args:
            value (int): The new square size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be &#62;= 0")
        self._size = value
    def area(self):
        """
        Returns the current square area.
        Returns:
            int: The current square area.
        """
        return self._size * self._size
    def my_print(self):
        """
        Prints in stdout the square with the character #:
        If size is equal to 0, print an empty line.
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
