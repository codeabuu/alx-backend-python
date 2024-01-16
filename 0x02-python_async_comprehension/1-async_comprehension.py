#!/usr/bin/env python3
'''coroutine will collect 10 random numbers using an async comprehensing '''


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''return random numbers'''
    collect = [i async for i in async_generator()]
    return collect
