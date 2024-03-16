#!/usr/bin/env python3
"""
This module uses List from typing library to enable type
annotation
type annotated function sum_list which takes a list input_list
of floats as arguments and returns their sum as a float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    args:
        input_list: A list of floats to be summed.

    Returns:
        The sum of the floats in the input_list, as a float.
    """
    s: float = 0
    for i in input_list:
        s += i
    return s
