#!/usr/bin/env python3
'''asynchronous coroutine that takes in an integer argument'''


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''function to await'''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
