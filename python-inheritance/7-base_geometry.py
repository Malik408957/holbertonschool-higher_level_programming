#!/usr/bin/python3
"""
This module contains a BaseGeometry class with area and validator methods.
"""


class BaseGeometry:
    """
    A base geometry class with area method and integer validator.
    """

    def area(self):
        """
        Calculate the area. This method is not implemented yet.

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value.

        Args:
            name (str): The name of the value (for error messages)
            value: The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
