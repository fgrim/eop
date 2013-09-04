# -*- coding: utf-8 -*-
"""
    This contains the exercises and examples from Elements of Programming Chapter 2: Transforms and Their Orbits
"""
import itertools

from .ch1 import Triple

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

def collision_point_nonterminating_orbit(x, f):
    """
        This detects the collision point in a transformation that has a cycle
    """
    slow, fast = x, f(x)
    while fast != slow:
        slow = f(slow)
        fast = f(f(fast))

    return fast

def circular_nonterminating_orbit(x, f):
    """
        This checks that an orbit is circular.  A circular orbit is one
        whose distance between the collision point and the beginning of the orbit
        is 1
    """
    return x == f(collision_point_nonterminating_orbit(x, f))

def circular(x, f, p=lambda x: True):
    """
        This returns a boolean indicating whether a given transformation has a circular
        segment or not
    """
    y = collision_point(x, f, p)
    return p(y) and x == f(y)

def convergent_point(x0, x1, f):
    """
        The covergent point is value where h steps from x and h + 1 steps from the collision point
        we arrive at the connection point of the cycle in f.
        Precondition: $(\exists n \in \func{DistanceType}(F))\,n \geq 0 \wedge f^n(x0) = f^n(x1)$
    """
    while x0 != x1:
        x0, x1 = f(x0), f(x1)
    return x0

def connection_point_nonterminating_orbit(x, f):
    """
    Returns the connection point in an orbit with a circular element
    """
    return convergent_point(
            x, f(collision_point_nonterminating_orbit(x, f)), f)

def connection_point(x, f, p):
    """
    The connection point is the point in the transform where the handle terminates
    at the start of a non-terminating cycle
    Precondition: $p(x) \Leftrightarrow \text{$f(x)$ is defined}$
    """
    y = collision_point(x, f, p)
    if not p(y):
        return y
    return convergent_point(x, f(y), f)

def intersection(x, y, f, p):
    """
        Exercise 2.2 Design an algorithm that determines, given a transformation
        and its definition state predicate, whether the orbits of two elements
        intersect.
    """

def convergent_point_guarded(x0, x1, y, f):
    """
    Exercise 2.3 For convergent_point to work, it must be called with elements whose distances
    to the convergent point are equal.  Implement an algorithm convergent_point_guarded for use
    when that is not to be the case, but there is an element in common to the orbits of both
    """
    d0 = distance(x0, y, f)
    d1 = distance(x1, y, f)
    if d0 < d1:
        x1 = power_unary(x1, d1 - d0, f)
    elif d1 < d0:
        x0 = power_unary(x0, d0 - d1, f)
    return convergent_point(x0, x1, f)

def orbit_structure_nonterminating_orbit(x, f):
    """
        This returns a triple representing the components of
        a nonterminating orbit.  The values of the triple conform to
        the following specification
        Case            m0      m1      m2
        Terminating     h - 1   0       terminal element
        Circular        0       c - 1   x
        \\rho shaped    h       c - 1   connection point

        Where h is defined as the handle size and c is defined as the cycle size
    """
    y = connection_point_nonterminating_orbit(x, f)
    return Triple(m0=distance(x, y, f), m1=distance(f(y), y, f), m2=y)

def orbit_structure(x, f, p):
    """
       Precondition: $p(x) \Leftrightarrow \text{$f(x)$ is defined}$
    """
    y = connection_point(x, f, p)
    m, n = distance(x, y, f), 0
    if p(y):
        n = distance(f(y), y, f)
        # Terminating: $m = h - 1 \wedge n = 0$
        # Otherwise:   $m = h \wedge n = c - 1$
    return Triple(m0=m, m1=n, m2=y)

"""
    Project 2.1 Another way to detect a cycle is to repeatedly test a single
    advancing element for equality with a sotred element while replacing
    the stored element at ever-increasing intervals.  This and other ideas
    are described in Sedgewick et. al. (1979), Brent (1980), and Levy (1982).
    Implement other algorithms for orbit analysis, compare their performance
    for different applications, and develop a new set of recommendations for
    selecting the appropriate algorithm.
"""
