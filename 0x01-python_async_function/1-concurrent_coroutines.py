#!/usr/bin/env python3
"""
import wait_random from the previous python file that you've
written and write an async routine wait_n takes 2 int arguments
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
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
