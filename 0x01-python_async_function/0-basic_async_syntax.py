#!/usr/bin/env python3
"""
Includes a coroutine that halts execution for a specified period before yielding control back.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This function creates a random decimal number between 0 and a specified maximum delay.

    Parameters:
    - max_delay: The upper limit for the delay time.

    Returns:
    - A randomly generated decimal number within the range of 0 to max_delay.
    """
    # Generate a random delay between 0 and max_delay
    rand = random.uniform(0, max_delay)
    # Asynchronously sleep for the generated delay
    await asyncio.sleep(rand)
    # Return the generated delay
    return rand

