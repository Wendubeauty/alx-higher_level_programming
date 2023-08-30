#!/usr/bin/python3
"""Square Class

This script defines a class for representing a 2D square

"""


class Square:
    """A 2d square

    This class contains methods that allow manipulation.

    """

    def __init__(self, size):
        """Initialize a square with a given size

        The size of the new square is private.

        Args:
            size (int): the length of the sides of the square.

        """

        self.__size = size
