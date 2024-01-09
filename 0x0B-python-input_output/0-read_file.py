#!/usr/bin/python3
"""Defines read_file function"""


def read_file(filename=""):
    """Reads a file (UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
