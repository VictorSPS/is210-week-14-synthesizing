#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fibonacci sequencw generator"""


def xfibo(count):
    """Function creates Fibonacci sequence
    Args:
        count(int): the number of Fibonacci numbers to return.
    Returns: 
        A Fibonacci sequence starting with 0
    Examples:
        >>> for i in xfibo(5):
                print i
        0
        1
        1
        2
        3
    """
    iteration = 0
    curnum, lastnum = 0, 1
    while iteration < count:
        yield curnum
        curnum, lastnum = lastnum, curnum + lastnum
        iteration += 1
