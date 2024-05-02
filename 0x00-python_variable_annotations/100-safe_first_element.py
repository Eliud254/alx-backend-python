#!/usr/bin/env python3
"""augment code with the correct duck-typed annotations."""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """The first element of the list .None if the list is empty."""
    if lst:
        return lst[0]
    else:
        return None