"""Main module."""

import random


def call_unpack(f, s):
    if isinstance(s, str):
        return f(s)
    elif s is not None:
        return f(*s)
    else:
        return f()


class Node:
    ID = 0

    def __init__(self, *children):
        Node.ID += 1
        self.id = Node.ID
        self.parent = None
        self.children = list(children)

        # set childerm parent
        for c in self.children:
            c.parent = self

    def __call__(self, *args):
        self._args = args
        # self._f(*self._args, **self._kwds)
        return self

    def __eq__(a, b):
        return a.id == b.id and\
               a.parent == b.parent and\
               a.children == b.children

    def __and__(a, b):
        assert isinstance(a, Node) and isinstance(b, Node)

        if isinstance(a, And):
            a.children.append(b)
            return a
        else:
            return And(a, b)

    def __or__(a, b):
        assert isinstance(a, Node) and isinstance(b, Node)

        if isinstance(a, Or):
            a.children.append(b)
            return a
        else:
            return Or(a, b)

    def __rshift__(a, b):
        assert isinstance(a, Node) and isinstance(b, Node)

        if isinstance(a, Seq):
            a.children.append(b)
            return a
        else:
            return Seq(a, b)


class And(Node):
    def execute(self, *args):
        # aync calls
        return [call_unpack(c.execute, args) for c in self.children]


class Or(Node):
    def execute(self, *args):
        # aync calls
        res = [call_unpack(c.execute, args) for c in self.children]
        return res[random.randint(0, len(res) - 1)]


class Seq(Node):
    def execute(self, *args):
        res = None
        for c in self.children:
            res = call_unpack(c.execute, res)
        return res


class Async_Fun(Node):
    def __init__(self, f):
        super().__init__()
        self._f = f
        self._args = []

    def execute(self, *args):
        if len(args) > 0:
            self._args = args
        # print(*self._args, **self._kwds)
        return self._f(*self._args)

    def __call__(self, *args):
        af = Async_Fun(self._f)
        af._args = args
        # self._f(*self._args, **self._kwds)
        return af


def async_function(func):
    """
    decorator
    """
    return Async_Fun(func)
