import sys


def count_ones(bigint):
    count = 0
    while bigint:
        count += bigint & 1
        bigint >>= 1
    return count


def get_bit(bigint, index):
    return (bigint >> index) & 1


def set_bit(bigint, index):
    return bigint | (1 << index)


def set_all_bits(bigint):
    res = 0
    while True:
        res |= 1
        if bigint < 2:
            break
        bigint >>= 1
        res <<= 1
    return res


def unset_bit(bigint, index):
    unset_mask = set_all_bits(bigint) ^ (1 << index)
    print(f'\n{unset_mask:b}')
    return bigint & unset_mask
