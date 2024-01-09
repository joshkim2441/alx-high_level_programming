#!/usr/bin/python3
"""Define the save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """Serializes an Object to a text file using a JSON representation

    Args:
        my_obj: The object to be serialized.
        filename: The name of the file to write th JSON data to
    """

    with open(filename, 'w+') as f:
        json.dump(my_obj, f, indent=4)  # Indent for readability
