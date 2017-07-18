#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `async_composition` package."""


import unittest

from async_composition import async_function, And, Seq, Or


class TestAsync_composition(unittest.TestCase):
    """Tests for `async_composition` package."""

    def setUp(self):
        """Set Up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_hello(self):
        @async_function
        def my_fun():
            return 'hello'

        @async_function
        def my_fun2(name):
            return '{}!'.format(name)

        @async_function
        def concat(s1, s2):
            return s1 + ' ' + s2

        @async_function
        def print1(s):
            return s + ' [from print1]'

        @async_function
        def print2(s):
            return s + ' [from print2]'

        c = Seq(And(my_fun,
                    my_fun2('luca')),
                concat,
                Or(print1,
                   print2))

        res = c.execute()

        from async_composition.utils import print_graph
        print_graph(c)

        self.assertIn('hello luca!', res)
