#!/usr/bin/env python3
"""[execute multiple coroutines at the same time with async]"""

import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """[execute multiple coroutines at the same time with async]
    Args:
        n (int): [number of times wait_random will be called]
        max_delay (int): [maximun value of delay]
    Returns:
        list: [list of all the delays (float values)]
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    list_delays = []
    for i in range(n):
        list_delays.append(wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(list_delays)]
