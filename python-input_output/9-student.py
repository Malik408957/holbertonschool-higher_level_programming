#!/usr/bin/python3
"""
Student class module
"""


class Student:
    """Defines a student by first_name, last_name and age"""

    def __init__(self, first_name, last_name, age):
        """
        Initialize student instance

        Args:
            first_name (str): Student's first name
            last_name (str): Student's last name
            age (int): Student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance

        Returns:
            dict: Dictionary containing student attributes
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
