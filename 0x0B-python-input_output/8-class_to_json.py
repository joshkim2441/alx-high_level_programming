#!/usr/bin/python3
"""Returns the dictionary description with simple data structure"""


def class_to_json(obj):
    """Converts a class instance to a JSON-serializable dictionary

    Args:
        obj: The class instance to convert

    Returns:
        A dictionary representing the object's attributes
    """

    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[key] = value
        elif isinstance(value, object):
            result[key] = class_to_json(value)
        else:
            raise TypeError(f"Unsupported type: {type(value)}")
    return result
