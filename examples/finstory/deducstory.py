import collections
import decimal

from finstory import FinancialHistory, new_decimal

class DeductibleHistory(FinancialHistory):

    def __init__(self, initial_balance=0.0):
        super().__init__(initial_balance)
        self._deductions = decimal.Decimal(0)

    def spend(self, amount, reason, deducting=0.0):
        """Record expense with partial deduction"""
        super().spend(amount, reason)
        if deducting:
            self._deductions += new_decimal(deducting)

    def spend_deductible(self, amount, reason):
        """Record expense with full deduction"""
        self.spend(amount, reason, amount)

    @property
    def deductions(self):
        return self._deductions
