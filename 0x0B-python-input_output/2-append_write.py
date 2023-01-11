#!/usr/bin/python3
"""2-append_write.py"""
"""A function that appends a text to a file"""


def append_write(filename="", text=""):
    """Appends a text to a file"""
    with open(filename, mode='a', encoding='utf-8') as f:
        f.write(text)
    with open(filename, encoding='utf-8') as f:
        l = len(f.read())
    return (l)
