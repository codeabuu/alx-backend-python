#!/usr/bin/env python3
'''Import wait_random from the previous python file
that you’ve written and write an async routine
called wait_n that takes in 2 int arguments'''


from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''loop and return'''
    delays = []
    p = []

    for i in range(n):
        tasks = wait_random(max_delay)
        p.append(tasks)

    for tasks in asyncio.as_completed((p)):
        delay = await tasks
        delays.append(delay)

    return delays
