import random

from multiprocessing import Pool
from multiprocessing.pool import AsyncResult

from .async_fun import Node, Or, Seq, And, Async_Fun


def _get_or_wait(value):
    return value.get() if isinstance(value, AsyncResult) else value


class Executor:
    def __init__(self):
        self._pool = Pool()

    def close(self):
        self._pool.close()

    def __call__(self, g):
        return self._run(g)

    def _run(self, g):
        assert isinstance(g, Node)

        res = self._rec_run(g)
        return _get_or_wait(res)

    def _rec_run(self, node, inputs=[]):
        # print(node.id)
        if isinstance(node, Or):
            # res = None
            # def call(r):
            #     print('res or', r)
            #     res = r
            results = []
            for c in node.children:
                results.append(
                    self._rec_run(c, inputs)  # , callback=call)
                )
            random.shuffle(results)  # only for DEBUG
            while True:
                for r in results:
                    if r.ready():
                        # TODO: stop all other tasks
                        return _get_or_wait(r)
                # print('Or:', value)
        elif isinstance(node, And):
            results = []
            for c in node.children:
                results.append(
                    self._rec_run(c, inputs)
                )
            res = []
            for r in results:
                value = _get_or_wait(r)
                # print('And:', value)
                res.append(value)
            return res
        elif isinstance(node, Seq):
            res = []
            for c in node.children:
                res = self._rec_run(c, _get_or_wait(res))
            return res
        elif isinstance(node, Async_Fun):
            # print('inputs:', inputs)
            return self._pool.apply_async(node.execute, [inputs])
