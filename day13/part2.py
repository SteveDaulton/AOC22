#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 13, part 2.

First time I've come across cmp_to_key.
https://docs.python.org/3/library/functools.html#functools.cmp_to_key
https://www.geeksforgeeks.org/how-does-the-functools-cmp_to_key-function-works-in-python/
"""

from itertools import zip_longest
from functools import cmp_to_key


def test(left: list, right: list) -> int:
    """Return -1 if in right order, else +1."""
    for lval, rval in zip_longest(left, right):
        if lval is None:  # Left side ran out
            return -1
        if rval is None:  # Right side ran out)
            return 1

        ltype = type(lval)
        rtype = type(rval)

        if list in (rtype, ltype):
            if rtype == int:
                rslt = test(lval, [rval])
            elif ltype == int:
                rslt = test([lval], rval)
            else:
                rslt = test(lval, rval)
            if rslt != 0:
                return rslt

        if ltype == int and rtype == int:
            if lval < rval:
                return -1
            if rval < lval:
                return 1
    return 0


with open('input', encoding='ascii') as fp:
    data = [eval(line.strip()) for line in fp if line.strip() != '']
    data.append([[2]])
    data.append([[6]])
    data = sorted(data, key=cmp_to_key(test))
    sidx = data.index([[2]]) + 1
    eidx = data.index([[6]]) + 1
    print(sidx * eidx)  # 27690
