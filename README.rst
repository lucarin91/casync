=================
Async Composition
=================

..
.. .. image:: https://img.shields.io/pypi/v/casync.svg
..         :target: https://pypi.python.org/pypi/casync
..
.. .. image:: https://img.shields.io/travis/lucarin91/casync.svg
..         :target: https://travis-ci.org/lucarin91/casync
..
.. .. image:: https://readthedocs.org/projects/async-composition/badge/?version=latest
..         :target: https://async-composition.readthedocs.io/en/latest/?badge=latest
..         :alt: Documentation Status
..
.. .. image:: https://pyup.io/repos/github/lucarin91/casync/shield.svg
..      :target: https://pyup.io/repos/github/lucarin91/casync/
..      :alt: Updates


Simple library to compose asynchronous functions in different patterns. The composition creates a graph that can be executed in parallel by different kind of executor (i.e., thread pool, event loop).

**DISCLAIMER:** this library is in early development stage. Most of the features are not available.

.. * Documentation: https://async-composition.readthedocs.io.

Installation
------------

For now, the library can be installed only from source and require Python 3. Download the repository with::

  git clone https://github.com/lucarin91/casync

inside the folder do this command to install the library::

  python setup.py install

After this, it is possible to tests the library using the examples in the ``examples``folder.

How use
--------
It is possible to compose functions in three different ways:

* **Sequential composition** (``Seq``), execute all the function one after the other::

  fun1 >> fun2

* **And composition** (``And``), the functions are executed concurrently. After all the functions ended their execution their results are passed ahead as a list::

  fun1 & fun2

* **Or composition** (``Or``), the function are executed concurrently, but when the first function terminates all the other are stopped::

  fun1 | fun2

An example of usage::

  from casync import af, Executor

  def fun1():
    return 'hello'

  def fun2():
    return 'world'

  def concat (s1, s2):
    return s1 + ' ' + s2

  comp1 = af(fun1) & af(fun2)
  comp2 = af(fun1) | af(fun2)
  comp3 = comp1 >> af(concat)


  ex = Executor()
  res = ex(comp1)  # ['hello', 'world']
  res = ex(comp2)  # 'hello' or 'world'
  res = ex(comp3)  # 'hello world'


Features
--------
* Create a computational graph with ``and(&)``, ``or(|)` and ``seq(>>)`` constructors.
* Execute graph in parallel using a python `multithreading` library.

Todo
----
* Support of composition of all kind of function and lambdas.
* Use decorators to easy the declaration of functions.
* Implement synchronisation of data during the execution of the graph.
* Implement different executors (i.e., event-loop with build in IO functionality).
* support Python 2.7 at least.

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

Licence
----------
MIT license
