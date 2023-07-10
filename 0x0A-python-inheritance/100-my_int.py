#!/usr/bin/python3
"""
    100-my_int()
"""
class MyInt(int):
    """
    A class MyInt that inherits from int.
    """

    def __eq__(self, other):
        """
        Invert the behavior of the equality (==) operator.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Invert the behavior of the inequality (!=) operator.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return super().__eq__(other)
