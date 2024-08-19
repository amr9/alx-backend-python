#!/usr/bin/env python3
"""Basic async syntax"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a randomdelay
    between 0 and max_delay (inclusive).

    Args:
        max_delay (float): Maximum delay in seconds (default is 10 seconds).

    Returns:
        float: Random delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
