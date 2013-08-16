# -*- coding: utf-8 -*-
"""
    Tests cases for the algorithms in eop.ch2
"""

import unittest

class ChapterTwoTest(unittest.TestCase):
    def test_power_unary(self):
        from eop.ch2 import power_unary
        f = lambda x: 2*x
        self.assertEquals(f(f(f(10))), power_unary(10, 3, f))

    def test_distance(self):
        from eop.ch2 import distance
        f = lambda x: 2*x
        self.assertEquals(3, distance(10, 80, f))

    def test_collision_point_non_terminating(self):
        from eop.ch2 import collision_point
        f = lambda x: x%10
        self.assertEquals(9, collision_point(9, f))

    def test_terminating_non_terminating(self):
        from eop.ch2 import terminating
        f = lambda x: x%10
        self.assertFalse(terminating(9, f, p=lambda x: x != 10))

    def test_collision_point_terminating(self):
        from eop.ch2 import collision_point
        f = lambda x: x%10
        self.assertEquals(9, collision_point(9, f))

    def test_terminating_non_terminating(self):
        from eop.ch2 import terminating
        f = lambda x: x%10
        self.assertFalse(terminating(9, f, p=lambda x: x != 10))
