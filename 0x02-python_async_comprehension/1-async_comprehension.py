#!/usr/bin/env python3
""" 
Asynchronously generates a sequence of floats using an async generator.
"""
from typing import Generator
import asyncio


async def async_comprehension() -> Generator[float, None, None]:
    """
    Asynchronously generates a sequence of floats using an async generator.

    Returns:
        A generator that yields floats.
    """
    async_generator = __import__('0-async_generator').async_generator

    return [number async for number in async_generator()]
