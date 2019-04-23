import collections
import decimal

decimal.setcontext(decimal.BasicContext)

def new_decimal(value):
    """Builds a Decimal using the cleaner float `repr`"""
    if isinstance(value, float):
        value = repr(value)
    return decimal.Decimal(value)


class FinancialHistory:

    def __init__(self, initial_balance=0.0):
        self._balance = new_decimal(initial_balance)
        self._incomes = collections.defaultdict(decimal.Decimal)
        self._expenses = collections.defaultdict(decimal.Decimal)

    def __repr__(self):
        name = self.__class__.__name__
        return f'<{name} balance: {self._balance:.2f}>'

    @property
    def balance(self):
        return self._balance


    def receive(self, amount, source):
        amount = new_decimal(amount)
        self._incomes[source] += amount
        self._balance += amount

    def spend(self, amount, reason):
        amount = new_decimal(amount)
        self._expenses[reason] += amount
        self._balance -= amount

    def received_from(self, source):
        return self._incomes[source]

    def spent_for(self, reason):
        return self._expenses[reason]
