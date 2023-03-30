#!/usr/bin/env python3
"""Module containing function makemultiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Multiplies a float by a multiplier
    Args:
        multiplier (float): The multiplier
    Returns:
        A function that multiplies a float by mltiplier
    """

    def multiplier_func(number: float) -> float:
        """Multiplies a float by multiplier"""
        return multiplier * number

    return multiplier_func
