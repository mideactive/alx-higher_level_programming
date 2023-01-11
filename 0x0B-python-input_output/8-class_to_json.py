#!/usr/bin/python3
# 8-class_to_json.py
"""function that returns the dictionary
description with simple data structure
"""
import json


def class_to_json(obj):
    """list, dictionary, string, integer and boolean"""
    return (obj.__dict__)
