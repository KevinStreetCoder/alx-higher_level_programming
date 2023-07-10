#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    A class Square that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a Square instance with a size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not a positive integer.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Return a string representation of the Square instance.

        Returns:
            str: The string representation of the Square instance.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
