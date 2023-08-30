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

    @property
    def position(self):
        """
        tuple of int: The square's position on a plane.

        Setter validates that the position is a tuple of 2 positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (
            isinstance(value, tuple)
            and len(value) == 2
            and isinstance(value[1], int)
            and isinstance(value[0], int)
            and value[0] >= 0
            and value[1] >= 0
        ):
            self.__position = value

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square with a given size.

        The size of the new square is private.

        Args:
            size (int): The length of the sides of the square.
            position (tuple): The position of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not(isinstance(position, tuple) and
                len(position) == 2 and isinstance(position[0], int) and
                isinstance(position[1], int) and position[0] >= 0 and
                position[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints a grid of '#' symbols representing the square.

        Prints a blank line if the size is 0 and moves square to match postion
        """
        if self.__size == 0:
            print()
            return
        for i in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))
