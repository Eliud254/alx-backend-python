#!/usr/bin/env python3
"""
This script defines an asynchronous coroutine that introduces a delay before yielding control back.
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that simulates a random delay before yielding control.

    Parameters:
    - max_delay: The upper limit for the delay time.
    
    Returns:
    - A randomly generated decimal number within the range of 0 to max_delay.
    """
    # Generate a random delay between 0 and max_delay
    rand_delay = random.uniform(0, max_delay)
    # Asynchronously sleep for the generated delay
    await asyncio.sleep(rand_delay)
    # Return the generated delay
    return rand_delay

