#!/usr/bin/env python3
'''Create a measure_time function with integers n and
max_delay as arguments that measures the total
execution time for wait_n'''


import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''other meth'''
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    total = end - start
    return (total/n)
