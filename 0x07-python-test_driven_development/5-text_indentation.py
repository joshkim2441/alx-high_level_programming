#!/usr/bin/python3
"""Defines a "5-text_indentation" function"""


def text_indentation(ext):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')

    lines = text.split('\n')
    lines = [line.strip() for line in lines]

    print('\n'.join(lines))
