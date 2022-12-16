#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 13, part 1.

I hate recursion :-)
"""

from itertools import zip_longest


def test(left: list, right: list) -> bool | None:
    """Return True if in right order, else False."""
    for lval, rval in zip_longest(left, right):
        if lval is None:  # Left side ran out
            return True
        if rval is None:  # Right side ran out)
            return False

        ltype = type(lval)
        rtype = type(rval)

        if list in (rtype, ltype):
            if rtype == int:
                rslt = test(lval, [rval])
            elif ltype == int:
                rslt = test([lval], rval)
            else:
                rslt = test(lval, rval)
            if rslt is not None:
                return rslt

        if ltype == int and rtype == int:
            if lval < rval:
                return True
            if rval < lval:
                return False
    return None


with open('input', encoding='ascii') as fp:
    eol = '\n'
    idx = 1
    in_right_order = []
    while eol == '\n':
        first = eval(fp.readline())
        second = eval(fp.readline())
        eol = fp.readline()
        if test(first, second):
            in_right_order.append(idx)
        idx += 1
    # print(in_right_order)
    print(sum(in_right_order))  # 5529
