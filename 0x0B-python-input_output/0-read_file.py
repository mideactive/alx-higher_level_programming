#!/usr/bin/python3
"""0-read_file.py"""
"""A function that reads a file in (UTF-8) and prints it's output to stdout"""


def read_file(filename=""):
    """Reads a file and prints it's output to stdout"""
    with open(filename,  encoding="utf-8") as f:
        print(f.read(), end="")
