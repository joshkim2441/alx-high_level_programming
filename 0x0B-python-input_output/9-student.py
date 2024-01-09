#!/usr/bin/python3
"""Defines the class Student function"""


class Student:
    """Represents the class Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a representation of the Student instance"""
        return self.__dict__
