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
        f = lambda x: (x + 1)%10
        self.assertEquals(8, collision_point(9, f))

    def test_terminating_non_terminating(self):
        from eop.ch2 import terminating
        f = lambda x: (x + 1)%10
        self.assertFalse(terminating(2, f, p=lambda x: x != 10))

    def test_collision_point_terminating(self):
        from eop.ch2 import collision_point
        f = lambda x: (x + 1)%10
        self.assertEquals(1, collision_point(2, f))

    def test_terminating_non_terminating(self):
        from eop.ch2 import terminating
        f = lambda x: (x + 1)%10
        self.assertFalse(terminating(2, f, p=lambda x: x != 10))

    def test_collision_point_nonterminating_orbit(self):
        from eop.ch2 import collision_point_nonterminating_orbit
        f = lambda x: (x + 1)%10
        self.assertEquals(1, collision_point_nonterminating_orbit(2, f))

    def test_circular_nonterminating_orbit_iscircular(self):
        from eop.ch2 import circular_nonterminating_orbit
        f = lambda x: (x + 1)%10
        self.assertTrue(circular_nonterminating_orbit(2, f))

    def test_circular_nonterminating_orbit_isnotcircular(self):
        from eop.ch2 import circular_nonterminating_orbit
        f = lambda x: (x + 1)%10 if x > 20 else x + 2
        self.assertFalse(circular_nonterminating_orbit(1, f))

    def test_circular_terminating_not_circular(self):
        from eop.ch2 import circular
        f = lambda x: x + 1
        self.assertFalse(circular(1, f, p=lambda x: x < 70))

    def test_circular_terminating_not_circular(self):
        from eop.ch2 import circular
        f = lambda x: (x + 1)%10
        self.assertTrue(circular(1, f, p=lambda x: x < 70))

    def test_convergent_point(self):
        from eop.ch2 import convergent_point
        f = lambda x: x + 1 if x < 10 else x%10 + 11
        self.assertEquals()
