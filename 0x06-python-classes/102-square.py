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
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value
    
    def area(self):
        """
        Returns the current square area.
        Returns:
            int: The current square area.
        """
        return self._size * self._size
    
    def __eq__(self, other):
        """
        Compare two Square instances based on the area.
        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False
    
    def __ne__(self, other):
        """
        Compare two Square instances based on the area.
        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return not self.__eq__(other)
    
    def __lt__(self, other):
        """
        Compare two Square instances based on the area.
        Returns:
            bool: True if the area of the first square is less than the second, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False
    
    def __le__(self, other):
        """
        Compare two Square instances based on the area.
        Returns:
            bool: True if the area of the first square is less than or equal to the second, False otherwise.
        """
        return self.__lt__(other) or self.__eq__(other)
    
    def __gt__(self, other):
        """
        Compare two Square instances based on the area.
        Returns:
            bool: True if the area of the first square is greater than the second, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False
    
    def __ge__(self, other):
        """
        Compare two Square instances based on the area.
        Returns:
            bool: True if the area of the first square is greater than or equal to the second, False otherwise.
        """
        return self.__gt__(other) or self.__eq__(other)
