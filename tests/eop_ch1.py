# -*- coding: utf-8 -*-
"""
    Tests cases for the algorithms in eop.ch1
"""

import unittest

class ChapterOneTest(unittest.TestCase):

    def test_pair_equals(self):
        from eop.ch1 import Pair
        p1, p2 = Pair(m0=1, m1=2), Pair(m0=1, m1=2)
        self.assertTrue(p1 == p2)

    def test_pair_not_equals(self):
        from eop.ch1 import Pair
        p1, p2 = Pair(m0=1, m1=2), Pair(m0=2, m1=1)
        self.assertFalse(p1 == p2)

    def test_pair_lt_dim1(self):
        from eop.ch1 import Pair
        p1, p2 = Pair(m0=1, m1=2), Pair(m0=2, m1=2)
        self.assertTrue(p1 < p2)

    def test_pair_lt_dim2(self):
        from eop.ch1 import Pair
        p1, p2 = Pair(m0=2, m1=1), Pair(m0=2, m1=2)
        self.assertTrue(p1 < p2)

    def test_triple_equals(self):
        from eop.ch1 import Triple
        t1, t2 = Triple(m0=1, m1=2, m2=3), Triple(m0=1, m1=2, m2=3)
        self.assertTrue(t1 == t2)

    def test_triple_not_equals(self):
        from eop.ch1 import Triple
        t1, t2 = Triple(m0=1, m1=2, m2=3), Triple(m0=2, m1=1, m2=3)
        self.assertFalse(t1 == t2)

    def test_triple_lt_dim1(self):
        from eop.ch1 import Triple
        t1, t2 = Triple(m0=1, m1=2, m2=3), Triple(m0=2, m1=2, m2=3)
        self.assertTrue(t1 < t2)

    def test_triple_lt_dim2(self):
        from eop.ch1 import Triple
        t1, t2 = Triple(m0=2, m1=1, m2=3), Triple(m0=2, m1=2, m2=3)
        self.assertTrue(t1 < t2)
