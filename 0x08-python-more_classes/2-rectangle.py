#!/usr/bin/python3
"""This is a definition of a rectangle"""


class Rectangle:
    """a rectangle class"""

    def __7init__(self, width=0, height=0):
        """this init is for the Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """a rectangle width collector"""
        return self.__width

    @width.setter
    def width(self, value):
        """a rectangle width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """a rectangle height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """a rectangle height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """

        this returns the perimeter of the rectangle,
        or nothing if height/width are 0
        """
        if self.__height == 0 or self.__width == 0:
            return
        return (self.__height * 2) + (self.__width * 2)
