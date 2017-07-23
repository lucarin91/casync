import unittest

from casync import async_function, And, Seq, Or, Executor, af
from casync.utils import print_graph


# @async_function
def my_fun():
    return 'hello'


# @async_function
def my_fun2(name):
    return '{}!'.format(name)


# @async_function
def concat(s1, s2):
    return s1 + ' ' + s2


# @async_function
def print1(s):
    return s + ' [from print1]'


# @async_function
def print2(s):
    return s + ' [from print2]'


class Testcasync(unittest.TestCase):
    """Tests for `casync` package."""

    def setUp(self):
        """Set Up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_hello(self):

        c = Seq(And(af(my_fun),
                    af(my_fun2)('luca')),
                af(concat),
                Or(af(print1),
                   af(print2)))

        print_graph(c)

        ex = Executor()

        res = ex.run(c)

        self.assertIn('hello luca!', res)
