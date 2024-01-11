#!/usr/bin/env python3
"""Annotate the below function’s parameters and return
values with the appropriate types

def element_length(lst):
    return [(i, len(i)) for i in lst]

{'lst': typing.Iterable[typing.Sequence], 'return': \
    typing.List[typing.Tuple[typing.Sequence, int]]}
"""


import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> \
        typing.List[typing.Tuple[typing.Sequence, int]]:
    """Returns a list of tuples"""
    return [(i, len(i)) for i in lst]
