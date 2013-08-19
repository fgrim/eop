# -*- coding: utf-8 -*-
"""
    This contains the exercises and examples from Elements of Programming Chapter 1: Foundations
"""

import collections

class Pair(collections.namedtuple('Pair', 'm0 m1')):

    __slots__ = ()

    def __eq__(self, oth):
        return self.m0 == oth.m0 and self.m1 == oth.m1

    def __lt__(self, oth):
        return self.m0 < oth.m0 or ((not oth.m0 < self.m0) and (self.m1 < oth.m1))

class Triple(collections.namedtuple('Triple', 'm0 m1 m2')):

    __slots__ = ()

    def __eq__(self, oth):
        return self.m0 == oth.m0 and self.m1 == oth.m1 and self.m2 == oth.m2

    def __lt__(self, oth):
        return self.m0 < oth.m0 or (
                (not oth.m0 < self.m0) and self.m1 < oth.m1) or (
                        (not oth.m1 < self.m1) and self.m2 < oth.m2);
