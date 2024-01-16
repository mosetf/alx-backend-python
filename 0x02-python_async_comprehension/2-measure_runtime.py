#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime of the async_comprehension function.

    Returns:
        The runtime of the async_comprehension function in seconds.
    """
    n = time.perf_counter()
    comprehensions = [async_comprehension() for _ in range(4)]

    results = await asyncio.gather(*comprehensions)

    return (time.perf_counter() - n)
