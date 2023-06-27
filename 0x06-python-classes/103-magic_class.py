#!/usr/bin/python3

import math

class MagicClass:
    """
    A class that performs mathematical operations on a radius.
    """

    def __init__(self, radius=0):
        """
        Initialize a MagicClass object.
        Args:
            radius (int or float): The radius value.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculate the area of a circle with the given radius.
        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate the circumference of a circle with the given radius.
        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
