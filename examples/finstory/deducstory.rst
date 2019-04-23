Financial History with Deductible Expenses Example
==================================================

``DeductibleHistory`` instances keep track of a person's expenses and income,
including expenses that are deductible

.. note::  This example is adapted from *Smalltalk-80: the language*,
           by Adele Goldberg and Dave Robson (Addison-Wesley, 1989).

Class ``DeductibleHistory`` inherits methods and properties from ``FinancialHistory``, plus:

``spend(amount, reason, deducting=0.0)``
    Spend an amount for the named reason, with an optional partial deduction.

``spend_deductible(amount, reason)``
    Spend an amount for the named reason, with full deduction.

The total amount of deductions is available in the ``deductions`` read-only property.
    


Demonstration
-------------

Create ``DeductibleHistory`` with $ 100.

    >>> from deducstory import DeductibleHistory
    >>> h = DeductibleHistory(1000)
    >>> h
    <DeductibleHistory balance: 1000.00>

Spend some money on a deductible course::

    >>> h.spend(600, 'course', 150)
    >>> h
    <DeductibleHistory balance: 400.00>

Make a donation::

    >>> h.spend_deductible(250, 'charity')
    >>> h
    <DeductibleHistory balance: 150.00>

Check amount spent on "charity"::

    >>> h.spent_for('charity')
    Decimal('250')

Check balance::

    >>> h.balance
    Decimal('150')

Get total deductions::

    >>> h.deductions
    Decimal('400')
