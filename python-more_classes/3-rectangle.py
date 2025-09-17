#!/usr/bin/python3
"""
3-rectangle module
Contains Rectangle class with width, height, area, perimeter and string representation
"""


class Rectangle:
    """Rectangle class with width, height, area, perimeter and string rep"""

    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = []
        for i in range(self.__height):
            rectangle_str.append("#" * self.__width)
        return "\n".join(rectangle_str)
