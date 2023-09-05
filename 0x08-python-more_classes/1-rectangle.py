#!/usr/bin/python3
"""This is a definition of a rectangle"""


class Rectangle:
    """a rectangle class"""

    def __init__(self, width=0, height=0):
        """this is nit for Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """a rectangular width collectorr"""
        return self.__width

    @width.setter
    def width(self, value):
        """Rectangle width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Rectangle height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Rectangle height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
