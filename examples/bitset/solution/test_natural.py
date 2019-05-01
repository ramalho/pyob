import sys

import pytest

from natural import N
from uintset import UintSet


def test_len():
    assert len(N) == sys.maxsize


def test_contains():
    assert 0 in N
    assert 1 in N
    assert -1 not in N
    assert 42 in N
    assert sys.maxsize in N


union_cases = [
        (N, UintSet()),
        (N, UintSet([1])),
        (UintSet([1]), N),
        (UintSet([1, 100]), N),
    ]

@pytest.mark.parametrize("first, second", union_cases)
def test_or_op(first, second):
     got = first | second
     assert got == N


intersection_cases = [
        (N, UintSet(), UintSet()),
        (N, UintSet([1]), UintSet([1])),
        (UintSet([1]), N, UintSet([1])),
        (UintSet([1, 100]), N, UintSet([1, 100])),
    ]

@pytest.mark.parametrize("first, second, want", intersection_cases)
def test_and_op(first, second, want):
     got = first & second
     assert got == want
