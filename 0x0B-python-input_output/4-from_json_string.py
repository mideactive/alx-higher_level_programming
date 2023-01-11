#!/usr/bin/python3
# 4-from_json_string.py
"""A function that returns an object represented by json string"""
import json


def from_json_string(my_str):
    """Returns an object represented by json string"""
    return (json.loads(my_str))
