import bitops


INVALID_ELEMENT_MESSAGE = "'UintSet' elements must be integers >= 0"

class UintSet:

    def __init__(self, elements=None):
        self._bigint = 0
        if elements:
            for e in elements:
                self.add(e)

    def __len__(self):
        return bitops.count_ones(self._bigint)

    def add(self, elem):
        try:
            self._bigint = bitops.set_bit(self._bigint, elem)
        except TypeError:
            raise TypeError(INVALID_ELEMENT_MESSAGE)
        except ValueError:
            raise ValueError(INVALID_ELEMENT_MESSAGE)

    def __contains__(self, elem):
        try:
            return bitops.get_bit(self._bigint, elem)
        except TypeError:
            raise TypeError(INVALID_ELEMENT_MESSAGE)
        except ValueError:
            raise ValueError(INVALID_ELEMENT_MESSAGE)

    def __iter__(self):
        return bitops.get_ones(self._bigint)

    def __repr__(self):
        elements = ', '.join(str(e) for e in self)
        if elements:
            elements = '{' + elements + '}'
        return f'UintSet({elements})'

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self._bigint == other._bigint

    def __or__(self, other):
        cls = self.__class__
        if isinstance(other, cls):
            res = cls()
            res._bigint = self._bigint | other._bigint
            return res
        return NotImplemented

    def union(self, *others):
        cls = self.__class__
        res = cls()
        res._bigint = self._bigint
        for other in others:    
            if isinstance(other, cls):
                res._bigint |= other._bigint
            try:
                second = cls(other)
            except TypeError:
                raise TypeError("expected UintSet or iterable argument")
            else:
                res._bigint |= second._bigint
        return res

    def __and__(self, other):
        cls = self.__class__
        if isinstance(other, cls):
            res = cls()
            res._bigint = self._bigint & other._bigint
            return res
        return NotImplemented

    def intersection(self, *others):
        cls = self.__class__
        res = cls()
        res._bigint = self._bigint
        for other in others:    
            if isinstance(other, cls):
                res._bigint &= other._bigint
            try:
                second = cls(other)
            except TypeError:
                raise TypeError("expected UintSet or iterable argument")
            else:
                res._bigint &= second._bigint
        return res

