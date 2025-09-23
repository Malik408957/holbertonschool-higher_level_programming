#!/usr/bin/python3
"""
Student class module with serialization/deserialization
"""


class Student:
    """Defines a student with serialization and deserialization capabilities"""

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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance with filter

        Args:
            attrs (list): List of attribute names to include (optional)

        Returns:
            dict: Dictionary containing filtered student attributes
        """
        if attrs is None:
            # Return all attributes
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            # Return only specified attributes that exist
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance from JSON dictionary

        Args:
            json (dict): Dictionary containing attribute names and values
        """
        for key, value in json.items():
            setattr(self, key, value)
