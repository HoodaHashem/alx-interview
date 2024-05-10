#!/usr/bin/python3
"""
minimum operation problem
"""


def minOperations(n):
    """minimum ops"""

    if n <= 1:
        return n
    ops = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            ops += divisor
            n //= divisor
        divisor += 1
    return ops
