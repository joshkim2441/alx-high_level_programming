#!/usr/bin/python3
"""Define append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a new line of txt after each line containing
    a specific string in a file

    Args:
        filename (str): The name of the file to modify
        search_string (str): The string to search for in the file
        new_string (str): The line of text to insert after
        each matching line
    """

    with open(filename, "r+") as f:
        lines = f.readlines()
        f.seek(0) # Rewind to the beginning of the file

        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
        f.truncate() # Adjust file size to match new content
