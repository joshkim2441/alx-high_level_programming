#!/usr/bin/python3
"""Defines the class Student function"""


class Student:
    """Represents a student with basic information"""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance

        Args:
            first_name (str): The student's first name
            last_name (str): The student's last name
            age (int): The student's age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a JSON-serializable dictionary representation of the student

        Args:
            attrs (list, optional): A list of attribute names to include

        Return:
           dict: A dictionary representation of the student
        """

        result = {}
        if attrs is None:
            attrs = self.__dict__.keys()  # Get all attributes
        for attr in attrs:
            if hasattr(self, attr):  # ensure attribute exists
                result[attr] = getattr(self, attr)
        return result
