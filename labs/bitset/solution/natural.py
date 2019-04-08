import sys

class NaturalSet:

    def __len__(self):
        return sys.maxsize

    def __contains__(self, element):
        return element >= 0

    def __or__(self, other):
        return N

    __ror__ = __or__

    def __and__(self, other):
        return other

    __rand__ = __and__

    def __repr__(self):
        return 'NaturalSet()'



N = NaturalSet()
