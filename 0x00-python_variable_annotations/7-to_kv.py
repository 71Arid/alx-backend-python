#!/usr/bin/env python3
"""
type annotated function to_kv that takes a string k and an
int of float as arguments an returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    k - first element of tuple (str)
    v - second element of tuple (square of int/float)
    """
    tp: Tuple[str, float] = (k, v * v)
    return tp
