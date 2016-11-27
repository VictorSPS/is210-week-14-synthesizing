#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_02. Using a list comprehension"""

import task_01


def fibo(count):
    """Function takes only one argument.
    Args:
        count(int): the total number of Fibonacci numbers
    Returns: 
        a list of Fibonacci numbers
    Examples:
        >>> fibo(5)
        [0, 1, 1, 2, 3]
    """
    return [num for num in task_01.xfibo(count)]
