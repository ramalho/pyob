from pytest import mark

from queens_and_guard import aligned


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
