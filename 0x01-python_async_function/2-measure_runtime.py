#!/usr/bin/env python3
"""
measures the total execution time for wait_n(n, max_delay), and returns
total_time / n
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Args:
        n (int): [number of times wait_random will be called]
        max_delay (int): [maximun value of delay]
    Returns:
        float: [average of the time taken by wait_random]
    """
    start_time = time.perf_counter()
    await wait_n(n, max_delay)
    end_time = time.perf_counter()
    return (end_time - start_time)/n

