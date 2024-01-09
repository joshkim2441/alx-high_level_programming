#!/usr/bin/python3
"""Defines to_json_string function"""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of an objecct (string)
    Args:
        my_obj: The string to represent
    Returns:
        JSON representation
    """

    return json.dumps(my_obj)
