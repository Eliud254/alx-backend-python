#!/usr/bin/env python3

"""
This module contains a function that creates a multiplier function
to multiply a float by a given multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier to be used in the function.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the result of multiplying it by the given multiplier.
    """

    def multiplier_func(number: float) -> float:
        """
        Multiply a float by the multiplier.

        Args:
            number (float): The float to be multiplied.

        Returns:
            float: The result of multiplying the float by the multiplier.
        """
        return multiplier * number
