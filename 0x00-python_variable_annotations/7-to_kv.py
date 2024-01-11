#!/usr/bin/env python3
"""Write a type-annotated function to_kv that takes a string k
and an int OR float v as arguments and returns a tuple.
"""


import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """returns"""
    return (k, float(v * v))
