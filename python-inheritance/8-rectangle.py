#!/usr/bin/python3
"""
8-rectangle.py
Rectangle class that inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initialize Rectangle with width and height

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        # Validate width
        self.integer_validator("width", width)
        self.__width = width

        # Validate height
        self.integer_validator("height", height)
        self.__height = height
