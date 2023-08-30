#!/usr/bin/python3
"""Square Class

This script defines a class for representing a 2D square

"""


class Square:
    """A 2d square

    This class contains methods that allow manipulation.

    """

    def __init__(self, size = 0):
        """Initialize a square with a given size

        The size of the new square is private.

        Args:
            size (int): the length of the sides of the square.
        Raises:
            TypeError: size is not an integer
            ValueError: size is negative

        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
