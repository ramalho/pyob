===============================
Lab 1: enhancing ``Coordinate``
===============================

Your goal is to enhance the ``Coordinate`` class, adding the following features:

* Create an ``__init__`` accepting a latitude and a longitude.
* Create ``reference_system`` class attribute.
* Create a ``geohash`` method using the ``encode`` function from the ``geohash.py`` module.

General instructions
====================

Edit the ``coordinate.py`` module in this directory.

Use the examples in this ``README.rst`` as **doctests** to guide your work.

To run tests, use ``doctest`` with the ``-f`` option (for "fail fast", to stop at first failure)::

    $ python3 -m doctest README.rst -f


Step 1
======

Implement ``__init__`` taking latitude and longitude, both optional with ``0.0`` as default.

Example::

    >>> from coordinate import Coordinate
    >>> gulf_of_guinea = Coordinate()
    >>> gulf_of_guinea
    Coordinate(0.0, 0.0)
    >>> greenwich = Coordinate(51.5)
    >>> greenwich
    Coordinate(51.5, 0.0)
    >>> london = Coordinate(51.5, -0.1)
    >>> print(london)
    51.5°N, 0.1°W


Step 2
======

Create a class attribute named ``reference_system`` with value ``'WGS84'``.

Example::

    >>> Coordinate.reference_system
    'WGS84'
    >>> cleveland = Coordinate(41.5, -81.7)
    >>> cleveland.reference_system
    'WGS84'


Step 3
======

Use the ``encode`` function of the ``geohash.py`` module
to create a ``geohash`` method in the ``Coordinate`` class.

Here is how to use the ``encode`` function::

    >>> import geohash
    >>> geohash.encode(41.40, -81.85)   # CLE airport
    'dpmg92wskz27'

After you implement the ``geohash`` method, this should work::

    >>> cleveland = Coordinate(41.5, -81.7)
    >>> cleveland.geohash()
    'dpmuhfggh08w'
