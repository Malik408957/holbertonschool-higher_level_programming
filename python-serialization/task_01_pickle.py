#!/usr/bin/python3
"""
Custom object serialization using pickle
"""

import pickle


class CustomObject:
    """A custom class for pickle serialization demonstration"""

    def __init__(self, name, age, is_student):
        """
        Initialize CustomObject

        Args:
            name (str): The name
            age (int): The age
            is_student (bool): Student status
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display object attributes in a formatted way"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object to a file using pickle

        Args:
            filename (str): The filename to save the serialized object

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            return True
        except Exception as e:
            print(f"Serialization error: {e}")
            return False

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file using pickle

        Args:
            filename (str): The filename to load the object from

        Returns:
            CustomObject: The deserialized object or None if error
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Deserialization error: {e}")
            return None
