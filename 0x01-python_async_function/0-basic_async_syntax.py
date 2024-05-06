#!/usr/bin/env python3
import asyncio
import random


async def wait_random(max_delay=10):
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds.
    :param max_delay: Maximum delay (default 10 seconds)
    :return: Random delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


# Example usage
async def main():
    """
    Example usage of wait_random.
    """
    print(await wait_random())
    print(await wait_random(5))
    print(await wait_random(15))


if __name__ == "__main__":
    asyncio.run(main())

