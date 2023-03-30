#!/usr/bin/env python3
"""Module containing function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes a mixed list of integers and floats and returns
    sum of all the numbers in the list as float"""
    return sum(mxd_lst)
