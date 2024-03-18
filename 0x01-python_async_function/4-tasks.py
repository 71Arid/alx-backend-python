#!/usr/bin/env python3
"""
Take the code from wait_n and alter it
into a new function task_wait_n.
The code is nearly identical to wait_n except
task_wait_random is being called.
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    creates a list of coroutines
    uses ayncio.gather to gather them
    sorts using sorted
    """
    srt_list: List[float] = []
    for _ in range(n):
        srt_list.append(wait_random(max_delay))
    wait_n = await asyncio.gather(*srt_list)
    return sorted(wait_n)
