#!/usr/bin/python3
"""2-append_write.py"""
"""A function that appends a text to a file"""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file."""
    with open(filename, mode='a', encoding='utf-8') as f:
        k = f.write(text)
    return (k)
