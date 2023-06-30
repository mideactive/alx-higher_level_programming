#!/usr/bin/python3
"""
    A function that finds a peak in a list of unsorted integers"
"""


def find_peak(list_of_integers):
    """ Return the max number from a list.

    list_of_integers: list
    """
    if len(list_of_integers) == 0:
        return None
    peak = list_of_integers[0]
    for i in range(1, len(list_of_integers)):
        if list_of_integers[i] > peak:
            peak = list_of_integers[i]
    return peak
