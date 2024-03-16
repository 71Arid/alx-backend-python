#!/usr/bin/env python3
"""
Annonating a given functiions parameter and return value
"""
from typing import List, Iterator, Sequence, Tuple


def element_length(lst: Iterator[Sequence]) -> List[Tuple[Sequence, int]]:
    """a return value of type List[Tuple[Sequence, int]]
    """
    return [(i, len(i)) for i in lst]
