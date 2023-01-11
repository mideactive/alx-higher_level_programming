#!/usr/bin/python3
"""1-write_file.py"""
"""A function that counts the number of text in a file"""


def write_file(filename="", text=""):
    """Writes to a file and counts the number of text in the file"""
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(text)
    with open(filename, encoding='utf-8') as f:
        n_text = len(f.read())
    return (n_text)
