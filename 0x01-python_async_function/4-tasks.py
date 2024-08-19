#!/usr/bin/env python3
"""Tasks"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that takes in 2 int arguments (n and max_delay)
    and returns a list of delays.

    Args:
        n (int): Number of times wait_random() will be called.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of delays in increasing order.
    """
    delays = [task_wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
