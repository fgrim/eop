# -*- coding: utf-8 -*-
"""
    This contains the exercises and examples from Elements of Programming Chapter 2: Transforms and Their Orbits
"""
import itertools

def power_unary(x, n, f):
    """
        This function calculates the function f^{n}(x) where n \element N,
        f^{n}(x) = { x, n == 0 or f^{n-1}(f(x)) if n > 0
    """
    return reduce(lambda g, h: lambda x: g(h(x)), itertools.repeat(f, n))(x)

def distance(x, y, f):
    """
        This function calculates the number of steps between x and y under
        the transformation f.  The pre condition here is that y is reachable from x via
        f
    """
    n = 0
    while x != y:
        x = f(x)
        n += 1
    return n

def collision_point(x, f, p=lambda x: True):
    """
        Given a transformation f this algorithm either finds the terminal point of the transformation
        or a y such that y = f^{n}(x) = f^{2n + 1}(x).  The definition space predicate p may be used
        to indicate a halting condition
    """
    if not p(x):
        return x

    slow, fast = x, f(x)
    while slow != fast:
        slow = f(slow)
        if not p(fast):
            return fast
        fast = f(fast)
        if not p(fast):
            return fast
        fast = f(fast)
    return fast

def terminating(x, f, p=lambda x: True):
    """
        This returns True if the transformation did not have a cycle from x to the terminal otherwise False
    """
    return not p(collision_point(x, f, p))
