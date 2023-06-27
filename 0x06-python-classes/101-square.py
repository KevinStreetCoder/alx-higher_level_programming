#!/usr/bin/python3

class Square:
    """A class to represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square object.

        Args:
            size (int): The side length of the square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current square size.

        Returns:
            int: The current square size.
        """
        return self._size

    @size.setter
    def size(self, value):
        """Set the current square size.

        Args:
            value (int): The new square size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """Get the current square position.

        Returns:
            tuple: The current square position.
        """
        return self._position

    @position.setter
    def position(self, value):
        """Set the current square position.

        Args:
            value (tuple): The new square position.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """Returns the current square area.

        Returns:
            int: The current square area.
        """
        return self._size * self._size

    def my_print(self):
        """Prints the square with the character '#'.

        If size is equal to 0, print an empty line.
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(' ' * self.position[0] + '#' * self.size)
