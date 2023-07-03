#!/usr/bin/python3
"""
    2-rectangle: class Rectangle
"""


class Rectangle:
    """
    Class Rectangle defines a rectangle.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the instances of Rectangle.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        Raises:
            ValueError: If width or height is negative.
            TypeError: If width or height is not an integer.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter function for the private attribute width.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter function for the private attribute width.

        Args:
            value (int): The new width value.
        Raises:
            ValueError: If the value is negative.
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter function for the private attribute height.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter function for the private attribute height.

        Args:
            value (int): The new height value.
        Raises:
            ValueError: If the value is negative.
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height)
