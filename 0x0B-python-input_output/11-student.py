#!/usr/bin/python3
"""Defines a class Student based on 10-student.py"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the attributes of the student instance

        Args:
            first_name (str): The student's first name
            last_name (str): The student's last name
            age (int): The student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dicionary representation of the student instance"""
        if attrs is None:
            return self.__dict__
        else:
            return ({attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)})

    def reload_from_json(self, json):
        """Replace all attributes of Student instance using
        the provided json dictionary"""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
