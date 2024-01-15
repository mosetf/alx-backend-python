#!/usr/bin/env python3
"""4. Tasks"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """[summary]

    Args:
        n (int): [number of times wait_random will be called]
        max_delay (int): [maximun value of delay]

    Returns:
        List[float]: [list of all the delays (float values)]
    """
    list_delays = [task_wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(list_delays)]
