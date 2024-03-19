#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and
write a measure_runtime coroutine that will
execute async_comprehension four times in parallel
using asyncio.gather.
measure_runtime should measure the total runtime and return it.
Notice that the total runtime is roughly 10 seconds,
explain it to yourself.
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    creates four async_comprehension instances
    the uses async.gather to execute them in parallel
    """
    start_time = time.time()
    execute_four = [async_comprehension() for i in range(4)]
    await asyncio.gather(*execute_four)
    return time.time() - start_time
