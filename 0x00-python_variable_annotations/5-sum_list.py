#!/usr/bin/env python3
from typing import List
"""
This module uses List from typing library to enable type
annotation
type annotated function sum_list which takes a list input_list
of floats as arguments and returns their sum as a float
"""


def sum_list(input_list: List[float]) -> float:
    """
    for loop that finds sum of all float values
    args:
        input_list: A list of floats to be summed.

    Returns:
        The sum of the floats in the input_list, as a float.
    """
    s: float = 0
    for i in input_list:
        s += i
    return s
