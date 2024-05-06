import asyncio
import random

async def wait_random(max_delay=10):
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

# Example usage
async def main():
    print(await wait_random())
    print(await wait_random(5))
    print(await wait_random(15))

if __name__ == "__main__":
    asyncio.run(main())

