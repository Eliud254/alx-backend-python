#!/usr/bin/env python3
"""The function which converts  Python variable to the KV pair."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Convertes Python variable to the KV pair."""
    return k, v ** 2