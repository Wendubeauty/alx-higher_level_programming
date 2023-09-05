#!/usr/bin/python3
"""This is a definition of a rectangle"""


class Rectangle:
    """a rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This init is for a rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        return "{:s}({:d}, {:d})".format((type(self).__name__), self.__width,
                                   self.__height)

    def __del__(self):
        """

        this deletes the rectangle and decreases the
        number of instances
        """
        Rectangle.number_of_instances -= 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """After comparing, this returns the bigger rectangle"""
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """this initializes a new square instance"""
        return cls(size, size)
