import unittest

from async_composition import async_function, Executor, Async_Fun, af


# TODO: fix the decorator
# @async_function
def my_fun():
    return 'hello'


# @async_function
def my_fun2(name):
    return '{}'.format(name)


# @async_function
def concat(s1, s2, s3):
    return ' '.join((s1, s2, s3))


# @async_function
def print1(s):
    return s + ' [from print1]'


# @async_function
def print2(s):
    return s + ' [from print2]'


class TestAsync_composition(unittest.TestCase):
    """Tests for `async_composition` package."""

    def setUp(self):
        """Set Up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_hello(self):
        # c = (my_fun & my_fun2('luca') & my_fun2('genoveffa')) >>\
        #     concat >>\
        #     (print1 | print2)

        par = af(my_fun) & af(my_fun2)('luca') & af(my_fun2)('genoveffa')  # And
        print_ = af(print1) | af(print2)  # Or
        c = par >> af(concat) >> print_  # Seq
        from async_composition.utils import print_graph
        print_graph(c)

        ex = Executor()
        res = ex.run(c)

        self.assertIn('hello luca genoveffa', res)
