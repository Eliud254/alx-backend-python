#!/usr/bin/env python3
"""
function that returns the list of integers
multiplied by certain factor.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """The list of integers multiplied by certain factor.
    Args:
        lst: Turple integers.
        factor: An integer.
    Returns:
        List of the integers.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)