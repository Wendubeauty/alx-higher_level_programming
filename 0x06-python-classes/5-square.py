#!/usr/bin/python3
"""
Square Class

This script defines a class for representing a 2D square.
"""


class Square:
    """
    A 2D square class that contains methods for manipulation.
    """

    @property
    def size(self):
        """
        int: Length of square sides.

        The setter validates that the size is an integer and is 0 or greater.
        """

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

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

    def my_print(self):
        """Prints a grid of '#' symbols representing the square.

        Prints a blank line if the size is 0.

        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
