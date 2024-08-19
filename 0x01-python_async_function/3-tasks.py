#!/usr/bin/env python3
"""task_wait_random that takes an integer
max_delay and returns a asyncio.Task."""

import asyncio
wait_random = __import__(
    '0-basic_async_syntax').wait_randomwait_random = __import__(
        '0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Asynchronous coroutine that takes in 2 int arguments (n and max_delay)
    and returns a list of delays.

    Args:
        n (int): Number of times wait_random() will be called.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of delays in increasing order.
    """
    return asyncio.create_task(wait_random(max_delay))
