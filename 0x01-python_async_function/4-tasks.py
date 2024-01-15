#!/usr/bin/env python3
"""4. Tasks"""
import asyncio
from typing import List

async def wait_n(n: int, max_delay: int) -> List[float]:
    """[summary]

    Args:
        n (int): [number of times wait_random will be called]
        max_delay (int): [maximun value of delay]

    Returns:
        List[float]: [list of all the delays (float values)]
    """
    task_wait_random = __import__('3-tasks').task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
