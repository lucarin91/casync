#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `async_composition` package."""


import unittest

from async_composition import async_function


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
            return '{}'.format(name)

        @async_function
        def concat(s1, s2, s3):
            return ' '.join((s1, s2, s3))

        @async_function
        def print1(s):
            return s + ' [from print1]'

        @async_function
        def print2(s):
            return s + ' [from print2]'

        # c = (my_fun & my_fun2('luca') & my_fun2('genoveffa')) >>\
        #     concat >>\
        #     (print1 | print2)

        par = my_fun & my_fun2('luca') & my_fun2('genoveffa')  # And

        print_ = print1 | print2  # Or

        c = par >> concat >> print_  # Seq

        res = c.execute()

        from async_composition.utils import print_graph
        print_graph(c)

        self.assertIn('hello luca genoveffa', res)
