#!/usr/bin/env python3
"""Module conatining function to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a Python vriable to a kv pair"""
    return k, v ** 2
