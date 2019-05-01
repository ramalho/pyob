import sys

import uintset

class EmptySet:

    def __len__(self):
        return 0

    def __contains__(self, element):
        return False

    def __or__(self, other):
        return other

    __ror__ = __or__

    def __and__(self, other):
        return self

    __rand__ = __and__

    def __repr__(self):
        return 'EmptySet()'



Empty = EmptySet()
