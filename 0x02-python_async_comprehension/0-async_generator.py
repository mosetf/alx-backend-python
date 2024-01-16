#!/usr/bin/env python3
"""0. Async Generator"""
import asyncio
import random
import time


async def async_generator():
    """
    Asynchronous generator that yields random numbers between 0 and 10.
    """
    for _ in range(10):
        time.sleep(1)
        yield random.uniform(0, 10)
