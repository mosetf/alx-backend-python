#!/usr/bin/env python3
"""[Basic Async Syntax]"""
import asyncio
import random


async def wait_random(max_delay=10):
    """Coroutine that waits for a random delay between 0 and max_delay
    Args:
        max_delay (int, optional): [maximun value of delay]. Defaults to 10.
    Returns:
        [float]: random delay
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay

if __name__ == "__main__":
    asyncio.run(wait_random())
