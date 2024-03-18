#!/usr/bin/env python3
"""
an asynchronous routine that takes in an integer argument named
wait_random that waits for a random delay between 0 and max_delay
seconds and eventually returns it
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    variable val holds the random value
    asyncio.sleep waits for random time
    val is returned
    """
    val = random.random() * max_delay
    await asyncio.sleep(val)
    return val
