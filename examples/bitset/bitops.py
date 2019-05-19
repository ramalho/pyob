import sys


def count_ones(bigint):
    count = 0
    while bigint:
        count += bigint & 1
        bigint >>= 1
    return count


def get_bit(bigint, index):
    return bool(bigint & (1 << index))


def set_bit(bigint, index):
    return bigint | (1 << index)


def unset_bit(bigint, index):
    if get_bit(bigint, index):
        return bigint ^ (1 << index)
    return bigint


def find_ones(bigint):
    index = 0
    while True:
        if bigint & 1:
            yield index
        bigint >>= 1
        if bigint == 0:
            break
        index += 1
