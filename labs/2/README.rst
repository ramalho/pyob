===========================
Lab 2: enhancing ``Budget``
===========================

Your goal is to enhance the ``camping.Budget`` class.

As implemented, ``camping.Budget`` does not allow adding contributor names after the budget is created.
Implement an ``.include(name)`` method to allow adding a contributor with an optional contribution.

General instructions
====================

Use the examples in this ``README.rst`` as **doctests** to guide your work.

To run tests, use ``doctest`` with the ``-f`` option (for "fail fast", to stop at first failure)::

    $ python3 -m doctest README.rst -f


Step 1
======

Implement ``include`` taking a name and an optional contribution (default: 0.0).

Example::

    >>> from camping import Budget
    >>> b = Budget('Debbie', 'Ann', 'Charlie')
    >>> b.total()
    0.0
    >>> b.people()
    ['Ann', 'Charlie', 'Debbie']
    >>> b.contribute("Debbie", 40.00)
    >>> b.contribute("Ann", 10.00)
    >>> b.include("Bob", 15)
    >>> b.people()
    ['Ann', 'Bob', 'Charlie', 'Debbie']
    >>> b.contribute("Bob", 20)
    >>> b.total()
    85.0

Step 2 (bonus)
==============

An alternative to such a method would be to change the contribute method,
removing the code that tests whether the contributor's name is found in ``self._campers``.
This would be simpler, but is there a drawback to this approach?
Discuss with tutorial participants near you.
