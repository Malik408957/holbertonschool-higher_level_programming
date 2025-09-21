#!/usr/bin/python3
"""
10-square.py
Square class that inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initialize Square with size

        Args:
            size (int): size of the square (both width and height)
        """
        # Validate size using integer_validator from BaseGeometry
        self.integer_validator("size", size)

        # Initialize Rectangle with size for both width and height
        super().__init__(size, size)

        # Make size private (optional since we inherit from Rectangle)
        self.__size = size
