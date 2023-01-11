#!/usr/bin/python3
import json
"""3-to_json_string.py"""
"""Defines a string-to-JSON function."""


def to_json_string(my_obj):
    """Return json representation o an object"""
    obj = json.dumps(my_obj)

    return (obj)
