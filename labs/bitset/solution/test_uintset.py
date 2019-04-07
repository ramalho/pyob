import pytest

from uintset import UintSet


def test_len():
    s = UintSet()
    assert len(s) == 0


def test_add():
    s = UintSet()
    s.add(0)
    assert len(s) == 1


def test_add_multiple():
    s = UintSet()
    s.add(1)
    s.add(3)
    s.add(1)
    assert len(s) == 2


def test_not_number():
    s = UintSet()
    with pytest.raises(TypeError) as e:
        s.add('A')
    assert e.value.args[0] == "'UintSet' elements must be integers >= 0"  


def test_add_negative():
    s = UintSet()
    with pytest.raises(ValueError) as e:
        s.add(-1)
    assert e.value.args[0] == "'UintSet' elements must be integers >= 0"  


def test_contains_zero_not():
    s = UintSet()
    assert 0 not in s


def test_contains_zero():
    s = UintSet()
    s.add(0)
    assert 0 in s


def test_new_from_iterable():
    s = UintSet([1, 100, 3])  # beyond word 0
    assert len(s) == 3
    assert 1 in s
    assert 3 in s
    assert 100 in s


def test_new_from_empty_iterable():
    s = UintSet([])
    assert len(s) == 0


def test_iter():
    s = UintSet([1, 5, 0, 3, 2, 4])
    assert list(s) == [0, 1, 2, 3, 4, 5]


def test_repr_empty():
    s = UintSet()
    assert repr(s) == 'UintSet()'


def test_repr():
    s = UintSet([1, 5, 0, 3, 2, 4])
    assert repr(s) == 'UintSet({0, 1, 2, 3, 4, 5})'


@pytest.mark.parametrize("first, second, want", [
    (UintSet(), UintSet(), True),
    (UintSet([1]), UintSet(), False),
    (UintSet(), UintSet([1]), False),
    (UintSet([1, 100]), UintSet([1, 101]), False),
    (UintSet([1, 100]), [1, 101], False),
])
def test_eq(first, second, want):
    assert (first == second) is want

@pytest.fixture
def union_cases():
    return [
        (UintSet(), UintSet(), UintSet()),
        (UintSet([1]), UintSet(), UintSet([1])),
        (UintSet(), UintSet([1]), UintSet([1])),
        (UintSet([1, 100]), UintSet([100, 1]), UintSet([100, 1])), # beyond word 0
        (UintSet([1, 100]), UintSet([2]), UintSet([1, 2, 100])),
    ]


def test_or_op(union_cases):
    for s1, s2, want in union_cases:
        got = s1 | s2
        assert got == want


'''
def test_union(union_cases):
    for s1, s2, want in union_cases:
        got = s1.union(s2)
        assert len(got) == len(want)
        assert got == want


def test_union_iterable(union_cases):
    for s1, s2, want in union_cases:
        it = list(s2)
        got = s1.union(it)
        assert len(got) == len(want)
        assert got == want


def test_union_iterable_multiple():
    s = UintSet([1, 3, 5])
    it1 = [2, 4, 6]
    it2 = {10, 11, 12}
    want = UintSet({1, 2, 3, 4, 5, 6, 10, 11, 12})
    got = s.union(it1, it2)
    assert got == want


@pytest.fixture
def intersection_cases():
    return [
        (UintSet(), UintSet(), UintSet()),
        (UintSet([1]), UintSet(), UintSet()),
        (UintSet([1]), UintSet([1]), UintSet([1])),
        (UintSet([1, 100]), UintSet([100, 1]), UintSet([100, 1])), # beyond word 0
        (UintSet([1, 100]), UintSet([2]), UintSet()),
        (UintSet([1, 2, 3, 4]), UintSet([2, 3, 5]), UintSet([2, 3])),
    ]


def test_and_op(intersection_cases):
    for s1, s2, want in intersection_cases:
        got = s1 & s2
        assert len(got) == len(want)
        assert got == want


def test_intersection(intersection_cases):
    for s1, s2, want in intersection_cases:
        got = s1.intersection(s2)
        assert len(got) == len(want)
        assert got == want


@pytest.fixture
def symmetric_diff_cases():
    return [
        (UintSet(), UintSet(), UintSet()),
        (UintSet([1]), UintSet(), UintSet([1])),
        (UintSet([1]), UintSet([1]), UintSet()),
        (UintSet([1, 100]), UintSet([100, 1]), UintSet()), # beyond word 0
        (UintSet([1, 100]), UintSet([2]), UintSet([1, 100, 2])),
        (UintSet([1, 2, 3, 4]), UintSet([2, 3, 5]), UintSet([1, 4, 5])),
    ]


def test_xor_op(symmetric_diff_cases):
    for s1, s2, want in symmetric_diff_cases:
        got = s1 ^ s2
        assert len(got) == len(want)
        assert got == want


def test_symmetric_difference(symmetric_diff_cases):
    for s1, s2, want in symmetric_diff_cases:
        got = s1.symmetric_difference(s2)
        assert len(got) == len(want)
        assert got == want


@pytest.fixture
def difference_cases():
    return [
        (UintSet(), UintSet(), UintSet()),
        (UintSet([1]), UintSet(), UintSet([1])),
        (UintSet([1]), UintSet([1]), UintSet()),
        (UintSet([1, 100]), UintSet([100, 1]), UintSet()), # beyond word 0
        (UintSet([1, 100]), UintSet([2]), UintSet([1, 100])),
        (UintSet([1, 2, 3, 4]), UintSet([2, 3, 5]), UintSet([1, 4])),
    ]


def test_sub_op(difference_cases):
    for s1, s2, want in difference_cases:
        got = s1 - s2
        assert len(got) == len(want)
        assert got == want


def test_difference(difference_cases):
    for s1, s2, want in difference_cases:
        got = s1.difference(s2)
        assert len(got) == len(want)
        assert got == want


def test_remove():
    test_cases = [
        (UintSet([0]), 0, UintSet()),
        (UintSet([1, 2, 3]), 2, UintSet([1, 3])),
    ]
    for s, elem, want in test_cases:
        s.remove(elem)
        assert s == want


def test_remove_all():
    elems = [1, 2, 3]
    set = UintSet(elems)
    for e in elems:
        set.remove(e)
    assert len(set) == 0


def test_remove_not_found():
    s = UintSet()
    elem = 1
    with pytest.raises(KeyError) as excinfo:
        s.remove(elem)
    assert str(excinfo.value) == str(elem)


def test_remove_not_found_2():
    s = UintSet([1, 3])
    elem = 2
    with pytest.raises(KeyError) as excinfo:
        s.remove(elem)
    assert str(excinfo.value) == str(elem)


def test_pop_not_found():
    s = UintSet()
    with pytest.raises(KeyError) as excinfo:
        s.pop()
    assert 'pop from an empty set' in str(excinfo.value)


def test_pop():
    test_cases = [0, 1, WORD_SIZE-1, WORD_SIZE, WORD_SIZE+1, 100]
    for want in test_cases:
        s = UintSet([want])
        got = s.pop()
        assert got == want
        assert len(s) == 0


def test_pop_all():
    want = [100, 1, 0]
    s = UintSet(want)
    got = []
    while s:
        got.append(s.pop())
        assert len(s) == (len(want) - len(got))
    assert got == want
'''
