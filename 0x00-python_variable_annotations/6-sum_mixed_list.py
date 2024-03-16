#!/usr/bin/env python3
"""
type annotated function sum_mixed_list which takes a list mx_lst
of intergers and floats and returns their sum as a float
"""
from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """
    return a float sum from a list of floats and ints
    """
    s: float = 0
    for i in mxd_lst:
        s += i
    return s
