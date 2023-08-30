#!/usr/bin/python3
"""
Square Class

This script defines a class for representing a 2D square.
"""


class Square:
    """
    A 2D square class that contains methods for manipulation.
    """

    def __init__(self, size=0):
        """
        Initialize a square with a given size.

        The size of the new square is private.

        Args:
            size (int): The length of the sides of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square
        """
        return self.__size ** 2
