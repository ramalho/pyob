import sys

import pytest

from empty import Empty
from uintset import UintSet


def test_len():
    assert len(Empty) == 0


def test_contains():
    assert 0 not in Empty
    assert 1 not in Empty
    assert -1 not in Empty
    assert 42 not in Empty
    assert sys.maxsize not in Empty


union_cases = [
        (Empty, UintSet(), UintSet()),
        (Empty, UintSet([1]), UintSet([1])),
        (UintSet([1]), Empty, UintSet([1])),
        (UintSet([1, 100]), Empty, UintSet([1, 100])),
    ]

@pytest.mark.parametrize("first, second, want", union_cases)
def test_or_op(first, second, want):
     got = first | second
     assert got == want

intersection_cases = [
        (Empty, UintSet()),
        (Empty, UintSet([1])),
        (UintSet([1]), Empty),
        (UintSet([1, 100]), Empty),
    ]

@pytest.mark.parametrize("first, second", intersection_cases)
def test_and_op(first, second):
     got = first & second
     assert got == Empty
