#!/usr/bin/python3
"""This is a definition of a rectangle"""


class Rectangle:
    """a rectangle class"""
    num_of_instances = 0
    printSymbol = "#"

    def __init__(self, width=0, height=0):
        """This init is for a rectangle"""
        self.width = width
        self.height = height
        Rectangle.num_of_instances += 1

    def __str__(self):
        """it prints a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        size = "#" * self.__width
        rectangle = []
        for ind in range(self.__height):
            rectangle.append(size)
        return "\n".join(rectangle)

    def __repr__(self):
        """it returns a representation of the rectangle"""
        return "{}({}, {})".format((type(self).__name__), self.__width,
                                   self.__height)

    def __del__(self):
        """

        this deletes the rectangle and decreases the
        number of instances
        """
        Rectangle.num_of_instances -= 1
        print("Bye rectangle...")

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
        """a rectangle height collector"""
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
        """a rectangle area getter"""
        return self.__height * self.__width

    def perimeter(self):
        """

        this returns the perimeter of the rectangle,
        or nothing if height/width are 0
        """
        if self.__height == 0 or self.__width == 0:
            return
        return (self.__height * 2) + (self.__width * 2)
