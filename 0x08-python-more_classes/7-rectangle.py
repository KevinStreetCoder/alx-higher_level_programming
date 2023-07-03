#!/usr/bin/python3
"""
    7-rectangle: class Rectangle
"""

class Rectangle:
    """
    Class Rectangle defines a rectangle.

    Attributes:
        number_of_instances (int): Keeps track of the number of instances of Rectangle class.
        print_symbol (str): The symbol used to represent the rectangle when printed.
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        """
        Returns a string representation of the rectangle for debugging.

        Returns:
            str: The string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Destructor for the Rectangle class.
        Decreases the number of instances and prints a farewell message.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
