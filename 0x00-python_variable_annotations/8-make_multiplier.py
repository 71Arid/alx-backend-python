#!/usr/bin/env python3
"""
type annotated function make_multiplier that takes a float multiplier
as an argument and returns function that multiplies float
by a multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes float and return a function that multiplies
    multiplier by multiplier
    """
    def func(x: float) -> float:
        return x * multiplier
    x: Callable[[float], float] = func
    return x
