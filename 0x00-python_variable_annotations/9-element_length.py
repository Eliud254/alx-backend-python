#!/usr/bin/env python3
"""The function having annotated parameters and
returns the  values with appropriate types."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """Returns the list of tuples with a  length of each element"""
    return [(i, len(i)) for i in lst]