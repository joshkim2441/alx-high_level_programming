#!/usr/bin/python3
"""Defines the load_from_json_file function"""
import json


def load_from_json_file(filename):
    """Deserializes a JSON file into a Python object

    Args:
    filename: The name of the JSON file to load

    Returns:
        The desrialized Python object
    """

    with open(filename, "r") as f:
        return json.load(f)
