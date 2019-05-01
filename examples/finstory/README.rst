Financial History Example
=========================

``FinancialHistory`` instances keep track of a person's expenses and income.

.. note::  This example is adapted from *Smalltalk-80: the language*,
           by Adele Goldberg and Dave Robson (Addison-Wesley, 1989).

The interface of ``FinancialHistory`` consists of:

``__init__(amount)``
    Begin a financial history with an amount given (default: 0).

``__repr__()``
    Return string representation of the instance, for debugging.

``receive(amount, source)``
    Receive an amount from the named source.

``spend(amount, reason)``
    Spend an amount for the named reason.

``balance()``
    Return total amount currenly on hand.

``received_from(source)``
    Return total amount received from the given source.

``spent_for(reason)``
    Return total amount spent for the given reason.


Demonstration
-------------

Create ``FinancialHistory`` with $ 100::

    >>> from finstory import FinancialHistory
    >>> h = FinancialHistory(100)
    >>> h
    <FinancialHistory balance: 100.00>

Spend some money::

    >>> h.spend(39.95, 'meal')
    >>> h
    <FinancialHistory balance: 60.05>

Decimals can be formatted like floats::

    >>> print(f'${h.balance:0.2f}')
    $60.05

Get more money::

    >>> h.receive(1000.01, "Molly's game")
    >>> h.receive(10.00, 'found on street')
    >>> h
    <FinancialHistory balance: 1070.06>

Spend more money::

    >>> h.spend(55.36, 'meal')
    >>> h.spend(26.65, 'meal')
    >>> h.spend(300, 'concert')
    >>> h
    <FinancialHistory balance: 688.05>

Check amount spent on meals::

    >>> h.spent_for('meal')
    Decimal('121.96')

Check amount spent on travel (zero):

    >>> h.spent_for('travel')
    Decimal('0')
