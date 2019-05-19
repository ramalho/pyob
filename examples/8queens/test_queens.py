from pytest import mark

from queens import aligned, all_safe


@mark.parametrize("source, target, expected", [
    ((1, 1), (1, 2), True),
    ((1, 1), (2, 2), True),
    ((1, 1), (2, 1), True),
    ((1, 1), (1, 3), True),
    ((1, 1), (2, 3), False),
    ((1, 1), (3, 3), True),
    ((1, 1), (3, 1), True),
    ((1, 1), (3, 2), False),
])
def test_aligned(source, target, expected):
    assert expected == aligned(source, target)
    assert expected == aligned(target, source)


@mark.parametrize("positions, expected", [
    ([(1, 1)], True),
    ([(1, 1), (1, 2)], False),
    ([(1, 1), (2, 3)], True),
    ([(1, 1), (1, 2), (2, 3)], False),
    ([(1, 1), (2, 3), (3, 2)], False),
    ([(1, 1), (2, 3), (3, 5)], True),
    ([(4, 5), (1, 1), (3, 2), (2, 4)], True),
])
def test_all_safe(positions, expected):
    assert expected == all_safe(positions)
